"""Routes d'authentification.

Ce module gère l'enregistrement, la connexion et la récupérationgrok

des informations utilisateur.
"""

from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from app.dependencies import (
    create_access_token,
    get_db,
    get_current_active_user,
)
from app.schemas.user import Token, UserCreate, UserResponse
from app.services import auth_service
from app.models import User

router = APIRouter(prefix="/auth", tags=["Authentication"])


@router.post(
    "/register", response_model=UserResponse, status_code=status.HTTP_201_CREATED
)
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """Création d'un nouvel utilisateur
    Args:
        user_data: Données de l'utilisateur (username, email, password).
        db : Session de base de données.
    returns:
        UserResponse: l'utilisateur créé.
    raises:
        HTTPException: si l'utilisateur ou l'email n'existe déjà.
    """
    try:
        user = auth_service.register_user(user_data, db)
        return user
    except ValueError as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e),
        )
    except Exception as e:
        # Capture erreur bcrypt (72bytes)
        if "72" in str(e).lower() or "byte" in str(e).lower():
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Le mot de passe est trop long (max 72 caractères).",
            )
        # Autre erreur inattendue
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Erreur lors de la création de l'utilisateur.",
        )


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    """Se connecter et obtenir un token JWT.

    Args:
        form_data: Formulaire OAuth2 (username=email, password).
        db: Session de base de données.

    Returns:
        Token: Token JWT d'accès.

    Raises:
        HTTPException: Si l'email ou le mot de passe est incorrect.
    """
    user = auth_service.authenticate_user(form_data.username, form_data.password, db)

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token = create_access_token(
        data={"sub": user.email}
        return {"access_token": access_token, "token_type": "bearer"}


@router.get("/me", response_model=UserResponse)
def get_current_user_info(current_user: User = Depends(get_current_active_user)):
    """Récupérer les informations de l'utilisateur connecté.

    Args:
        current_user: Utilisateur authentifié via le token JWT.

    Returns:
        UserResponse: Informations de l'utilisateur.
    """
    return current_user
