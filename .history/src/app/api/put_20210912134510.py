from fastapi import FastAPI

app = FastAPI()


@app.get("/PUT")
async def Nice():
    return {"Message": "Hello wipro , This is a start to create a api"}
