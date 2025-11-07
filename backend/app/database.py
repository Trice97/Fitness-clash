from sqlalchemy import creat_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os 


# --- Chargement des variable d'environnement  ---
load_dotenv()

# --- Récupration de la variable DATABASE_URL ---
DATABASE_URL = os.getenv("DATABASE_URL")


# --- Création du moteur de connexion à POSTGRESQL ---
engine = create_engine(DATABASE_URL, echo=True, future=True)

# --- Création de la session locale(pour interagir avec la DB) ---
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bing=engine)

# --- Base de classes pour les modeles SQLACLCHEMY ---
Base = declarative_base()