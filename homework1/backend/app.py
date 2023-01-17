from flask import Flask
from flask_cors import CORS

from app_init import db
from app_controller import app_controller
import os

url = os.environ.get('DATABASE_URL')

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = url
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.register_blueprint(app_controller)
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)