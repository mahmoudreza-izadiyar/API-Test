from fastapi import FastAPI

from app.api import PUT

app = FastAPI()


app.include_router(PUT.router)
