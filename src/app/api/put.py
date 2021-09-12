from fastapi import APIRouter

router = APIRouter()


@router.get("/PUT")
async def Nice():
    return {"Message": "Hello wipro , woooHooo, this api works. now test PUT request!"}
