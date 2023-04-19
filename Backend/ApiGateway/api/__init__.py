from flask import Flask
from flask_cors import CORS

def create_app():
    app = Flask(__name__)
    from .user import user
    from .review import review
    app.register_blueprint(user, url_prefix='/user')
    app.register_blueprint(review, url_prefix='/review')
    return app

app = create_app()
CORS(app)