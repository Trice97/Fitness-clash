"""Application principale FastAPI.

Point d'entrée de l'API Fitness Clash.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes import auth, contacts, users, workouts

# Créer l'application
app = FastAPI(
    title="Fitness Clash API",
    description="API pour l'application de fitness gamifiée avec workouts personnalisés",
    version="1.0.0",
)

# Configuration CORS pour le frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # URL du frontend React
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Inclure les routers
app.include_router(auth.router)
app.include_router(users.router)
app.include_router(workouts.router)
app.include_router(contacts.router)


@app.get("/")
def root():
    """Route racine."""
    return {
        "message": "Fitness Clash API",
        "version": "1.0.0",
        "docs": "/docs",
    }


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}
