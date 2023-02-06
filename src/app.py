"""This module is the entry point of the application."""

import os

from flask import Flask
from waitress import serve

from src.app_init import db
from src.database.model import Stock, VendingMachine
from src.route.stock_route import stock_controller
from src.route.vm_route import vm_controller

url: os = (
    "mysql+pymysql://"
    + os.environ["MYSQL_USER"]
    + ":"
    + os.environ["MYSQL_PASSWORD"]
    + "@"
    + os.environ["MYSQL_DATABASE"]
)
# url: os = "mysql+pymysql://myuser:mypassword@localhost:3306/mydb"

app: Flask = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = url


"""Initiate database to app."""
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()
    db.session.add(VendingMachine(name="test", location="test"))
    db.session.add(Stock(vm_id=1, stock="test", quantity=1))
    db.session.commit()


"""Register blueprints to app."""
app.register_blueprint(stock_controller)
app.register_blueprint(vm_controller)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
