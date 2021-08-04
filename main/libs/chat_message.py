from datetime import datetime

import attr

from main.db import redis


@attr.s(auto_attribs=True)
class ChatMessage:
    username: str
    text: str
    timestamp: str

    @classmethod
    def new(cls, *, username, text):
        return ChatMessage(
            username=username, text=text, timestamp=datetime.utcnow().isoformat()
        )

    @staticmethod
    def get(message_id):
        return redis.hgetall(message_id)

    @staticmethod
    def get_all():
        return [ChatMessage.get(id) for id in redis.lrange("messages", 0, -1)]

    def save(self):
        message_id = f"message:{redis.llen('messages') + 1}"
        redis.hmset(message_id, attr.asdict(self))
        redis.rpush("messages", message_id)
