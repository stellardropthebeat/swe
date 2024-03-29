"""This module is the entry point of the application."""

import os

from flask import Flask
from waitress import serve

from src.app_init import db
from src.database.model import Stock, StockTimeLine, VendingMachine
from src.route.stock_route import stock_controller
from src.route.stock_timeline import stock_timeline_controller
from src.route.vm_route import vm_controller

url: os = (
    "postgresql://"
    + os.environ["POSTGRES_USER"]
    + ":"
    + os.environ["POSTGRES_PASSWORD"]
    + "@"
    + os.environ["POSTGRES_DB"]
)
# url: os = "postgresql://myuser:mypassword@localhost:5432/mydb"

app: Flask = Flask(__name__)
app.app_context().push()
app.config["SQLALCHEMY_DATABASE_URI"] = url


"""Initiate database to app."""
db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()
    # if VendingMachine is empty add a test entry
    if VendingMachine.query.count() == 0:
        db.session.add(VendingMachine(name="test", location="test"))
        db.session.commit()
    # if Stock is empty add a test entry
    if Stock.query.count() == 0:
        db.session.add(Stock(vm_id=1, stock="test", quantity=1))
        db.session.commit()
    # if StockTimeline is empty add a test entry
    if StockTimeLine.query.count() == 0:
        db.session.add(StockTimeLine(vm_id=1, product_id=1, quantity=1))
        db.session.commit()


"""Register blueprints to app."""
app.register_blueprint(stock_controller)
app.register_blueprint(vm_controller)
app.register_blueprint(stock_timeline_controller)


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=5000)
