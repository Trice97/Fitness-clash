from pydantic import BaseModel, EmailStr, field, constr
from typing import optional 
from datetime import datetime

# ==========================================
# BASE
# ==========================================

class userBase(basemodel):
    """Champs communs"""

    username: constr(min_length=3, max_length=50) = Field(
        ...,
        description="Nom d'un joueur",
        examples=["patrice"]
    )
    email: EmailStr = Field(
        ...,
        description="email valide",
        examples=["tricepa@holberton.com"] 
    )

# ==========================================
# CREATE
# ==========================================

class UserCreate(UserBase):
    """"Creation d'un utilisateur"""
    password: constr(min_length=5) = Field(
        ...,
        description="Mot de passe (5 caracteres mini)"
        exemples=["secret123"]
    )
    difficulty_level: int = Field(
        default=1,
        ge=1,
        le=3,
        description="Niveau de difficulté (1-3)"
    )

# ==========================================
# UPDATE
# ==========================================

class UserUpdate(BaseModel):
    """Modification d'un utilisateur"""
    username: Optional[constr(min_length=3, max_length=50)] = None
    email: Optional[EmailStr] = None
    difficulty_level: Optional[int] = Field(default=None, ge=1, le=3)

# ==========================================
# RESPONSE
# ==========================================

class UserResponse(UserBase):
    """Réponse API avec un utilisateur"""
    id: int
    difficulty_level: int
    total_points: int
    total_workouts: int
    clashes_won: int
    clashes_lost: int
    clashes_draw: int
    is_active: bool
    created_at: datetime
    
    class Config:
        from_attributes = True

# ==========================================
# LOGIN
# ==========================================

class UserLogin(BaseModel):
    """Login avec email et password"""
    email: EmailStr
    password: str

class Token(BaseModel):
    """Token JWT de réponse"""
    access_token: str
    token_type: str = "bearer"

class TokenData(BaseModel):
    """Données extraites du token"""
    user_id: int