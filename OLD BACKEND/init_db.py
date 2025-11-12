"""
Initialise la base de données
Lance une fois pour créer toutes les tables
"""

from app.database import engine, Base
from app.models import *

print("🔄 Création des tables...")
Base.metadata.create_all(bind=engine)
print("✅ Toutes les tables créées !")
