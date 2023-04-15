from flask import Blueprint, jsonify, request, abort
from flask_mail import Message
from dotenv import load_dotenv
import re

import os
load_dotenv()


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'

def check(email):
    if(re.fullmatch(regex, email)):
        return True
    return False

views = Blueprint("",__name__)

@views.route("/")
def index():
    response = {"message": "ping"}
    return jsonify(response)

@views.route("/contact", methods = ["POST"])
def contact():
    from . import mail, db
    from . import ContactMessage
    if not request.get_json():
        abort(400, description="Not a JSON")
    data = request.get_json()
    email = data.get("email")
    name = data.get("name")
    body = data.get("body")
    if not check(email) or not name or not body:
        abort(400, description="Invalid email format")
    msg = Message("Lehky", sender = os.getenv("email"), recipients = [email])
    msg.body = f'Dear {name},\n\n\nThank you for taking your time to reach out to Lehky, We sincerely do appreciate it\n\nPlease note that your message will be looked into and feedback will be sent to you within a short period of time.\n\nOnce again, thanks for your time.\n\nWarm Regards,\n\nLilly Wanjiku\n\nMD Lilly and Sons enterprise.'
    mail.send(msg)
    msg = Message("New Contact message Notification", sender = os.getenv("email"), recipients = [os.getenv("email")])
    msg.body = f"A new contact message received from {name} with email {email} which goes thus: \n\n{body}\n\nAn autoresponse has been sent to them\n\nPlease see to it "
    mail.send(msg)
    new_contact = ContactMessage(
        name = name,
        email = email,
        body = body
    )
    db.session.add(new_contact)
    db.session.commit()
    return jsonify({"message": "ok"}), 200

@views.route("/sub", methods=["GET", "POST"])
def sub():
    from .import Newsletter
    from . import mail, db, Newsletter
    if request.method == "GET":
        all = []
        subscribers = Newsletter.query.all()
        for s in subscribers:
            all.append(s.email)
        return jsonify(all), 200
    else:
        data = request.get_json()
        email = data.get("email")
        if not email or not check(email):
            abort(400, description="Invalid email format")
        if Newsletter.query.filter_by(email = email).first():
            abort(400, description="You are already a subscriber")
            return jsonify(results)
        new_subscriber = Newsletter(email = email)
        db.session.add(new_subscriber)
        db.session.commit()
        return jsonify({"message":"ok"}), 200

@views.route("/unsub", methods = ["POST"])
def un_sub():
    from . import mail, db, Newsletter
    data = request.get_json()
    email = data.get("email")
    if not email or not check(email):
        abort(400, description="Invalid email format")
    subscriber = Newsletter.query.filter_by(email=email).first()
    if not subscriber:
        abort(400, description="User not a subscriber")
    db.session.delete(subscriber)
    db.session.commit()
    return jsonify({"message":"ok"}), 200

@views.route("/news", methods=["POST"])
def news():
    from . import mail, db, Newsletter
    data = request.get_json()
    message = data.get("message")
    subject = data.get("subject")
    if not message or not subject or (len(message) < 1 or len(subject) < 1):
        abort(400, description="Field can not be empty")
    subscribers = Newsletter.query.all()
    recipients = []
    for sub in subscribers:
        recipients.append(sub.email)
    msg = Message(subject, sender = os.getenv("email"), recipients = recipients)
    msg.body = message
    mail.send(msg)
    return jsonify({"message":"ok"}), 200
