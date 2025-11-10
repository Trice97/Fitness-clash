from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.exercise import Exercise
from app.schemas.exercise import ExerciseCreate


"""Services pour la gestion des exercises"""


# ==========================================
# CREATE
# ==========================================
def create_exercise(db: Session, exercise_data: ExerciseCreate):
    """fonction pour créer un nouvel exercise"""
    

    existing_exercise = db.query(Exercise).filter(Exercise.name == exercise_data.name).first()
    if not exercise:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Un exercise avec ce nom existe déjà"
        )
    

# ==========================================
# READ
# ==========================================
def get_exercise_by_id(db: Session, exercise_id:int):
    """"Récupère un exercise par ID"""
    exercise = db.query(Exercise).filter(Exercise.id == exercise_id).first()
    if not exercise:
            raise HTTPException(status_code=404, detail="exercise introuvable")
    return exercise



# ==========================================
# UPDATE
# ==========================================

