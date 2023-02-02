"""Initialize the sqlalchemy database."""

import os

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

url: os = (
    "mysql+pymysql://"
    + os.environ["MYSQL_USER"]
    + ":"
    + os.environ["MYSQL_PASSWORD"]
    + "@"
    + os.environ["MYSQL_DATABASE"]
)
# url: os = "mysql+pymysql://myuser:mypassword@localhost:3306/mydb"
db_engine: sqlalchemy = sqlalchemy.create_engine(url)

if not database_exists(db_engine.url):
    create_database(db_engine.url)

db: sqlalchemy = SQLAlchemy()
