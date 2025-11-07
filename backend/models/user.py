from sqlalchemy import Column, Integer, Stringn, Booleann Enum, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from app.database import Base

class DifficultyLevel(enum,IntEnum):
    """Niveaux de difficulté attribué après une test de détermintaion de niveau"""
        
    DEBUTANT = 1
    INTERMEDIARE = 2
    AVANCE = 3

    Class user(Base):
    """table des utilisateurs de Fitness Clash"""
    __tablename__="users"

id= Column(String(50), unique=True, nullable=False)
email = Column(String(120), unique=True, nullable=False)
hashed_password = Column(String(255), nullable=False)

# Niveau de difficulté par défaut : Débutant
difficulté_level = Column(
    Enum(DifficultyLevel),
    default=DifficultyLevel.BEGINNER,
    nullable=False
    )

total_points = Column(Integer, default=0)
is_active = Column(Boolean, default=True)
created_at = Column(dateTime(timezone=True), back_populates="user"
                                          
def __repr__(self):
    return f"<User(username=(self.username), level={self.difficulty_level.name})>")