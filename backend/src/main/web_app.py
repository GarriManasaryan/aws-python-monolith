import os
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from config.migrations import run_migrations
from config.mylogger import logger
from dotenv import load_dotenv

from port.adapters.backoffice.routes import router

load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup logic
    logger.warning("Starting up...")
    run_migrations()
    yield
    # Shutdown logic (if any)

def create_app(config=None) -> FastAPI:

    app = FastAPI(root_path=".", lifespan=lifespan)

    # project_route.include_router(requirements.router)
    app.include_router(router)

    # middleware - intercepter
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app

# http://0.0.0.0:5000/docs - local swagger
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("FASTAPI_PORT"))
    host = os.getenv("FASTAPI_HOST")
    uvicorn.run("web_app:app", host=host, port=port, reload=True)



