from pydantic import BaseModel, EmailStr, Field, constr
from typing import Optional
from datetime import datetime


# ==========================================
# BASE
# ==========================================


class UserBase(BaseModel):
    """Champs communs"""

    username: constr(min_length=3, max_length=50) = Field(
        ..., description="Nom d'un joueur", examples=["Tricepa"]
    )
    email: EmailStr = Field(
        ..., description="email valide", examples=["tricepa97@holberton.com"]
    )


# ==========================================
# CREATE
# ==========================================


class UserCreate(UserBase):
    """Creation d'un utilisateur"""

    password: constr(min_length=8, max_length=72) = Field(
        ..., description="Mot de passe (8 à 72 caracteres)", examples=["monpass123"]
    )


# ==========================================
# UPDATE
# ==========================================


class UserUpdate(BaseModel):
    """Modification d'un utilisateur"""

    username: Optional[constr(min_length=5, max_length=50)] = None
    email: Optional[EmailStr] = None


# ==========================================
# RESPONSE
# ==========================================


class UserResponse(UserBase):
    """Réponse API avec un utilisateur"""

    id: int
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

    email_id: int
