from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from app.schemas.exercise import ExerciseResponse


# ==========================================
# WORKOUT EXERCISE (exercice dans un workout)
# ==========================================


class WorkoutExerciseResponse(BaseModel):
    """un exercice dans un entrainement"""

    order: int
    exercicse: ExerciseResponse
    target_reps: Optional[int]
    taret_duration: Optional[int]

    class Config:
        from_attributes = True


# ==========================================
# CREATE
# ==========================================


class WorkoutCreate(BaseModel):
    """Générer un nouveau workout"""

    # Pas besoin de paramètres : on génère selon le niveau de l'utilisateur
    pass


# ==========================================
# COMPLETE
# ==========================================


class WorkoutComplete(BaseModel):
    """Valider un workout comme complété"""

    is_completed: bool = True


# ==========================================
# RESPONSE
# ==========================================


class WorkoutResponse(BaseModel):
    """Réponse API avec un workout"""

    id: int
    user_id: int
    difficulty_level: int
    total_points: int
    is_completed: bool
    created_at: datetime
    exercises: List[WorkoutExerciseResponse] = []

    class Config:
        from_attributes = True
