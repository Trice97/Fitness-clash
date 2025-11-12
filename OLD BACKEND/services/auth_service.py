from passlib.context import CryptContext
from sqlalchemy.orm import Session
from app.models import User
from app.schemas.user import UserCreate


"""Fichier de création et d'authentification
Création des:authentification des utilisateurs 
gestion du hashing du mot de passe 
"""

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    """
    prends le mot de passe en clair et le HASHE définit les règles de configuration manimale et maximale du password

    Args:
        password: Mot de passe en clair

    returns:
        mot de passe hashé
    """
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    vérifie qu'un mot de passe correspond au hash

    Args:
        plain_password: Mot de passe en clair
        hashed_password: Hash stocké en base

    Returns:
        True si le mot de passe correspond, False sinon
    """
    return pwd_context.verify(plain_password, hashed_password)


def register_user(user_data: UserCreate, db: Session) -> User:
    """
    Crée un nouvel utilisateur

    Args:
        user_data: Données de l'utilisateur (username, email, password)
        db: Session de base de données

    Returns:
        L'utilisateur créé

    Raises:
        ValueError: Si l'username ou l'email existe déjà
    """

    # on vérifie si l'user name existe déjà
    existing_username = (
        db.query(User).filter(User.username == user_data.username).first()
    )
    if existing_username:
        raise ValueError("déso!, l'username existe déjà")

    # vérifier si l'email est déjà
    existing_email = db.query(User).filter(User.email == user_data.email).first()
    if existing_email:
        raise ValueError("déso!, cet email existe déjà")

    # création nouvel utilisateur
    hashed_pw = hash_password(user_data.password)

    new_user = User(
        username=user_data.username,
        email=user_data.email,
        hashed_password=hashed_pw,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


def authenticate_user(email: str, password: str, db: Session) -> User | None:
    """
    Authentifie un utilisateur

    Args:
        email: Email de l'utilisateur
        password: Mot de passe en clair
        db: Session de base de données

    Returns:
        L'utilisateur si authentification réussie, None sinon
    """
    user = db.query(User).filter(User.email == email).first()
    if not user:
        return None

    if not verify_password(password, user.hashed_password):
        return None

    return user
