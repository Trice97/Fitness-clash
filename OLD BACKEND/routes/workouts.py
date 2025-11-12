"""Routes pour les workouts.

Ce module gère la génération, la complétion et la récupération
des entraînements.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user
from app.models import User
from app.schemas.workout import WorkoutCreate, WorkoutResponse
from app.services import workout_service

router = APIRouter(prefix="/workouts", tags=["Workouts"])


@router.post(
    "/generate", response_model=WorkoutResponse, status_code=status.HTTP_201_CREATED
)
def generate_workout_endpoint(
    workout_data: WorkoutCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Générer un nouvel entraînement personnalisé pour l'utilisateur actuel.

    Args:
        workout_data: Données pour générer l'entraînement (objectifs, préférences).
        current_user: Utilisateur actuellement authentifié.
        db : Session de base de données.

    Returns:
        WorkoutResponse: L'entraînement généré.

    Raises:
        HTTPException: Si la génération de l'entraînement échoue.
    """
    try:
        workout = workout_service.generate_workout(workout_data, current_user, db)
        return workout
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )


@router.post("/{workout_id}/complete", response_model=WorkoutResponse)
def complete_workout_endpoint(
    workout_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Marquer un workout comme terminé.

    Args:
    workout_id: ID du workout à compléter.
    current_user: Utilisateur authentifié.
    db: Session de base de données.

    Returns:
    WorkoutResponse: Le workout marqué comme terminé.

    Raises:
    HTTPException Si le workout n'existe pas ou est déjà complété.
    """
    try:
        workout = workout_service.complete_workout(workout_id, current_user.id, db)
        return workout
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/", response_model=List[WorkoutResponse])
def get_workout_history(
    limit: int = 10,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Récupérer l'historique des workouts.

    Args:
        limit: Nombre maximum de workouts à retourner (défaut: 10).
        current_user: Utilisateur authentifié.
        db: Session de base de données.

    Returns:
        List[WorkoutResponse]: Liste des workouts du plus récent au plus ancien.
    """
    workouts = workout_service.get_user_workouts(current_user.id, limit, db)
    return workouts
