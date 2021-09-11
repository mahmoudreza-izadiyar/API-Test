from fastapi import FastAPI

app = FastAPI()


@app.get("/PUT")
def pong():
    return {"congrat": "HELLO WIPRO"}
