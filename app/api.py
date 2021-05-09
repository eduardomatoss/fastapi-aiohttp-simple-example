from fastapi import FastAPI

from app.routers import (
    root,
    health_check,
    endpoint
)
from app.common.api_config import startup_aiohttp, shutdown_aiohttp

APP_NAME = "fastapi-aiohttp-simple-example"
APP_DESCRIPTION = "This is an example of a fastapi project with aiohttp"
API_RELEASE_VERSION = "1.0.0"

app = FastAPI(
    title=APP_NAME,
    description=APP_DESCRIPTION,
    version=API_RELEASE_VERSION,
    docs_url="/docs",
    on_startup=[startup_aiohttp],
    on_shutdown=[shutdown_aiohttp],
)

app.include_router(root.router)
app.include_router(health_check.router)
app.include_router(endpoint.router)
