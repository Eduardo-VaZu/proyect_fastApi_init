from fastapi import APIRouter, Query, status
from fastapi.params import Depends
from fastapi import HTTPException

from app.models.message_model import Message, CreateMessage, ResponseMessage
from app.services.message_service import MessageService
from app.dependecies.message_dependice import get_message_service

from typing import List, Optional

MESSAGE_NOT_FOUND = "Message not found"

router = APIRouter(tags=["Messages"], prefix="/messages")


@router.get("/health")
def health_check():
    return {
        "status": "success",
        "health_check": "Bienvenido a la API Profesional",
        "swagger": "http://127.0.0.1:8000/docs",
        "redoc": "http://127.0.0.1:8000/redoc",
    }


@router.get("/", response_model=List[ResponseMessage])
def get_all_messages(service: MessageService = Depends(get_message_service)):
    messages = service.get_all_messages()
    if messages is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return messages


@router.get("/{message_id}", response_model=Optional[ResponseMessage])
def get_message_by_id(
    message_id: int, service: MessageService = Depends(get_message_service)
):
    message = service.get_message_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return message


@router.get("/detail/id", response_model=Optional[ResponseMessage])
def get_message_url_param(
    message_id: int = Query(..., gt=1),
    service: MessageService = Depends(get_message_service),
):
    message = service.get_message_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return message


@router.post("/", response_model=ResponseMessage, status_code=status.HTTP_201_CREATED)
def create_message(
    message: CreateMessage, service: MessageService = Depends(get_message_service)
):
    return service.create_message(message)


@router.put("/{message_id}", response_model=Optional[ResponseMessage])
def update_message(
    message_id: int,
    message: CreateMessage,
    service: MessageService = Depends(get_message_service),
):

    message = service.get_message_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return service.update_message(message_id, message)


@router.delete("/{message_id}", response_model=bool)
def delete_message(
    message_id: int,
    service: MessageService = Depends(get_message_service),
):
    message = service.get_message_by_id(message_id)
    if message is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail=MESSAGE_NOT_FOUND
        )
    return service.delete_message(message_id)
