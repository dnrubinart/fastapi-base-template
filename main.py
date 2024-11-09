import uvicorn
from fastapi import APIRouter, FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routes import api_router
from core.config import Settings, settings


class App:
    def __init__(
        self, settings: Settings = settings, api_router: APIRouter = api_router
    ):
        self.__app = FastAPI(
            title=settings.PROJECT_NAME,
            docs_url="/docs",
            redoc_url="/redoc",
            openapi_url="/openapi.json",
        )
        self.__setup_middlewares(settings=settings)
        self.__setup_routes(settings=settings, router=api_router)

    def __setup_middlewares(self, settings: Settings):
        self.__app.add_middleware(
            CORSMiddleware,
            allow_origins=settings.CORS_ALLOWED_HOSTS,
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

    def __setup_routes(self, router: APIRouter, settings: Settings):
        self.__app.include_router(router, prefix=settings.API_V1_STR)

    def __call__(self):
        return self.__app


def create_app() -> FastAPI:
    return App(settings=settings, api_router=api_router)()


app = create_app()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
