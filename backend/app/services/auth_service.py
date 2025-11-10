"""Contient la logique de hachage, de vérification des mots de passe et de création de JWT."""

from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from dotenv import load_dotenv
from typing import Optional

from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UserCreate

# --- Chargement des variables d'environnement ---
load_dotenv()
SECRET_KEY = os.getenv("JWT_SECRET_KEY", "cette-cle-secrete-doit-etre-changee")
ALGORITHM = os.getenv("JWT_ALGORITHM", "HS256")
# Convertir en int (si non défini, utilise 45 minutes)
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES") or 45) 

# Contexte pour le hachage des mots de passe (bcrypt est le standard)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# ========================================
# HACHAGE ET VÉRIFICATION
# ========================================
def hash_password(password: str) -> str:
    """Hache un mot de passe clair."""
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    """Vérifie un mot de passe clair contre un hachage."""
    return pwd_context.verify(password, hashed)

# ========================================
# JWT
# ========================================
def create_access_token(data: dict):
    """Crée un jeton d'accès JWT."""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

# ========================================
# LOGIQUE MÉTIER
# ========================================
def register_user(user_data: UserCreate, db: Session) -> User:
    """Enregistre un nouvel utilisateur après vérification."""
    # Vérification d'unicité (par email)
    if db.query(User).filter(User.email == user_data.email).first():
        raise ValueError("Cet email est déjà enregistré.")
        
    # Vérification d'unicité (par nom d'utilisateur)
    if db.query(User).filter(User.username == user_data.username).first():
        raise ValueError("Ce nom d'utilisateur est déjà pris.")
        
    hashed = hash_password(user_data.password)
    
    new_user = User(
        username=user_data.username, 
        email=user_data.email, 
        hashed_password=hashed
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def authenticate_user(email: str, password: str, db: Session) -> Optional[User]:
    """Tente d'authentifier un utilisateur par email et mot de passe."""
    user = db.query(User).filter(User.email == email).first()
    if user and verify_password(password, user.hashed_password):
        return user
    return None

