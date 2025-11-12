"""Schemas pour les contacts"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models import ContactStatus

# ==========================================
# CREATE
# ==========================================


class ContactCreate(BaseModel):
    """Ajouter un contact"""

    contact_id: int = Field(..., description="ID de l'utilisateur à ajouter")


# ==========================================
# RESPONSE
# ==========================================


class ContactResponse(BaseModel):
    """Réponse API avec un contact"""

    id: int
    user_id: int
    contact_id: int
    status: ContactStatus
    created_at: datetime
    accepted_at: Optional[datetime]

    class Config:
        from_attributes = True
