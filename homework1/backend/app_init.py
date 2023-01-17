import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists
import os

url = os.environ.get('DATABASE_URL')

db_engine = sqlalchemy.create_engine(url)

if not database_exists(db_engine.url):
    create_database(db_engine.url)

db = SQLAlchemy()