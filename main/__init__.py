import attr
from flask import Flask, jsonify, render_template
from flask_socketio import SocketIO, emit

from main.config import config
from main.libs.chat_message import ChatMessage


def _init_app():
    _app = Flask(__name__)
    _app.config.from_object(config)
    return _app


app = _init_app()


@app.get("/")
def index():
    return render_template("login.html")


@app.get("/chat")
def chat():
    return render_template("chat.html")


@app.get("/messages")
def get_messages():
    messages = ChatMessage.get_all()
    print(messages)
    return jsonify(messages)


socketio = SocketIO(app)


@socketio.event
def user_message(data):
    chat_message = ChatMessage.new(username=data["username"], text=data["text"])
    chat_message.save()
    emit(
        "broadcast_message",
        attr.asdict(chat_message),
        broadcast=True,
    )
