from flask import Flask
from .routes import bp


def create_app():
    _app = Flask(__name__, static_folder='../static', template_folder='../templates')
    _app.register_blueprint(bp)

    with _app.app_context():

        return _app

