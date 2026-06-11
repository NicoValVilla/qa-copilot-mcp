from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.infrastructure.web.controllers.qa_controller import router as qa_router
from src.infrastructure.web.controllers.view_controller import router as view_router


def create_app() -> FastAPI:
    app = FastAPI(
        title="QA Copilot MCP",
        description="Demo educativa de MCP con Arquitectura Hexagonal.",
        version="0.1.0",
    )
    app.mount(
        "/static",
        StaticFiles(directory="src/infrastructure/web/static"),
        name="static",
    )
    app.include_router(view_router)
    app.include_router(qa_router)
    return app


app = create_app()
