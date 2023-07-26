import os
from sqlalchemy import Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

Base = declarative_base()

schema = os.getenv('SNOWFLAKE_SCHEMA')

class CatPic(Base):
    __tablename__ = 'catpic'
    __table_args__ = {'schema': 'PUBLIC'}

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    url = Column(String)
    username = Column(String, default='fred')