"""Service de génération et gestion des workouts.

Ce module fournit les fonctions pour créer, compléter et récupérer
des entraînements personnalisés pour les utilisateurs.
"""

import random
from sqlalchemy.orm import Session
from app.models import Workout, Exercise, WorkoutExercise, BodyPart, User
from typing import List


def generate_workout(user_id: int, difficulty: int, db: Session) -> Workout:
    """
    Génère un entraînement personnalisé pour l'utilisateur ayant sollicité un training
    La fonction genere un entraînement en selectionnant parmi les zones du corps et le niveau de difficulté des entrainements à réalisé par l'user
    """

    upper_exercises = (
        db.query(Exercise)
        .filter(Exercise.body_part == BodyPart.UPPER, Exercise.difficulty == difficulty)
        .all()
    )

    core_exercises = (
        db.query(Exercise)
        .filter(Exercise.body_part == BodyPart.CORE, Exercise.difficulty == difficulty)
        .all()
    )
    lower_exercises = (
        db.query(Exercise)
        .filter(Exercise.body_part == BodyPart.LOWER, Exercise.difficulty == difficulty)
        .all()
    )

    # selection de 5 exercices par zone corporelle
    selected_upper = random.sample(upper_exercises, min(5, len(upper_exercises)))
    selected_core = random.sample(core_exercises, min(5, len(core_exercises)))
    selected_lower = random.sample(lower_exercises, min(5, len(lower_exercises)))

    # fusion des exercises sélèctionnés pour l'entraînement de l'utilisateur
    all_exercises = selected_upper + selected_core + selected_lower
    random.shuffle(all_exercises)

    # creation du training
    workout = Workout(user_id=user_id, difficulty_level=difficulty, total_points=0)

    db.add(workout)
    db.flush()

    total_points = 0

    # Création des workout et calcul des points
    for order, exercise in enumerate(all_exercises, start=1):
        workout_exercise = WorkoutExercise(
            workout_id=workout.id,
            exercise_id=exercise.id,
            order=order,
            target_reps=exercise.reps,
            target_duration=exercise.duration_seconds,
        )
        db.add(workout_exercise)
        total_points += exercise.points_value

    # Mettre à jour les points totaux
    workout.total_points = total_points
    db.commit()
    db.refresh(workout)
    return workout


def complete_workout(workout_id: int, user_id: int, db: Session) -> Workout:
    """Marque un workout comme complété et met à jour les stats utilisateur.

    Args:
        workout_id: ID du workout à compléter.
        user_id: ID de l'utilisateur (pour vérifier la propriété).
        db: Session SQLAlchemy pour accéder à la base de données.

    Returns:
        Workout: Le workout marqué comme complété.

    Raises:
        ValueError: Si le workout n'existe pas, n'appartient pas à l'utilisateur,
            ou est déjà complété.
    """

    # récupération du workout"
    workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id, Workout.user_id == user_id)
        .first()
    )

    if not workout:
        raise ValueError("Workout not found or doesen't belong to the user")
    if workout.is_completed:
        raise ValueError("Workout already completed")

    # Workout completed
    workout.is_completed = True
    # Mise à jour stat utilisateur
    user = db.query(User).filter(User.id == user_id).first()
    user.total_workouts += 1
    user.total_points += workout.total_points

    db.commit()
    db.refresh(workout)
    return workout


def get_user_workouts(user_id: int, limit: int, db: Session) -> List[Workout]:
    """Récupère l'historique des workouts d'un utilisateur.

    Args:
        user_id: ID de l'utilisateur.
        limit: Nombre maximum de workouts à retourner.
        db: Session SQLAlchemy pour accéder à la base de données.

    Returns:
        List[Workout]: Liste des workouts du plus récent au plus ancien.
    """

    return (
        db.query(Workout)
        .filter(Workout.user_id == user_id)
        .order_by(Workout.created_at.desc())
        .limit(limit)
        .all()
    )


def get_workout_by_id(workout_id: int, user_id: int, db: Session) -> Workout:
    """Récupère un workout spécifique avec vérification de propriété.

    Args:
        workout_id: ID du workout à récupérer.
        user_id: ID de l'utilisateur (pour vérifier la propriété).
        db: Session SQLAlchemy pour accéder à la base de données.

    Returns:
        Workout: Le workout demandé avec ses exercices.

    Raises:
        ValueError: Si le workout n'existe pas ou n'appartient pas à l'utilisateur.
    """

    workout = (
        db.query(Workout)
        .filter(Workout.id == workout_id, Workout.user_id == user_id)
        .first()
    )
    if not workout:
        raise ValueError("Workout not found or doesn't belong to user")

    return workout
