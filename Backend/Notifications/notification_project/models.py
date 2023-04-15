from . import db
from datetime import datetime
from fastapi_utils.guid_type import GUID, GUID_DEFAULT_SQLITE


class Newsletter(db.Model):
    __tablename__ = "newsletter"
    id = db.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    email = db.Column(db.String(120), unique=True, nullable=False)

class ContactMessage(db.Model):
    __tablename__ = "contact"
    id = db.Column(GUID, primary_key=True, default=GUID_DEFAULT_SQLITE)
    name = db.Column(db.String(200), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    body = db.Column(db.Text, nullable = False)
    date = db.Column(db.DateTime, nullable= False, default=datetime.utcnow)
    def _repr__(self):
        return f"Message from {self.name}, date: {self.date_posted}"
