"""Test endpoint différent"""

import requests
import json

API_KEY = "45cf9619b4mshde0449aa85bbe2dp195b87jsn9a34b3987943"

# Essayons l'endpoint principal
url = "https://exercisedb.p.rapidapi.com/exercises"

headers = {
    "X-RapidAPI-Key": API_KEY,
    "X-RapidAPI-Host": "exercisedb.p.rapidapi.com"
}

params = {"limit": "100"}  # Demander 100 exercices

print("🔍 Test avec endpoint principal...")

response = requests.get(url, headers=headers, params=params)

print(f"Status: {response.status_code}")
print(f"Nombre d'exercices reçus: {len(response.json())}")

# Filtrer bodyweight
all_exercises = response.json()
bodyweight = [e for e in all_exercises if e.get('equipment') == 'body weight']

print(f"✅ Exercices bodyweight: {len(bodyweight)}")

# Sauvegarder
with open('all_bodyweight.json', 'w') as f:
    json.dump(bodyweight, f, indent=2)

print("\nPremier exercice:")
print(json.dumps(bodyweight[0], indent=2))

print(f"\n💾 Sauvegardé dans 'all_bodyweight.json'")
