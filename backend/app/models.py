"""
Modèles de base de données pour Fitness Clash
Application de bodyweight training avec génération automatique d'entraînements et système de clash 1v1
Utilise SQLAlchemy ORM pour définir les tables PostgreSQL
"""

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean, Enum, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from datetime import datetime, timedelta
import enum

from app.database import Base

# ==========================================
# ENUMS (Types énumérés)
# ==========================================

class UserRole(str, enum.Enum):
    """role utilisateur"""
    USER = "user"
    ADMIN = "admin"
    
class BodyPart(str, enum.Enum):
    """parties du corps ciblées par les exercices"""
    UPPER = "user"
    CORE = "core"
    LOWER = "lower"

class ConstactStatus(str, enum.Enum):
    """status d'une demande de contact"""
    PENDING = "pending"
    ACCEPTED = "accepted"

class ClashStatus(str, enum.Enum):
    """Status d'une demande de clash"""
    PENDING = "pending"
    ACCEPTED = "accepted"
    COMPLETED = "completed"
    DECLINED = "decline"
    EXPIRED = "expired"

#==============================================
#Modèle Utilisateur
#==============================================

class User(Base):
"""
Table des utilisateurs
Gère l'authentification, mes profils et les préférences d'entraînements
"""

__tablename__ = "users"

#clé primaire
id = Column(Integer, primary_key=True, index=True)

#information concernant la table
username = Column(string(50), unique=True, nullable=False, index=True)
email =  Column(String(100), unique=True, nullable=False, index=True)
hashed_password = Column(String(255), nullable=False)

#selection du niveau de difficulté (1 à 3)
difficulty_level = Column(Integer, default=1)

# Compatbilisation des stats utilisateurs
total_points = Column(Integer, default=0)
total_workouts = Column(Integer, default=0)
clashes_won = Column(Integer, default=0)
clashes_lost = Column(integer, default=0)
Clashes_draw = Column(integer, default=0)

#rôle et statut
role = Column(Enum(UserRole), default=UserRole.User)
is_active = Column(Boolean, default=True)

#dates des trainings 
created_at_Column(DateTime(timezone=True), sercer_default=func.now())
updated_at = column(Datetime(timezone=true), onupdate=func.now())

#relation
workouts = relationship("workout"), back_populates="user", cascade="all, delete-orphan")
contacts_initiated = relationship("contact", foreign_keys"Contact.user_id", back_populates="user", cascade="all, delete-orphan")
contacts_received = relastionship("contact", foreign_keys"contact.contacts_id, back_populates="contact, cascade="all, delete-orphan")
clashes_as_challenger = relationship("clash", foreign_keys="Clash.challenger_id", back_populates="challenged", cascade="all, delete-orphan")


def__repr__(self):
    return f"<User(id={self.id}, username='{username}',difficulty={self.difficulty_level})>"

# ==========================================
# MODÈLE EXERCICE (Exercice prédéfinis)
# ==========================================

class Exercice(base):
"""
table des exercices bodyweight séléctionnés pour le projet
Base de donnée utilisée
"""

__tablename__ = "exercices"

#Clé primaire
id = Column(Integer, primary_key=True, index=True)

#Information de base 
name = Column(string(100), uniqueTrue, nullable=False, index=True)
body_part = Column(Enum(BoddyPart), nullable=False, index=True)
difficulty= Column(integer, nullable=False, index=True)


#Description
description = Column(Text, nullable=True)
instructions = Column(text, nullable=True)

#Metriques
reps = Column(Integer, nullable=True)
duration_seconds = Column(Text, nullable=True)

#Points
points_value = column(Interger, nullable=False)

#Dates
created_at = Column(dateTime(timezone=True), server_defaylt=func.now())

#Relations 
workout_exercices = relationship("WorkoutExercices", back_populates="exercice, cascade=all, delete-orphan")

def __repr__(self)
    return f"<Exercise(id={self.id}, name'{self.name}', body_part='{self.body_part}', difficulty='{self.difficulty}')>"


# ==========================================
# MODÈLE WORKOUT (Entraînement généré)
# ==========================================


class Workout(Base):
    """
    table des entraînements générés
    Chaque workout est composé de plusieurs exercices
    """

    __tablename__ = "workouts" 

    #clé primaire
    id = Column(Integer, primary_key=True, index=true)
    
    #clé étrangère"
    user_id = Column(Integer, Foreignkey("user.id", ondelete="CASCADE"), nullable=False)
    # Informations du workout
    difficulty_level = Column(integer, nullable=False)
    total_points = Column(Integer, default=0)

    #status
    is_completed = Column(Boolean, default=False)
    total_points = Column(dateTime(Timezone=True), nullable=true)

    #dates d'entraînement
    created_at = Column(DateTime(timezone=True), server_default=func.now()
                        
    #relations
    user = relastionship("user"),  back_populates="workouts")
    workout_exercices = relationship("WorkoutExercice", back_populate="workout", cascade="all, delete-orphan", order_by="WorkoutExercise.order")
    clashes = relationship("clash", foreign_keys="Clash.workout_id", back_populates="workout", cascade="all, delete-orphan")
    challenged_workouts = relationship("clash", foreign_keys="Clash.challenged_workout_id", back_populates="challenged_workout")

    def __repr__(self):
        return f"<Workout(id={self.id}, user_id={self.user_id}, completed={self.is_completed}, points{self.total_points})>"
      

