"""This module is the entry point of the application."""

import os

from flask import Flask
from flask_cors import CORS

from app_init import db
from route.stock_route import stock_controller
from route.vm_route import vm_controller

url: os = os.environ.get("DATABASE_URL")

app: Flask = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*", "send_wildcard": "False"}})
app.config["SQLALCHEMY_DATABASE_URI"] = url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

if __name__ == "__main__":
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.register_blueprint(stock_controller)
    app.register_blueprint(vm_controller)
    from waitress import serve

    serve(app, host="0.0.0.0", port=5000)
