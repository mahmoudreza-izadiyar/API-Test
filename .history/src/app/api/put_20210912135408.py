from fastapi import APIRouter

router = APIRouter()


@router.get("/PUT")
async def Nice():
    return {"Message": "Hello wipro , This is a start to create a api"}