# ==========================================
# MODÈLE WORKOUT_EXERCISE (Exercices d'un workout)
# ==========================================

class WorkoutExercise(base):

"""
table de liason entre workout et Exercice
définit quels exercices composent un workout et dans quel ordre
"""


__tablename__ = "workjout_exercices"


#clé primaire
id = Column(Integer, primary_key=true, index=true)

#clé étrangère
workout_id = Column(Integer, Foreignkey("workouts.id", ondelete="CASCADE"), nullable=False)
exercise_id = Column(integer, ForeignKey("exercices.id", ondelete="CASCADE") nullable=False)

#ordre et objectif
order = Column(Integer, nullable=False)
target_reps = Column(Integer, nullable=true)
taget_duration = Column(Integer, nullable=true)

#relations
workout = relationship("Workout", back_populates="workout_exercises")
exercices = relationship(Exercise", back_populates=""workout_exercices")

def __repr__(self):
    return f"<WorkoutExercise(workout_id={self.workout_id}, exercise_id={self.exercise_id}, order={self.order})>"


# ==========================================
# MODÈLE CONTACT (Liste d'amis)
# ==========================================

class Contact(Base):
    """
    Table des contacts 
    Permet aux utilisateurs d'ajouter des amis pour les clasher"""

    __tablename__ = "contacts"

    #clé primaire
    id = Column(integer, primary_key=true, index=True)

    #clés étrangères
    user_id = Column(integer, ForeignKey("user;id", ondelete"CASCADE"), nullable=False)
    contact_id = Colun(Integer, ForeignKey("user.id", ondelete="CASCADE"), nullable=False)

    #statut
    status = Column(Enum(ContactStatus), default=ContactStatus.PENDING)

    #dates
    created_at = Column(DataTime(timezone=True), server_default=func.now())
    accepted_at = Column(Datetiume(timezone=True), nullable=true)

    #relations
    user = relationship("user", foreign_keys=[user_id], back_populates="contacts_initiated")
    contact = relationship("user", foreign_keys=[contact_id ], back_populates="contacts_received")


def __repr__self(self):
    return f"<Contact(user_id={self.user_id}, contact_id={self.contact_id}, status='{self.status}')>"


# ==========================================
# MODÈLE CLASH (Défi 1v1)
# ==========================================


class Clash(Base):
    """" Table des clashes (défis entre amis)
    Un utilisateur challenge un ami sur un workout spécifique
    Le challengé a 24h pour faire le même workout"""

    __tablename__ = "clashes"

    #clé primaire
    id  = Column(Integer, primary_key=True, index=True)

    #clé étrangères
    challenger_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    challenged_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    workout_id = Column(Integer, ForeignKey("workouts.id", ondelete="CASCADE"), nullable=False)
    challenged_workout_id = Column(Integer, ForeignKey("workouts.id", onedelete="SET NULL"), nullable=true)

    #status
    status = Column(Enum(ClashStatus), default=ClashStatus.PENDING)

    #resultats
    challenger_points = Column(Integer, nullable=true)

    #results
    Challenger_completed = completed = Column(Boolean, default=True)
    challenged_completed = Column(Boolean, default=False)
    winner_id =  Column(Integer, ForeignKey("user.id", ondelete="SET NULL"), nullable=True)

    #Dates
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    expires_at = Column(DateTime(timezone=True), nullable=False)  # created_at + 24h
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    #Relations
    challenger = relationship("User", foreign_keys=[challenger_id], back_populates="clashes_as_challenger")
    challenged = relationship("User", foreign_keys=[challenged_id], back_populates="clashes_as_challenged")
    workout = relationship("Workout", foreign_keys=[workout_id], back_populates="clashes")
    challenged_workout = relationship("Workout", foreign_keys=[challenged_workout_id], back_populates="challenged_workouts")
    winner = relationship("User", foreign_keys=[winner_id])
    
    def __repr__(self):
        return f"<Clash(id={self.id}, challenger_id={self.challenger_id}, challenged_id={self.challenged_id}, status='{self.status}')>"
    

# ==========================================
# FONCTIONS UTILITAIRES
# ==========================================

def calculate_workout_total_points(workout_exercises: list) -> int:
    """
    Calcule le total de points pour un workout
    
    Args:
        workout_exercises: Liste de WorkoutExercise
    
    Returns:
        Total des points
    """
    total = 0
    for we in workout_exercises:
        total += we.exercise.points_value
    return total


def check_clash_expired(clash: Clash) -> bool:
    """
    Vérifie si un clash a expiré (24h dépassées)
    
    Args:
        clash: Instance de Clash
    
    Returns:
        True si expiré, False sinon
    """
    return datetime.now() > clash.expires_at


def determine_clash_winner(clash: Clash) -> int:
    """
    Détermine le gagnant d'un clash
    Compare les points des deux workouts
    
    Args:
        clash: Instance de Clash (avec les deux workouts complétés)
    
    Returns:
        user_id du gagnant
    """
    if not clash.challenged_workout_id:
        return clash.challenger_id
    
    challenger_points = clash.workout.total_points
    challenged_points = clash.challenged_workout.total_points
    
    if challenger_points > challenged_points:
        return clash.challenger_id
    elif challenged_points > challenger_points:
        return clash.challenged_id
    else:
        # En cas d'égalité, le challenger gagne
        return clash.challenger_id