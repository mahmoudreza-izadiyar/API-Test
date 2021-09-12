from fastapi import FastAPI

from app.api import put

app = FastAPI()


app.include_router(Nice.router)
