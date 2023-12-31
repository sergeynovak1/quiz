from fastapi import FastAPI

from src.qa.router import router

app = FastAPI()

app.include_router(router)
