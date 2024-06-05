import uvicorn
from fastapi import FastAPI

from app.api.v1.endpoints import router

PROJECT_NAME = "Repetit"
API_V1_STR = "/api/v1"


app = FastAPI(
    title=PROJECT_NAME,
    openapi_url=f"{API_V1_STR}/openapi.json",
)

app.include_router(router, prefix=API_V1_STR)