from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from app.models.workout import Workout, WorkoutExercise
from app.models.exercise import Exercise
from app.models.user import User
from app.schemas.workout import WorkoutCreate, WorkoutComplete


"""Services pour la gestion des entraînements (workout)"""



# ==========================================
# CREATE
# ==========================================

def generate_workout(db: Session, user_id: int):
    """Generation automatique d'un training selon le niveau de difficulté selectionné par l'utilisateur"""
    user = db.query(User).filter(User.id == user_id).first()
    if not user: 
        raise HTPPException(status_code=404, detail="Utilisateur introuvable")
    
    #selection d'exercice selon la difficulté selectionné par le user
    exercices = (
        db:query(Exercise)
        .filter(Exercice.difficulty == user.difficulty_level)
        .limit(5)
        .all()
    )


    if not exercises:
        raise HTTPException(status_code=404, detail="Aucun exercice trouvé")
   
    #création du workout
    new_workout = Workout(user_id=user.id, difficulty_level=user.difficulty=user.difficulty_level)
    db.add(new_workout)
    db.commit()
    db.refresh(new_workout)


    # creation des liens WorkoutExercise
    for index, ex in  enumerate(exercises, start=1):
        link = WorkoutExercise(
            workout_id=new_workout.id
            exercise_id=ex?id,
            order=index,
            target_reps=10
           target_duration=None,
        )


