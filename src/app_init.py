"""Initialize the sqlalchemy database."""

import os

import sqlalchemy
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import create_database, database_exists

url: os = (
    "postgresql://"
    + os.environ["POSTGRES_USER"]
    + ":"
    + os.environ["POSTGRES_PASSWORD"]
    + "@"
    + os.environ["POSTGRES_DB"]
)
# url: os = "postgresql://myuser:mypassword@localhost:5432/mydb"
db_engine: sqlalchemy = sqlalchemy.create_engine(url)

if not database_exists(db_engine.url):
    create_database(db_engine.url)

db: sqlalchemy = SQLAlchemy()
