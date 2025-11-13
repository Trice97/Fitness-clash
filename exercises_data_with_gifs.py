# 🎥 DONNÉES D'EXERCICES AVEC GIFs
# À intégrer dans ton seed_exercises.py existant

exercises_data = [
    # ========== BEGINNER ==========
    # CHEST
    {
        "name": "Push-ups",
        "body_part": "chest",
        "difficulty": "beginner",
        "description": "Classic push-ups for upper body strength",
        "reps": 15,
        "points_value": 10,
        "gif_url": "https://v2.exercisedb.io/image/lq4ZXYFBQ8FxRk"
    },
    {
        "name": "Incline Push-ups",
        "body_part": "chest",
        "difficulty": "beginner",
        "description": "Push-ups with hands elevated for easier movement",
        "reps": 12,
        "points_value": 8,
        "gif_url": "https://v2.exercisedb.io/image/EarLbEATZ5Y2wc"
    },
    
    # LEGS
    {
        "name": "Squats",
        "body_part": "legs",
        "difficulty": "beginner",
        "description": "Basic squats for leg strength",
        "reps": 20,
        "points_value": 10,
        "gif_url": "https://v2.exercisedb.io/image/wTkiF-OYh0YbHr"
    },
    {
        "name": "Wall Sit",
        "body_part": "legs",
        "difficulty": "beginner",
        "description": "Static hold against a wall for leg endurance",
        "reps": 30,
        "points_value": 12,
        "gif_url": "https://v2.exercisedb.io/image/eJ2P5HH2pWmJNM"
    },
    
    # ========== INTERMEDIATE ==========
    # CHEST
    {
        "name": "Diamond Push-ups",
        "body_part": "chest",
        "difficulty": "intermediate",
        "description": "Push-ups with hands close together for triceps focus",
        "reps": 12,
        "points_value": 15,
        "gif_url": "https://v2.exercisedb.io/image/vXFoqHnhf1PqjX"
    },
    
    # LEGS
    {
        "name": "Lunges",
        "body_part": "legs",
        "difficulty": "intermediate",
        "description": "Alternating leg lunges for balance and strength",
        "reps": 16,
        "points_value": 15,
        "gif_url": "https://v2.exercisedb.io/image/YP8wV9E58H3Jt9"
    },
    {
        "name": "Jump Squats",
        "body_part": "legs",
        "difficulty": "intermediate",
        "description": "Explosive squat jumps for power",
        "reps": 15,
        "points_value": 18,
        "gif_url": "https://v2.exercisedb.io/image/z7ml2aTqVv2qv2"
    },
    
    # BACK
    {
        "name": "Superman Hold",
        "body_part": "back",
        "difficulty": "intermediate",
        "description": "Lying face down, lift arms and legs simultaneously",
        "reps": 20,
        "points_value": 15,
        "gif_url": "https://v2.exercisedb.io/image/9QBBMY-NXB2ZBW"
    },
    
    # ========== ADVANCED ==========
    # CHEST
    {
        "name": "Decline Push-ups",
        "body_part": "chest",
        "difficulty": "advanced",
        "description": "Push-ups with feet elevated for increased difficulty",
        "reps": 15,
        "points_value": 20,
        "gif_url": "https://v2.exercisedb.io/image/NMTCKs7AqPhqeV"
    },
    
    # LEGS
    {
        "name": "Pistol Squats",
        "body_part": "legs",
        "difficulty": "advanced",
        "description": "Single-leg squats requiring balance and strength",
        "reps": 10,
        "points_value": 25,
        "gif_url": "https://v2.exercisedb.io/image/jRxO3pMvBpNQ2d"
    },
    {
        "name": "Bulgarian Split Squats",
        "body_part": "legs",
        "difficulty": "advanced",
        "description": "Single-leg squats with rear foot elevated",
        "reps": 12,
        "points_value": 22,
        "gif_url": "https://v2.exercisedb.io/image/ZvaVeSkrg6SoFr"
    },
    
    # CORE
    {
        "name": "Dragon Flag",
        "body_part": "core",
        "difficulty": "advanced",
        "description": "Advanced core exercise made famous by Bruce Lee",
        "reps": 8,
        "points_value": 30,
        "gif_url": "https://v2.exercisedb.io/image/ASAyxNSiDcAYSs"
    }
]

# ========================================
# EXEMPLE D'UTILISATION DANS TON SEED
# ========================================

"""
def seed_exercises():
    db = SessionLocal()
    
    # Supprimer les anciens exercices si nécessaire
    db.query(Exercise).delete()
    db.commit()
    
    # Ajouter les nouveaux exercices avec GIFs
    for data in exercises_data:
        exercise = Exercise(**data)
        db.add(exercise)
    
    db.commit()
    print(f"✅ {len(exercises_data)} exercices ajoutés avec GIFs !")
    db.close()

if __name__ == "__main__":
    seed_exercises()
"""
