import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

# ============================================================
# TEST 1 : Vérifier que le endpoint /api/workouts/generate/{user_id} fonctionne
# ============================================================
def test_generate_workout_success():
    user_id = 14  # ⚠️ à adapter à un user existant dans ta base
    response = client.post(f"/api/workouts/generate/{user_id}")
    assert response.status_code == 200
    data = response.json()

    # Vérifie que le workout contient bien 3 exercices
    assert "exercises" in data
    assert len(data["exercises"]) == 3

    # Vérifie la cohérence du user_id
    assert data["user_id"] == user_id
    assert data["is_completed"] is False

# ============================================================
# TEST 2 : Vérifier qu’un user inexistant renvoie 404
# ============================================================
def test_generate_workout_user_not_found():
    response = client.post("/api/workouts/generate/999999")
    assert response.status_code == 404
