"""
Script de seed pour peupler la table exercises avec 9 exercices de démo
Usage: python seed_exercises.py
"""

from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.exercise import Exercise, BodyPart
from app.models.workout import Workout, WorkoutExercise
from app.models.user import User

def seed_exercises(db: Session):
    """Peuple la base de données avec 9 exercices de démonstration"""

    exercises_data = [
        # ========== UPPER (Haut du corps) ==========
        {
            "name": "Push ups bodyweight",
            "body_part": BodyPart.UPPER,
            "difficulty": 1,
            "description": "Exercice de pompes classiques au poids du corps pour renforcer les pectoraux, triceps et épaules.",
            "instructions": "1. Position de départ : mains au sol largeur des épaules, corps gainé en planche\n2. Descendez en fléchissant les coudes jusqu'à ce que la poitrine touche presque le sol\n3. Poussez pour revenir en position haute\n4. Gardez le corps aligné du haut à en bas",
            "reps": 15,
            "duration_seconds": None,
            "points_value": 10,
            "gif_url": "/static/gifs/Upper_1_Push-ups-bodyweight.mp4",
        },
        {
            "name": "Diamond Push-up",
            "body_part": BodyPart.UPPER,
            "difficulty": 2,
            "description": "Variante de pompes avec les mains rapprochées en forme de diamant, ciblant davantage les triceps.",
            "instructions": "1. Position de départ : mains rapprochées formant un diamant sous la poitrine\n2. Descendez lentement en gardant les coudes près du corps\n3. Poussez pour remonter\n4. Maintenez le gainage tout au long du mouvement",
            "reps": 12,
            "duration_seconds": None,
            "points_value": 20,
            "gif_url": "/static/gifs/Upper_2_Diamond-Pushup-4k.mp4",
        },
        {
            "name": "Chest Tap Push-up",
            "body_part": BodyPart.UPPER,
            "difficulty": 3,
            "description": "Pompe explosive avec tape de la poitrine en l'air, demandant puissance et coordination.",
            "instructions": "1. Démarrez en position de pompe classique\n2. Poussez explosif pour décoller les mains du sol\n3. Tapez votre poitrine avec une main en l'air\n4. Réceptionnez en douceur et répétez\n5. Alternez la main qui tape",
            "reps": 8,
            "duration_seconds": None,
            "points_value": 30,
            "gif_url": "/static/gifs/Upper_3_Chest-tap-Pushups.mp4",
        },
        # ========== CORE (Abdos/Tronc) ==========
        {
            "name": "Abdominal Crunches",
            "body_part": BodyPart.CORE,
            "difficulty": 1,
            "description": "Crunch abdominal basique pour travailler les abdominaux supérieurs.",
            "instructions": "1. Allongez-vous sur le dos, genoux pliés, pieds au sol\n2. Mains derrière la tête ou sur la poitrine\n3. Contractez les abdos pour soulever les épaules du sol\n4. Redescendez lentement sans reposer complètement\n5. Gardez le bas du dos collé au sol",
            "reps": 20,
            "duration_seconds": None,
            "points_value": 10,
            "gif_url": "/static/gifs/CORE_1_Abdominal-Crunches.mp4",
        },
        {
            "name": "Dead Bug",
            "body_part": BodyPart.CORE,
            "difficulty": 2,
            "description": "Exercice de coordination pour renforcer les abdominaux et la stabilité du tronc.",
            "instructions": "1. Allongé sur le dos, bras tendus vers le plafond, genoux à 90°\n2. Tendez simultanément un bras en arrière et la jambe opposée\n3. Revenez à la position de départ\n4. Alternez de l'autre côté\n5. Gardez le bas du dos plaqué au sol",
            "reps": 16,
            "duration_seconds": None,
            "points_value": 20,
            "gif_url": "/static/gifs/CORE_2_Dead-Bug-4k.mp4",
        },
        {
            "name": "Crunch Frog on Floor",
            "body_part": BodyPart.CORE,
            "difficulty": 3,
            "description": "Mouvement dynamique combinant crunch et rapprochement des genoux pour un travail complet des abdos.",
            "instructions": "1. Assis au sol, jambes tendues devant vous\n2. Ramenez les genoux vers la poitrine tout en contractant les abdos\n3. Tendez à nouveau les jambes sans toucher le sol\n4. Gardez l'équilibre sur les fesses\n5. Mouvement fluide et contrôlé",
            "reps": 15,
            "duration_seconds": None,
            "points_value": 30,
            "gif_url": "/static/gifs/CORE_3_Abdominal-Crunches-Hold.mp4",
        },
        # ========== LOWER (Bas du corps) ==========
        {
            "name": "Jumping Lunge",
            "body_part": BodyPart.LOWER,
            "difficulty": 1,
            "description": "Fente sautée pour travailler les jambes avec un aspect cardio et explosivité.",
            "instructions": "1. Position de fente : jambe avant pliée à 90°, genou arrière près du sol\n2. Sautez en changeant de jambe en l'air\n3. Atterrissez en fente de l'autre côté\n4. Gardez le buste droit et le regard devant\n5. Mouvement dynamique et rythmé",
            "reps": 20,
            "duration_seconds": None,
            "points_value": 10,
            "gif_url": "/static/gifs/LOWER_1_Jumping-Lunge.mp4",
        },
        {
            "name": "Frog Jumps",
            "body_part": BodyPart.LOWER,
            "difficulty": 2,
            "description": "Sauts de grenouille pour développer la puissance des jambes et le cardio.",
            "instructions": "1. Position accroupie, mains au sol entre les jambes\n2. Sautez explosif vers l'avant\n3. Atterrissez en position accroupie\n4. Enchaînez les sauts\n5. Gardez les mains au sol à chaque réception",
            "reps": 15,
            "duration_seconds": None,
            "points_value": 20,
            "gif_url": "/static/gifs/LOWER_2_Frog-Jumps.mp4",
        },
        {
            "name": "Jumping Pistol Squat",
            "body_part": BodyPart.LOWER,
            "difficulty": 3,
            "description": "Squat unijambiste explosif, exercice avancé demandant force, équilibre et puissance.",
            "instructions": "1. Tenez-vous sur une jambe, l'autre tendue devant vous\n2. Descendez en squat sur une jambe\n3. Poussez explosif pour sauter\n4. Atterrissez sur la même jambe en contrôle\n5. Alternez de jambe après chaque série",
            "reps": 6,
            "duration_seconds": None,
            "points_value": 30,
            "gif_url": "/static/gifs/LOWER_3_Jumping-Pistol-Squat.mp4",
        },
    ]

    added_count = 0
    skipped_count = 0

    print("🚀 Démarrage du seed des exercices...\n")

    for ex_data in exercises_data:
        # Vérifier si l'exercice existe déjà
        existing = db.query(Exercise).filter(Exercise.name == ex_data["name"]).first()
        if existing:
            print(f"⏭️  Ignoré: {ex_data['name']} (existe déjà)")
            skipped_count += 1
            continue

        # Créer l'exercice
        exercise = Exercise(**ex_data)
        db.add(exercise)
        print(
            f"✅ Ajouté: {ex_data['name']} (difficulté={ex_data['difficulty']}, points={ex_data['points_value']})"
        )
        added_count += 1

    # Commit tous les exercices
    try:
        db.commit()
        print("\n🎉 Seed terminé avec succès !")
        print(f"   ✅ {added_count} exercices ajoutés")
        print(f"   ⏭️  {skipped_count} exercices ignorés (déjà présents)")
    except Exception as e:
        db.rollback()
        print(f"\n❌ Erreur lors du commit: {e}")
        raise


def main():
    """Fonction principale"""
    db = SessionLocal()
    try:
        seed_exercises(db)
    finally:
        db.close()
        print("\n✅ Connexion DB fermée")


if __name__ == "__main__":
    main()
