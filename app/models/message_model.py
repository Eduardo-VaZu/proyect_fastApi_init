from pydantic import BaseModel, Field, EmailStr


class Message(BaseModel):
    id: int
    message: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="El mensaje debe tener al menos 8 caracter",
    )
    author_email: EmailStr | None = Field(
        None, description="El email es optional pero debe de tener formato valido"
    )
    priority: int = Field(
        default=1, ge=1, le=5, description="Prioridad entre 1 (baja) y 5 (alta)"
    )


class CreateMessage(BaseModel):
    message: str = Field(
        ...,
        min_length=8,
        max_length=50,
        description="El mensaje debe tener al menos 8 caracter",
    )
    author_email: EmailStr | None = Field(
        None, description="El email es optional pero debe tener formato valido"
    )
    priority: int = Field(
        default=1, ge=1, le=5, description="Prioridad entre 1 (baja) y 5 (alta)"
    )


class ResponseMessage(BaseModel):
    id: int
    message: str
    author_email: EmailStr | None
    priority: int

    class Config:
        from_attributes = True
