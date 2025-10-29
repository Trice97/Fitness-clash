"""
Dependencies pour FastAPI
Fonctions utilitaires pour la gestion des sessions DB et l'authentification
"""

from typing import Generator, Optional
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from datetime import datetime, timedelta

from app.database import SessionLocal
from app.models import User

# Configuration JWT
SECRET_KEY = "your-secret-key-change-this-in-production"  # À changer en production !
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_HOURS = 24

# Security scheme pour récupérer le token Bearer
security = HTTPBearer()


def get_db() -> Generator[Session, None, None]:
    """
    Dependency pour obtenir une session de base de données.
    Utilisé dans toutes les routes qui ont besoin d'accéder à la DB.
    
    Usage:
        @app.get("/users")
        def get_users(db: Session = Depends(get_db)):
            return db.query(User).all()
    
    Yields:
        Session: Une session SQLAlchemy
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    """
    Crée un token JWT avec les données fournies.
    
    Args:
        data (dict): Données à encoder dans le token (généralement {"sub": user_id})
        expires_delta (Optional[timedelta]): Durée de validité du token
    
    Returns:
        str: Token JWT encodé
    
    Example:
        token = create_access_token({"sub": str(user.id)})
    """
    to_encode = data.copy()
    
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    
    return encoded_jwt


def decode_access_token(token: str) -> dict:
    """
    Décode un token JWT et retourne les données.
    
    Args:
        token (str): Token JWT à décoder
    
    Returns:
        dict: Données décodées du token
    
    Raises:
        HTTPException: Si le token est invalide ou expiré
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide ou expiré",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
) -> User:
    """
    Dependency pour obtenir l'utilisateur actuellement connecté.
    Extrait le token JWT du header Authorization, le décode, et récupère l'utilisateur.
    
    Usage dans une route protégée:
        @app.get("/me")
        def get_me(current_user: User = Depends(get_current_user)):
            return current_user
    
    Args:
        credentials (HTTPAuthorizationCredentials): Token Bearer du header
        db (Session): Session de base de données
    
    Returns:
        User: L'utilisateur connecté
    
    Raises:
        HTTPException: Si le token est invalide ou si l'utilisateur n'existe pas
    """
    token = credentials.credentials
    
    # Décoder le token
    payload = decode_access_token(token)
    
    # Extraire le user_id du token
    user_id: str = payload.get("sub")
    if user_id is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token invalide : user_id manquant",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Récupérer l'utilisateur de la DB
    user = db.query(User).filter(User.id == int(user_id)).first()
    
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Utilisateur non trouvé",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    return user


def get_current_active_user(current_user: User = Depends(get_current_user)) -> User:
    """
    Dependency optionnelle pour vérifier que l'utilisateur est actif.
    Peut être étendue plus tard si on ajoute un champ 'is_active' au modèle User.
    
    Args:
        current_user (User): Utilisateur récupéré par get_current_user
    
    Returns:
        User: L'utilisateur actif
    
    Raises:
        HTTPException: Si l'utilisateur est désactivé (futur)
    """
    # Pour l'instant, on retourne juste l'utilisateur
    # Plus tard, on peut ajouter : if not current_user.is_active: raise HTTPException(...)
    return current_user