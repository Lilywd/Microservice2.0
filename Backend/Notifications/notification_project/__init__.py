''' 
Create a flask project that handles notification service
'''

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from os import path
import os
from dotenv import load_dotenv
from flask_mail import Mail
load_dotenv()

DB_NAME = "notification.db"
db = SQLAlchemy()


from datetime import datetime
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Newsletter(db.Model):
    __tablename__ = "newsletter"
    id = db.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    email = db.Column(db.String(120), unique=True, nullable=False)

class ContactMessage(db.Model):
    __tablename__ = "contact"
    id = db.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    body = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    def _repr__(self):
        return f"Message from {self.name}, date: {self.date_posted}"
def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    app.config['MAIL_SERVER']='smtp.gmail.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USERNAME'] = os.getenv("email")
    app.config['MAIL_PASSWORD'] = os.getenv('password')
    app.config['MAIL_USE_TLS'] = True
    db.init_app(app)
    from .views import views
    app.register_blueprint(views, url_prefix='/')
    create_database(app)
    return app

def create_database(app):
    if not path.exists('notification/' + DB_NAME):
        with app.app_context():
            db.create_all()

app = create_app()
CORS(app)
mail = Mail(app)