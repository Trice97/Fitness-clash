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
    """parties du corp ciblées par les exercices"""
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

Class USER(Base):
"""
Table des utilisateurs
Gère l'authentification, mes profits et les préférences d'entraînement
"""

__tablename__ = "users"

#clé primaire
id = Column(Integer, primary_key=true, index=True)

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
created_at Column(DateTime(timezone=True), sercer_default=func.now())
updated_at = column(Datetime(timezone=true), onupdate=func.now())

#relation
workouts = relationship("workout"), back_populates="user", cascade="all, delete-orphan")
contacts_initiated = relationship("contact", foreign_keys"Contact.user_id", back_populates="user", cascade="all, delete-orphan")
contacts_received = relastionship("contact", foreign_keys"contact.contacts_id, back_populates="contact, cascade="all, delete-orphan")
clashes_as_challenger = relationship("clash", foreign_keys="Clash.challenger_id", back_populates="challenged", cascade="all, delete-orphan")


def __repr__(self)
    return f"<User(id={self.id}, username='{username}',difficulty={self.difficulty_level})>"

# ==========================================
# MODÈLE EXERCICE (Exercice prédéfinis)
# ==========================================

class Exercice(base):
"""
table des exercices bodyweight séléctionnés pour le projet
Base de donnée utilisée"""

__tablename__ = "exercices"

#Clé primaire
id = Column(Integer, primary_key=True, index=True)

#information de base 
name = Column(string(100), uniqueTrue, nullable=False, index=true)
body_part = Column(Enum(BoddyPart), nullable=false, index=true)
difficulty= Column(integer, nullable=False, index=true)


#description = Column(Text, nullable=true=
instructions = Column(Integer, nullable=True)

#Points
points_value = column, nullable=false)

#dates
created_at = Column(dateTime(timezone=true), server_defaylt=func.now())

#relations 
workout_exercices = relationship("WorkoutExercices", back_populates="exercice, cascade=all, delete-orphan")

def __repr__(self)
    return f"<Exercise(id={self.id}, name'{self.name}', body_part='{self.body_part}', difficulty='{self.difficulty}')>"

# ==========================================
# MODÈLE WORKOUT (Entraînement généré)
# ==========================================

