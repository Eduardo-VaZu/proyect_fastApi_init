from app.services.impl.messageIpml_service import MessageServiceImpl
from app.services.message_service import MessageService
from app.config.db_config import SessionLocal
from functools import lru_cache


@lru_cache()
def get_message_service() -> MessageService:
    return MessageServiceImpl()
