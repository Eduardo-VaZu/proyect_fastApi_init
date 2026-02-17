from app.services.message_service import MessageService
from app.models.message_model import Message, CreateMessage
from typing import List, Optional


class MessageServiceImpl(MessageService):

    def __init__(self):
        self._messages: List[Message] = [
            Message(
                id=1,
                message=" Hola Mundo desde Python con FastAPI",
                author_email="vargas@gamil.com",
                priority=1,
            ),
            Message(
                id=2,
                message=" Seccion de fastapi profesional",
                author_email=None,
                priority=5,
            ),
            Message(
                id=3,
                message=" Ejemplo de mensaje de prueba",
                author_email="correo@gmail.com",
                priority=2,
            ),
        ]

        self._next_id = 4

    def get_all_messages(self) -> List[Message]:
        return self._messages

    def get_message_by_id(self, message_id: int) -> Optional[Message]:
        return next(
            (msg for msg in self._messages if msg.id == message_id),
            None,
        )

    def create_message(self, message: CreateMessage) -> Message:
        new_message = Message(
            id=self._next_id,
            message=message.message,
            author_email=message.author_email,
            priority=message.priority,
        )
        self._messages.append(new_message)
        self._next_id += 1
        return new_message

    def update_message(
        self, message_id: int, message: CreateMessage
    ) -> Optional[Message]:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                update = Message(
                    id=message_id,
                    message=message.message,
                    author_email=message.author_email,
                    priority=message.priority,
                )
                self._messages[index] = update
                return update
        return None

    def delete_message(self, message_id: int) -> bool:
        for index, msg in enumerate(self._messages):
            if msg.id == message_id:
                del self._messages[index]
                return True
        return False
