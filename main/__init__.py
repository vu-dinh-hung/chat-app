from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from main.config import config


def _init_app():
    _app = Flask(__name__)
    _app.config.from_object(config)
    return _app


app = _init_app()


@app.get('/')
def index():
    return render_template('index.html')


socketio = SocketIO(app)


@socketio.event
def user_message(message):
    emit('broadcast_message', message, broadcast=True, include_self=False)
