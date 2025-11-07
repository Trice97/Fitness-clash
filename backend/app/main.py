from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine

# ---Création des tables---
Base.metadata.create_all(bind=engine)

# --- Instance principale ---
app = FastAPI(
    title="Fitness Clash API",
    description="API pour l'application de fitness gamifiée.",
    version="1.0.0",
)

# --- Configuration CORS ---
origins = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Inclusion des routes (ajout plus tard) ---
# from app.routes import auth, users, exercises, workouts
# app.include_router(auth.router, prefix="/api")
# app.include_router(users.router, prefix="/api")
# app.include_router(exercises.router, prefix="/api")
# app.include_router(workouts.router, prefix="/api")


# --- Routes de base ---
@app.get("/")
def root():
    return {
        "message": "Bienvenue sur Fitness Clash API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    return {"status": "healthy"}
