"""Script pour explorer l'API ExerciseDB"""

import requests
import json

def explore_exercisedb():
    """Explorer les exercices disponibles"""
    
    # Ta clé API
    API_KEY = "45cf9619b4mshde0449aa85bbe2dp195b87jsn9a34b3987943"
    
    print("🔍 Test 1 : Récupération des exercices bodyweight...")
    
    # URL pour les exercices bodyweight
    url = "https://exercisedb.p.rapidapi.com/exercises/equipment/body%20weight"
    
    headers = {
        "X-RapidAPI-Key": API_KEY,
        "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
    }
    
    try:
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            exercises = response.json()
            
            print(f"✅ {len(exercises)} exercices bodyweight trouvés !\n")
            
            # Afficher les 10 premiers
            print("📋 Premiers exercices :\n")
            for i, exercise in enumerate(exercises[:10], 1):
                print(f"--- Exercice {i} ---")
                print(f"ID: {exercise.get('id')}")
                print(f"Nom: {exercise.get('name')}")
                print(f"Body Part: {exercise.get('bodyPart')}")
                print(f"Target: {exercise.get('target')}")
                print(f"GIF: {exercise.get('gifUrl')}")
                print()
            
            # Sauvegarder tous les exercices
            with open('exercisedb_bodyweight.json', 'w', encoding='utf-8') as f:
                json.dump(exercises, f, indent=2, ensure_ascii=False)
            
            print(f"💾 Tous les {len(exercises)} exercices sauvegardés dans 'exercisedb_bodyweight.json'")
            
            # Statistiques par body part
            print("\n📊 Répartition par body part :")
            body_parts = {}
            for ex in exercises:
                bp = ex.get('bodyPart', 'unknown')
                body_parts[bp] = body_parts.get(bp, 0) + 1
            
            for bp, count in sorted(body_parts.items()):
                print(f"   {bp}: {count} exercices")
            
        else:
            print(f"❌ Erreur {response.status_code}")
            print(f"Message: {response.text}")
    
    except Exception as e:
        print(f"❌ Erreur: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    explore_exercisedb()
