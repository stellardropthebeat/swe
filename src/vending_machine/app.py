"""This module is the entry point of the application."""

import os

from app_init import db
from database.stock import Stock
from database.vending_machine import VendingMachine
from flask import Flask
from route.stock_route import stock_controller
from route.vm_route import vm_controller
from sqlalchemy.exc import SQLAlchemyError
from waitress import serve

url: os = os.environ.get("DATABASE_URL")

app: Flask = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


"""Initiate database to app."""
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()
    try:
        db.session.add(VendingMachine(name="test", location="test"))
        db.session.add(Stock(vm_id=1, stock="test", quantity=1))
        db.session.commit()
    except SQLAlchemyError:
        pass


"""Register blueprints to app."""
app.register_blueprint(stock_controller)
app.register_blueprint(vm_controller)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
