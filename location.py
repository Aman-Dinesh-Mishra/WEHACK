import requests
import os
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models import Location, User
from backend.schemas import LocationCreate, LocationResponse
from backend.routers.auth import get_current_user  

router = APIRouter(
    prefix="/location",
    tags=["Location"]
)

GOOGLE_MAPS_URL = "https://maps.googleapis.com/maps/api/geocode/json"
GOOGLE_MAPS_API_KEY = os.getenv("GOOGLE_MAPS_API_KEY")

def get_address_from_coordinates(lat: float, lng: float) -> str:
    params = {"latlng": f"{lat},{lng}", "key": GOOGLE_MAPS_API_KEY}
    
    try:
        response = requests.get(GOOGLE_MAPS_URL, params=params)
        data = response.json()
        
        if response.status_code != 200 or not data.get("results"):
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Failed to fetch address")
        
        return data["results"][0]["formatted_address"]
    
    except requests.RequestException:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Google Maps API request failed")

@router.post("/", response_model=LocationResponse)
def save_location(
    location: LocationCreate, 
    db: Session = Depends(get_db), 
    current_user: User = Depends(get_current_user)  
):
    address = get_address_from_coordinates(location.latitude, location.longitude)

    new_location = Location(
        user_id=current_user.id,
        latitude=location.latitude,
        longitude=location.longitude,
        address=address
    )
    db.add(new_location)
    db.commit()
    db.refresh(new_location)

    return new_location
