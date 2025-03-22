from fastapi import APIRouter

router = APIRouter(prefix="/location", tags=["Location"])

@router.get("/")
def get_location():
    return {"message": "Location service is working!"}
