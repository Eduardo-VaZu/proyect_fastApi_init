from typing import List, Optional
from abc import ABC, abstractmethod
from app.models.message_model import Message, CreateMessage


class MessageService(ABC):
    @abstractmethod
    def get_all_messages(self) -> List[Message]:
        pass

    @abstractmethod
    def get_message_by_id(self, message_id: int) -> Optional[Message]:
        pass

    @abstractmethod
    def create_message(self, message: CreateMessage) -> Message:
        pass

    @abstractmethod
    def update_message(
        self, message_id: int, message: CreateMessage
    ) -> Optional[Message]:
        pass

    @abstractmethod
    def delete_message(self, message_id: int) -> bool:
        pass
