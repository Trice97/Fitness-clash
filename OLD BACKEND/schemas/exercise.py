"""Schemas pour les exercices"""

from pydantic import BaseModel, Field, constr
from typing import Optional
from app.models import BodyPart

# ==========================================
# BASE
# ==========================================


class ExerciseBase(BaseModel):
    """Champs communs"""

    name: constr(min_length=3, max_length=100) = Field(
        ..., description="Nom de l'exercice", examples=["Push-ups"]
    )
    body_part: BodyPart = Field(
        ..., description="Partie du corps (upper/core/lower)", examples=["upper"]
    )
    difficulty: int = Field(
        ..., ge=1, le=3, description="Difficulté (1-3)", examples=[2]
    )


# ==========================================
# CREATE
# ==========================================


class ExerciseCreate(ExerciseBase):
    """Création d'un exercice"""

    description: Optional[str] = Field(
        default=None, max_length=500, description="Description de l'exercice"
    )
    instructions: Optional[str] = Field(
        default=None, max_length=1000, description="Instructions détaillées"
    )
    reps: Optional[int] = Field(default=None, ge=1, description="Nombre de répétitions")
    duration_seconds: Optional[int] = Field(
        default=None, ge=1, description="Durée en secondes"
    )
    points_value: int = Field(
        ..., ge=1, description="Points attribués pour cet exercice"
    )


# ==========================================
# RESPONSE
# ==========================================


class ExerciseResponse(ExerciseBase):
    """Réponse API avec un exercice"""

    id: int
    description: Optional[str]
    instructions: Optional[str]
    reps: Optional[int]
    duration_seconds: Optional[int]
    points_value: int

    class Config:
        from_attributes = True
