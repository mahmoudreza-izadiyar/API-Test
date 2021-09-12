from fastapi import FastAPI

from app.api import Nice

app = FastAPI()


app.include_router(Nice.router)
