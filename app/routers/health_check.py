from fastapi import APIRouter


router = APIRouter()


@router.get("/health-check")
async def app_check():
    return {"message": "OK"}
