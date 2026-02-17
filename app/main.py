from fastapi import FastAPI
from app.routes.message_routes import router as message_router

app = FastAPI(
    title="API Profesional",
    description="API para el manejo de mensajes",
    version="1.0.0",
)

app.include_router(message_router, prefix="/api/v1")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
