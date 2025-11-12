"""Routes pour les contacts (amis).

Ce module gère l'ajout, l'acceptation et la suppression de contacts.
"""

from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.database import get_db
from app.dependencies import get_current_user
from app.models import Contact, ContactStatus, User
from app.schemas.contact import ContactCreate, ContactResponse

router = APIRouter(prefix="/contacts", tags=["Contacts"])


@router.post("/", response_model=ContactResponse, status_code=status.HTTP_201_CREATED)
def creat_contact_request(
    contact_data: ContactCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Envoyer une demande de contact à un autre utilisateur.

    Args:
        contact_data: Données de la demande de contact (user_id de l'autre utilisateur).
        current_user: Utilisateur actuellement authentifié.
        db : Session de base de données.

    Returns:
        ContactResponse: La demande de contact créée.

    Raises:
        HTTPException: Si la demande de contact existe déjà ou si l'utilisateur n'existe pas.
    """

    # d'abord checker si l'utilisateur à ajouter existe
    contact_user = db.query(User).filter(User.id == contact_data.contact_id).first()
    if not contact_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Utilisateur non trouvé",
        )

    # checker qu'on ne s'ajoute pas soit même
    if current_user.id == contact_data.contact_id:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Tu peux pas t'ajouter toi-même",
        )

    #  # Vérifier qu'une demande n'existe pas déjà
    existing_contact = (
        db.query(Contact)
        .filter(
            (
                (Contact.user_id == current_user.id)
                & (Contact.contact_id == contact_data.contact_id)
            )
            | (
                (Contact.user_id == contact_data.contact_id)
                & (Contact.contact_id == current_user.id)
            )
        )
        .first()
    )

    if existing_contact:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Contact request already exists",
        )

    # creer la demande de contact
    contact = Contact(
        user_id=current_user.id,
        contact_id=contact_data.contact_id,
        status=ContactStatus.PENDING,
    )

    db.add(contact)
    db.commit()
    db.refresh(contact)

    return contact


@router.get("/", response_model=List[ContactResponse])
def get_contacts(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Récupérer tous les contacts (acceptés et en attente).

    Args:
        current_user: Utilisateur authentifié.
        db: Session de base de données.

    Returns:
        List[ContactResponse]: Liste des contacts.
    """
    contacts = (
        db.query(Contact)
        .filter(
            (Contact.user_id == current_user.id)
            | (Contact.contact_id == current_user.id)
        )
        .all()
    )

    return contacts


@router.post("/{contact_id}/accept", response_model=ContactResponse)
def accept_contact(
    contact_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Accepter une demande de contact.

    Args:
        contact_id: ID du contact à accepter.
        current_user: Utilisateur authentifié.
        db: Session de base de données.

    Returns:
        ContactResponse: Le contact accepté.

    Raises:
        HTTPException: Si la demande n'existe pas ou n'est pas en attente.
    """
    contact = (
        db.query(Contact)
        .filter(
            Contact.id == contact_id,
            Contact.contact_id == current_user.id,
            Contact.status == ContactStatus.PENDING,
        )
        .first()
    )

    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact request not found",
        )

    contact.status = ContactStatus.ACCEPTED
    contact.accepted_at = func.now()

    db.commit()
    db.refresh(contact)

    return contact


@router.delete("/{contact_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_contact(
    contact_id: int,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    """Supprimer un contact ou refuser une demande.

    Args:
        contact_id: ID du contact à supprimer.
        current_user: Utilisateur authentifié.
        db: Session de base de données.

    Raises:
        HTTPException: Si le contact n'existe pas.
    """
    contact = (
        db.query(Contact)
        .filter(
            Contact.id == contact_id,
            (
                (Contact.user_id == current_user.id)
                | (Contact.contact_id == current_user.id)
            ),
        )
        .first()
    )

    if not contact:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Contact not found",
        )

    db.delete(contact)
    db.commit()

    return None
