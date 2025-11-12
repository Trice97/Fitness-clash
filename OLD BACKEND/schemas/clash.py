"""Schemas pour les clashes"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional
from app.models import ClashStatus

# ==========================================
# CREATE
# ==========================================


class ClashCreate(BaseModel):
    """Créer un clash"""

    challenged_id: int = Field(..., description="ID de l'utilisateur défié")
    workout_id: int = Field(..., description="ID du workout à réaliser")


# ==========================================
# ACCEPT
# ==========================================


class ClashAccept(BaseModel):
    """Accepter un clash"""

    # Pas de données nécessaires
    pass


# ==========================================
# COMPLETE
# ==========================================


class ClashComplete(BaseModel):
    """Compléter un clash (côté challenged)"""

    challenged_workout_id: int = Field(
        ..., description="ID du workout complété par le challengé"
    )


# ==========================================
# RESPONSE
# ==========================================


class ClashResponse(BaseModel):
    """Réponse API avec un clash"""

    id: int
    challenger_id: int
    challenged_id: int
    workout_id: int
    challenged_workout_id: Optional[int]
    status: ClashStatus
    challenger_completed: bool
    challenged_completed: bool
    winner_id: Optional[int]
    created_at: datetime
    expires_at: datetime
    completed_at: Optional[datetime]

    class Config:
        from_attributes = True
