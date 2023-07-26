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

password = os.getenv('SNOWFLAKE_PASSWORD')
schema = os.getenv('SNOWFLAKE_SCHEMA')
user = os.getenv('SNOWFLAKE_USER')
account = os.getenv('SNOWFLAKE_ACCOUNT')
database = os.getenv('SNOWFLAKE_DATABASE')
warehouse = os.getenv('SNOWFLAKE_WAREHOUSE')

engine = create_engine(f'snowflake://{user}:{password}@{account}/{database}/{schema}?warehouse={warehouse}', echo=True)
Session = sessionmaker(bind=engine)

@app.route('/cat', methods=['GET'])
def get_cat():
    try:
        res = requests.get('https://api.thecatapi.com/v1/images/search')
        data = res.json()[0]['url']
        
        session = Session()
        new_cat_pic = CatPic(url=data)  
        session.add(new_cat_pic)
        session.commit()

        return jsonify({'newCatPic': {'id': new_cat_pic.id, 'url': data}, 'meow': 'Meow'}), 200
    except Exception as e:
        logging.error(e)
        return jsonify({'message': str(e)}), 400

@app.route('/all-cats', methods=['GET'])
def get_all_cats():
    try:
        session = Session()
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
