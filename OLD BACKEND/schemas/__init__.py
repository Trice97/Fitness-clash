"""
Export tous les schemas pour faciliter les imports
"""

from .user import UserCreate, UserUpdate, UserResponse, UserLogin, Token, TokenData

from .exercise import ExerciseCreate, ExerciseResponse

from .workout import (
    WorkoutCreate,
    WorkoutComplete,
    WorkoutResponse,
    WorkoutExerciseResponse,
)

from .contact import ContactCreate, ContactResponse

from .clash import ClashCreate, ClashAccept, ClashComplete, ClashResponse

__all__ = [
    # User
    "UserCreate",
    "UserUpdate",
    "UserResponse",
    "UserLogin",
    "Token",
    "TokenData",
    # Exercise
    "ExerciseCreate",
    "ExerciseResponse",
    # Workout
    "WorkoutCreate",
    "WorkoutComplete",
    "WorkoutResponse",
    "WorkoutExerciseResponse",
    # Contact
    "ContactCreate",
    "ContactResponse",
    # Clash
    "ClashCreate",
    "ClashAccept",
    "ClashComplete",
    "ClashResponse",
]
