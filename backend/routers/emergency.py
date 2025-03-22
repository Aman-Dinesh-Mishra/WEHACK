from fastapi import APIRouter

router = APIRouter(prefix="/emergency", tags=["Emergency"])

@router.get("/")
def emergency_service():
    return {"message": "Emergency service is active!"}
