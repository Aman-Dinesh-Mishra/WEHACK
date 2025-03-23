from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models import EmergencyContact
from backend.schemas import EmergencyContactCreate, EmergencyContactResponse

router = APIRouter(
    prefix="/emergency",
    tags=["Emergency"]
)

# Add Emergency Contact
@router.post("/", response_model=EmergencyContactResponse)
def add_emergency_contact(contact: EmergencyContactCreate, db: Session = Depends(get_db)):
    new_contact = EmergencyContact(
        user_id=contact.user_id,
        name=contact.name,
        phone=contact.phone
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)

    return new_contact

# Get Emergency Contacts for a User
@router.get("/{user_id}", response_model=list[EmergencyContactResponse])
def get_emergency_contacts(user_id: int, db: Session = Depends(get_db)):
    contacts = db.query(EmergencyContact).filter(EmergencyContact.user_id == user_id).all()
    
    if not contacts:
        raise HTTPException(status_code=404, detail="No emergency contacts found")
    
    return contacts

