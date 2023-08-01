import os
from sqlalchemy import Column, Integer, String, Sequence, MetaData, Boolean
from sqlalchemy.ext.declarative import declarative_base
from dotenv import load_dotenv

metadata = MetaData()
Base = declarative_base(metadata=metadata)

schema = os.getenv('SNOWFLAKE_SCHEMA')

class CatPic(Base):
    __tablename__ = 'catpic'
    __table_args__ = {'schema': schema}

    id = Column(Integer, Sequence('id_seq'), primary_key=True)
    url = Column(String)
    adopted = Column(Boolean, default=False, nullable=False)
    color = Column(String, default='colorful')