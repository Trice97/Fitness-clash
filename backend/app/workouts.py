from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.database import Base


class Workout(Base):
    """table des entraînements générés automatiquement"""
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)

    # 🔗 Lien vers l'utilisateur propriétaire du workout
    user_id = Column(Integer, ForeignKey("users.id",ondelete="CASCADE"),nullable=False)

    # Niveau de difficulté du workout (lié au profil de l’utilisateur)
    difficulty_level = Column(Integer, nullable=False)

    # statistiques
    total_points = Column(Integer, default=0)
    is_completed = Column(Boolean, default=False)

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # relations ORM
    user = relationship("User", back_populates="workouts")
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="workout"
        "cascade="all, delete-orphan"
        "order_by="WorkoutExercise.order"
)


def __repr__(self):
    return f"<workout(id={self.id}, user_id={self.user_id}, completed={self.is_completed}, points={self.totalpoints})>"

class WorkoutExercise(Base):
    """Table d'association entre Workout et Exercise"""
    __tablename__ = "workout_exercises"

    id = Column(Integer, primary_key=True, index=True)

    # clés étrangères
    workout_id = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"), nullable=False)
    exercise_id = Column(Integer, ForeignKey("exercises.id", ondelete="CASCADE"), nullable=False)
                                             
    def __repr__(self):
        return f"<WorkoutExercise(workout_id={self.workout_id}, exercise_id={self.exercise_id}, order={self.order})>"