
m app.database import SessionLocal
from app.models import exercicse, BodyPart
from sqlalchemy.exc import integrityError

"""
Script initialisant la base de donnée postgresql avec les 45 exos "Bodyweights" de referrence classé par niveaux de difficulté
"""

def seed_exercises():


"""remplissage de la db postgresql avec l'ensembles des exercices séelectionnés;
ps il est possible que seed_exercices soit modifié sous réserves de correspondances entre les exercices selectionnés et leurs correspondances Gifs"""

db = Sessionlocal()

try: 
    print

    exercices_data = [

# ==========================================
# UPPER BODY - NIVEAU 1 (Débutant)
# ==========================================
{
    "name": "Wall Push-ups",
    "Body_part": BodyPart,UPPER,
    "difficulty":1,
    "description":"pompes contre un mur, idéal pour débuter",
    "instructions":"Placez vos mains contre un mur à hauteur d'épaules, écartées de la largeur des épaules. Éloignez vos pieds du mur. Fléchissez les coudes pour rapprocher votre poitrine du mur, puis repoussez. Gardez le corps droit.",
    "reps": 15,
    "duration_seconds": None,
    "points_value": 5,
    "gif_url": None
},
{
                "name": "Knee Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 1,
                "description": "Pompes sur les genoux pour réduire l'intensité",
                "instructions": "En position de pompe, posez vos genoux au sol. Gardez le dos droit des genoux jusqu'à la tête. Fléchissez les coudes en descendant la poitrine vers le sol, puis remontez.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Incline Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 1,
                "description": "Pompes sur surface surélevée (banc, marche)",
                "instructions": "Placez vos mains sur un banc ou une marche. Mettez-vous en position de planche avec les pieds au sol. Descendez en fléchissant les coudes, puis remontez.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Arm Circles",
                "body_part": BodyPart.UPPER,
                "difficulty": 1,
                "description": "Rotation des bras pour échauffement et endurance",
                "instructions": "Debout, bras tendus sur les côtés à hauteur d'épaules. Faites de petits cercles vers l'avant pendant 15 secondes, puis vers l'arrière pendant 15 secondes.",
                "reps": None,
                "duration_seconds": 30,
                "points_value": 5,
                "gif_url": None
            },
            {
                "name": "Shoulder Taps",
                "body_part": BodyPart.UPPER,
                "difficulty": 1,
                "description": "En planche, toucher alternativement les épaules",
                "instructions": "En position de planche haute (bras tendus), touchez votre épaule gauche avec votre main droite, puis votre épaule droite avec votre main gauche. Gardez les hanches stables.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            
            # ==========================================
            # UPPER BODY - NIVEAU 2 (Intermédiaire)
            # ==========================================
            {
                "name": "Standard Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 2,
                "description": "Pompes classiques au sol",
                "instructions": "En position de planche, mains écartées de la largeur des épaules. Descendez en fléchissant les coudes jusqu'à ce que la poitrine touche presque le sol. Remontez en poussant.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Wide Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 2,
                "description": "Pompes mains écartées pour cibler la poitrine",
                "instructions": "Comme les pompes classiques, mais avec les mains écartées plus largement que les épaules. Descendez et remontez en contrôlant le mouvement.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Diamond Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 2,
                "description": "Pompes mains rapprochées en forme de diamant",
                "instructions": "Placez vos mains sous votre poitrine en formant un diamant avec vos pouces et index. Descendez en gardant les coudes près du corps, puis remontez.",
                "reps": 10,
                "duration_seconds": None,
                "points_value": 15,
                "gif_url": None
            },
            {
                "name": "Pike Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 2,
                "description": "Pompes en position pike pour cibler les épaules",
                "instructions": "Mettez-vous en position de V inversé, fesses en l'air. Fléchissez les coudes pour descendre la tête vers le sol, puis remontez. Cible principalement les épaules.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 15,
                "gif_url": None
            },
            {
                "name": "Tricep Dips",
                "body_part": BodyPart.UPPER,
                "difficulty": 2,
                "description": "Dips sur chaise ou banc pour les triceps",
                "instructions": "Asseyez-vous sur le bord d'une chaise, mains à côté des hanches. Glissez vers l'avant et fléchissez les coudes pour descendre, puis remontez en poussant avec les triceps.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            
            # ==========================================
            # UPPER BODY - NIVEAU 3 (Avancé)
            # ==========================================
            {
                "name": "Decline Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 3,
                "description": "Pompes pieds surélevés",
                "instructions": "Placez vos pieds sur une chaise ou un banc, mains au sol. Faites des pompes dans cette position. Plus d'intensité sur les épaules et le haut de la poitrine.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 18,
                "gif_url": None
            },
            {
                "name": "Archer Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 3,
                "description": "Pompes avec poids transféré sur un bras",
                "instructions": "Mains très écartées. Descendez en transférant le poids sur un bras (l'autre reste tendu sur le côté). Remontez et alternez.",
                "reps": 10,
                "duration_seconds": None,
                "points_value": 20,
                "gif_url": None
            },
            {
                "name": "Pseudo Planche Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 3,
                "description": "Pompes avec mains vers l'arrière, corps penché",
                "instructions": "Placez vos mains au niveau de la taille (pas des épaules), doigts pointant vers les pieds. Penchez-vous en avant et faites des pompes. Très exigeant pour les épaules.",
                "reps": 8,
                "duration_seconds": None,
                "points_value": 22,
                "gif_url": None
            },
            {
                "name": "Clapping Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 3,
                "description": "Pompes explosives avec clap des mains",
                "instructions": "Faites une pompe explosive en poussant assez fort pour décoller les mains du sol. Tapez dans vos mains en l'air, puis rattrapez-vous.",
                "reps": 8,
                "duration_seconds": None,
                "points_value": 22,
                "gif_url": None
            },
            {
                "name": "One-arm Push-ups",
                "body_part": BodyPart.UPPER,
                "difficulty": 3,
                "description": "Pompes à un seul bras",
                "instructions": "Un bras dans le dos ou sur le côté. Écartez les jambes pour plus de stabilité. Descendez et remontez sur un seul bras. Extrêmement difficile.",
                "reps": 5,
                "duration_seconds": None,
                "points_value": 30,
                "gif_url": None
            },
            
            # ==========================================
            # CORE - NIVEAU 1 (Débutant)
            # ==========================================
            {
                "name": "Plank 30s",
                "body_part": BodyPart.CORE,
                "difficulty": 1,
                "description": "Gainage statique sur les avant-bras",
                "instructions": "Sur les avant-bras et pointes de pieds, gardez le corps droit comme une planche. Ne laissez pas les hanches tomber. Maintenez 30 secondes.",
                "reps": None,
                "duration_seconds": 30,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Dead Bug",
                "body_part": BodyPart.CORE,
                "difficulty": 1,
                "description": "Mouvement alterné bras-jambes au sol",
                "instructions": "Allongé sur le dos, bras tendus vers le plafond, genoux pliés à 90°. Descendez le bras droit et la jambe gauche en même temps, puis alternez.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Bird Dog",
                "body_part": BodyPart.CORE,
                "difficulty": 1,
                "description": "À quatre pattes, lever bras et jambe opposés",
                "instructions": "À quatre pattes. Tendez le bras droit devant vous et la jambe gauche derrière. Maintenez 2 secondes, revenez, puis alternez.",
                "reps": 10,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Lying Leg Raises",
                "body_part": BodyPart.CORE,
                "difficulty": 1,
                "description": "Lever les jambes allongé sur le dos",
                "instructions": "Allongé sur le dos, mains sous les fesses. Levez les jambes tendues jusqu'à 90°, puis redescendez lentement sans toucher le sol.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Knee Raises",
                "body_part": BodyPart.CORE,
                "difficulty": 1,
                "description": "Lever les genoux vers la poitrine",
                "instructions": "Debout ou suspendu à une barre. Levez les genoux vers la poitrine en contractant les abdos. Redescendez contrôlé.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            
            # ==========================================
            # CORE - NIVEAU 2 (Intermédiaire)
            # ==========================================
            {
                "name": "Crunches",
                "body_part": BodyPart.CORE,
                "difficulty": 2,
                "description": "Crunchs abdominaux classiques",
                "instructions": "Allongé sur le dos, genoux pliés, mains derrière la tête. Contractez les abdos pour lever les épaules du sol. Ne tirez pas sur la nuque.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 10,
                "gif_url": None
            },
            {
                "name": "Bicycle Crunches",
                "body_part": BodyPart.CORE,
                "difficulty": 2,
                "description": "Crunchs en pédalant, coude vers genou opposé",
                "instructions": "Allongé sur le dos, mains derrière la tête. Pédalez en touchant le coude droit au genou gauche, puis alternez. Mouvement contrôlé.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Russian Twists",
                "body_part": BodyPart.CORE,
                "difficulty": 2,
                "description": "Rotation du buste assis, pieds levés",
                "instructions": "Assis, pieds levés, buste légèrement incliné en arrière. Tournez le buste de gauche à droite en touchant le sol de chaque côté avec vos mains.",
                "reps": 30,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Plank 60s",
                "body_part": BodyPart.CORE,
                "difficulty": 2,
                "description": "Gainage 1 minute",
                "instructions": "Même position que le plank 30s, mais maintenez pendant 60 secondes. Concentrez-vous sur la respiration.",
                "reps": None,
                "duration_seconds": 60,
                "points_value": 15,
                "gif_url": None
            },
            {
                "name": "Mountain Climbers",
                "body_part": BodyPart.CORE,
                "difficulty": 2,
                "description": "Genoux vers poitrine en position pompe",
                "instructions": "En position de planche haute, ramenez alternativement et rapidement les genoux vers la poitrine. Gardez les hanches basses.",
                "reps": 30,
                "duration_seconds": None,
                "points_value": 15,
                "gif_url": None
            },
            
            # ==========================================
            # CORE - NIVEAU 3 (Avancé)
            # ==========================================
            {
                "name": "V-ups",
                "body_part": BodyPart.CORE,
                "difficulty": 3,
                "description": "Lever simultanément bras et jambes en V",
                "instructions": "Allongé sur le dos, bras tendus au-dessus de la tête. Levez simultanément les jambes et le haut du corps pour toucher vos pieds en formant un V.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 18,
                "gif_url": None
            },
            {
                "name": "Dragon Flags",
                "body_part": BodyPart.CORE,
                "difficulty": 3,
                "description": "Lever le corps entier à l'horizontal",
                "instructions": "Allongé sur un banc, agrippez le banc derrière votre tête. Levez tout votre corps (sauf les épaules) à l'horizontal, puis redescendez contrôlé. Extrêmement difficile.",
                "reps": 8,
                "duration_seconds": None,
                "points_value": 25,
                "gif_url": None
            },
            {
                "name": "Hanging Leg Raises",
                "body_part": BodyPart.CORE,
                "difficulty": 3,
                "description": "Lever les jambes suspendu à une barre",
                "instructions": "Suspendu à une barre de traction, levez les jambes tendues jusqu'à l'horizontal ou plus haut. Redescendez contrôlé sans balancer.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 20,
                "gif_url": None
            },
            {
                "name": "L-sit",
                "body_part": BodyPart.CORE,
                "difficulty": 3,
                "description": "Position assise en l'air, jambes tendues",
                "instructions": "Assis au sol, mains à plat à côté des hanches. Poussez pour soulever tout le corps, jambes tendues devant vous en L. Maintenez.",
                "reps": None,
                "duration_seconds": 20,
                "points_value": 22,
                "gif_url": None
            },
            {
                "name": "Plank to Push-up",
                "body_part": BodyPart.CORE,
                "difficulty": 3,
                "description": "Passer de gainage avant-bras à pompe",
                "instructions": "Commencez en planche sur avant-bras. Passez en position de pompe (bras tendus) un bras à la fois, puis revenez sur les avant-bras. Alternez le bras qui monte en premier.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 18,
                "gif_url": None
            },
            
            # ==========================================
            # LOWER BODY - NIVEAU 1 (Débutant)
            # ==========================================
            {
                "name": "Bodyweight Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 1,
                "description": "Squats classiques au poids du corps",
                "instructions": "Pieds écartés largeur d'épaules. Descendez en fléchissant les genoux et en reculant les fesses, comme pour vous asseoir. Gardez le dos droit. Remontez.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Wall Sit 30s",
                "body_part": BodyPart.LOWER,
                "difficulty": 1,
                "description": "Position assise contre un mur",
                "instructions": "Dos contre un mur, descendez en position assise (cuisses parallèles au sol). Maintenez cette position 30 secondes.",
                "reps": None,
                "duration_seconds": 30,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Calf Raises",
                "body_part": BodyPart.LOWER,
                "difficulty": 1,
                "description": "Lever sur la pointe des pieds",
                "instructions": "Debout, pieds écartés largeur de hanches. Levez-vous sur la pointe des pieds le plus haut possible, puis redescendez lentement.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 5,
                "gif_url": None
            },
            {
                "name": "Glute Bridges",
                "body_part": BodyPart.LOWER,
                "difficulty": 1,
                "description": "Lever les hanches allongé sur le dos",
                "instructions": "Allongé sur le dos, genoux pliés, pieds au sol. Levez les hanches en contractant les fessiers jusqu'à former une ligne droite des épaules aux genoux. Redescendez.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            {
                "name": "Step-ups",
                "body_part": BodyPart.LOWER,
                "difficulty": 1,
                "description": "Monter alternativement sur une chaise ou marche",
                "instructions": "Face à une chaise ou marche, montez en plaçant un pied complet sur la surface, poussez pour monter l'autre pied. Redescendez et alternez.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 8,
                "gif_url": None
            },
            
            # ==========================================
            # LOWER BODY - NIVEAU 2 (Intermédiaire)
            # ==========================================
            {
                "name": "Jump Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 2,
                "description": "Squats explosifs avec saut",
                "instructions": "Faites un squat classique, puis explosez vers le haut en sautant le plus haut possible. Atterrissez en douceur et enchaînez.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 15,
                "gif_url": None
            },
            {
                "name": "Lunges",
                "body_part": BodyPart.LOWER,
                "difficulty": 2,
                "description": "Fentes avant alternées",
                "instructions": "Debout, faites un grand pas en avant. Descendez en fléchissant les deux genoux (genou arrière vers le sol). Remontez et alternez les jambes.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Bulgarian Split Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 2,
                "description": "Fentes avec pied arrière surélevé",
                "instructions": "Placez un pied arrière sur une chaise ou banc. Descendez en squat sur la jambe avant. Plus intense que les fentes classiques.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 15,
                "gif_url": None
            },
            {
                "name": "Sumo Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 2,
                "description": "Squats jambes très écartées",
                "instructions": "Pieds très écartés, pointes tournées vers l'extérieur. Descendez en squat, genoux suivant la direction des pieds. Cible les adducteurs.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 12,
                "gif_url": None
            },
            {
                "name": "Wall Sit 60s",
                "body_part": BodyPart.LOWER,
                "difficulty": 2,
                "description": "Position assise contre mur 1 minute",
                "instructions": "Même que Wall Sit 30s, mais maintenez pendant 60 secondes. Brûlure garantie dans les cuisses !",
                "reps": None,
                "duration_seconds": 60,
                "points_value": 15,
                "gif_url": None
            },
            
            # ==========================================
            # LOWER BODY - NIVEAU 3 (Avancé)
            # ==========================================
            {
                "name": "Pistol Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 3,
                "description": "Squats sur une seule jambe",
                "instructions": "Debout sur une jambe, l'autre tendue devant vous. Descendez en squat sur la jambe d'appui en gardant l'autre jambe tendue. Très difficile, nécessite force et équilibre.",
                "reps": 8,
                "duration_seconds": None,
                "points_value": 25,
                "gif_url": None
            },
            {
                "name": "Jump Lunges",
                "body_part": BodyPart.LOWER,
                "difficulty": 3,
                "description": "Fentes alternées avec saut explosif",
                "instructions": "En position de fente, sautez explosif et changez de jambe en l'air. Atterrissez en position de fente avec l'autre jambe devant. Enchaînez rapidement.",
                "reps": 20,
                "duration_seconds": None,
                "points_value": 20,
                "gif_url": None
            },
            {
                "name": "Single-leg Deadlifts",
                "body_part": BodyPart.LOWER,
                "difficulty": 3,
                "description": "Deadlift sur une jambe",
                "instructions": "Debout sur une jambe. Penchez-vous en avant en tendant l'autre jambe derrière vous, buste parallèle au sol. Revenez debout. Équilibre et force requis.",
                "reps": 12,
                "duration_seconds": None,
                "points_value": 18,
                "gif_url": None
            },
            {
                "name": "Shrimp Squats",
                "body_part": BodyPart.LOWER,
                "difficulty": 3,
                "description": "Squat sur une jambe, genou arrière au sol",
                "instructions": "Debout sur une jambe, tenez l'autre pied derrière vous. Descendez en squat jusqu'à poser le genou arrière au sol. Remontez. Variante du pistol squat.",
                "reps": 8,
                "duration_seconds": None,
                "points_value": 22,
                "gif_url": None
            },
            {
                "name": "Box Jumps",
                "body_part": BodyPart.LOWER,
                "difficulty": 3,
                "description": "Sauts explosifs sur surface surélevée",
                "instructions": "Face à une box ou chaise stable. Sautez explosif pour atterrir dessus avec les deux pieds. Redescendez et répétez. Plyométrique intense.",
                "reps": 15,
                "duration_seconds": None,
                "points_value": 20,
                "gif_url": None
            },
        ]
        
        # Insérer les exercices
        added_count = 0
        skipped_count = 0
        
        for exercise_data in exercises_data:
            existing = db.query(Exercise).filter(
                Exercise.name == exercise_data["name"]
            ).first()
            
            if existing:
                skipped_count += 1
                print(f"⏭️  {exercise_data['name']} existe déjà")
            else:
                exercise = Exercise(**exercise_data)
                db.add(exercise)
                added_count += 1
                print(f"✅ {exercise_data['name']}")
        
        db.commit()
        
        print(f"\n🎉 Seeding terminé !")
        print(f"   ✅ {added_count} exercices ajoutés")
        print(f"   ⏭️  {skipped_count} exercices existaient déjà")
        print(f"   📊 Total en base : {db.query(Exercise).count()} exercices")
        
        # Statistiques
        print(f"\n📊 Répartition :")
        for body_part in BodyPart:
            for diff in [1, 2, 3]:
                count = db.query(Exercise).filter(
                    Exercise.body_part == body_part,
                    Exercise.difficulty == diff
                ).count()
                print(f"   {body_part.value.upper()} - Niveau {diff} : {count} exercices")
        
    except IntegrityError as e:
        print(f"❌ Erreur d'intégrité : {e}")
        db.rollback()
    except Exception as e:
        print(f"❌ Erreur : {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    seed_exercises()