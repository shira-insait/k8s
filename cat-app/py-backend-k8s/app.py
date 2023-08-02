from flask import Flask, jsonify, request
import logging
import os
import requests 
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import CatPic
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv()

app = Flask(__name__)
CORS(app)

db_type = os.getenv('DB_TYPE')

if db_type == 'snowflake':
    password = os.getenv('SNOWFLAKE_PASSWORD')
    schema = os.getenv('SNOWFLAKE_SCHEMA')
    user = os.getenv('SNOWFLAKE_USER')
    account = os.getenv('SNOWFLAKE_ACCOUNT')
    database = os.getenv('SNOWFLAKE_DATABASE')
    warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')
    engine = create_engine(f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}', echo=True)
elif db_type == 'pg':
    pg_password = os.getenv('POSTGRES_PASSWORD')
    pg_user = os.getenv('POSTGRES_USER')
    pg_host = os.getenv('POSTGRES_HOST')
    pg_port = os.getenv('POSTGRES_PORT')
    pg_database = os.getenv('POSTGRES_DATABASE')
    pg_schema = os.getenv('POSTGRES_SCHEMA')
    engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}:{pg_port}/{pg_database}?schema={pg_schema}', echo=True)
else:
    raise ValueError('Invalid DB_TYPE')
    
Session = sessionmaker(bind=engine)

@app.route('/cat', methods=['GET'])
def get_cat():
    try:
        res = requests.get('https://api.thecatapi.com/v1/images/search')
        data = res.json()[0]['url']
        
        with Session() as session:
            new_cat_pic = CatPic(url=data)  
            session.add(new_cat_pic)
            session.flush()
            new_cat_pic_id = new_cat_pic.id
            session.commit()

        return jsonify({'newCatPic': {'id': new_cat_pic_id, 'url': data}, 'meow': 'Meow'}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': str(e)}), 400

@app.route('/all-cats', methods=['GET'])
def get_all_cats():
    try:
        with Session() as session:
            all_cats = session.query(CatPic).all()

        return jsonify({'allCats': [{'id': cat.id, 'url': cat.url} for cat in all_cats]}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': str(e)}), 400

@app.route('/health', methods=['GET'])
def get_health():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
