from flask import Flask
from flask_socketio import SocketIO
from main.config import config


def _init_app():
    _app = Flask(__name__)
    _app.config.from_object(config)
    return _app


app = _init_app()


@app.get('/')
def hello():
    return '<h1>hello world</h1>'


socketio = SocketIO(app)
