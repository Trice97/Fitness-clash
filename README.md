# 🏋️ FITNESS CLASH — Backend API

API REST développée avec **FastAPI** pour gérer un système de fitness gamifié avec génération automatique d'entraînements personnalisés.

---

## 📋 Table des matières

- [Aperçu](#-aperçu)
- [Technologies](#-technologies)
- [Architecture](#-architecture)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Lancement](#-lancement)
- [Tests](#-tests)
- [Documentation API](#-documentation-api)
- [Endpoints](#-endpoints)
- [Modèles de données](#-modèles-de-données)
- [Prochaines étapes](#-prochaines-étapes)

---

## 🎯 Aperçu

**Fitness Clash** est une application de fitness gamifiée qui permet aux utilisateurs de :

- S'inscrire et se connecter avec authentification JWT
- Générer automatiquement des entraînements personnalisés selon leur niveau
- Suivre leur progression avec un système de points
- Gérer une bibliothèque d'exercices ciblés par partie du corps

Le backend fournit une API RESTful complète avec validation des données, gestion de base de données PostgreSQL et tests unitaires.

---

## 🛠 Technologies

| Technologie | Version | Usage |
|------------|---------|-------|
| **Python** | 3.11+ | Langage principal |
| **FastAPI** | 0.115+ | Framework web async |
| **PostgreSQL** | 14+ | Base de données relationnelle |
| **SQLAlchemy** | 2.0+ | ORM |
| **Pydantic** | 2.0+ | Validation de schémas |
| **Pytest** | 8.0+ | Tests unitaires |
| **JWT** | python-jose | Authentification |
| **Bcrypt** | passlib | Hashage de mots de passe |
| **Ruff** | — | Linter Python |

---

## 📁 Architecture

```
backend/
├── app/
│   ├── main.py                 # Point d'entrée FastAPI
│   ├── database.py             # Configuration PostgreSQL
│   ├── models/                 # Modèles SQLAlchemy
│   │   ├── user.py
│   │   ├── exercise.py
│   │   ├── workout.py
│   │   └── workout_exercise.py
│   ├── schemas/                # Schémas Pydantic
│   │   ├── user.py
│   │   ├── exercise.py
│   │   └── workout.py
│   ├── services/               # Logique métier
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   ├── exercise_service.py
│   │   └── workout_service.py
│   ├── routes/                 # Routes API
│   │   ├── auth.py
│   │   ├── users.py
│   │   ├── exercises.py
│   │   └── workouts.py
│   └── dependencies/           # Dépendances (auth, db)
├── tests/
│   └── test_workout.py         # Tests unitaires
├── seed_exercises.py           # Script de seed initial
├── requirements.txt
└── pytest.ini
```

---

## 🚀 Installation

### Prérequis

- Python 3.11+
- PostgreSQL 14+
- pip

### 1. Cloner le repository

```bash
git clone https://github.com/ton-username/fitness-clash.git
cd fitness-clash/backend
```

### 2. Créer un environnement virtuel

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ⚙️ Configuration

### 1. Base de données PostgreSQL

Créer une base de données :

```sql
CREATE DATABASE fitness_clash;
```

### 2. Variables d'environnement

Créer un fichier `.env` à la racine du dossier `backend/` :

```env
DATABASE_URL=postgresql://user:password@localhost:5432/fitness_clash
SECRET_KEY=votre_cle_secrete_jwt_super_longue_et_aleatoire
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

> **Note** : Remplace `user` et `password` par tes identifiants PostgreSQL.

### 3. Initialiser la base de données

```bash
# Créer les tables
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine)"

# Seed des exercices de base
python seed_exercises.py
```

---

## 🏃 Lancement

### Mode développement

```bash
uvicorn app.main:app --reload --port 8000
```

L'API sera accessible sur : **http://localhost:8000**

### Documentation interactive

- **Swagger UI** : http://localhost:8000/docs
- **ReDoc** : http://localhost:8000/redoc

---

## 🧪 Tests

### Lancer tous les tests

```bash
pytest
```

### Lancer avec couverture de code

```bash
pytest --cov=app --cov-report=html
```

### Tests disponibles

| Fichier | Tests |
|---------|-------|
| `test_workout.py` | ✅ Génération de workout<br>✅ User introuvable |

**Résultats attendus** :

```
tests/test_workout.py::test_generate_workout_success PASSED
tests/test_workout.py::test_generate_workout_user_not_found PASSED
======================== 2 passed in 0.52s =========================
```

---

## 📖 Documentation API

### Authentification

Tous les endpoints protégés nécessitent un **Bearer Token JWT** dans le header :

```
Authorization: Bearer <ton_token>
```

---

## 🔗 Endpoints

### 🔐 Authentification (`/api/auth`)

| Méthode | Endpoint | Description | Auth |
|---------|----------|-------------|------|
| `POST` | `/api/auth/login` | Connexion utilisateur | ❌ |
| `GET` | `/api/auth/me` | Profil utilisateur courant | ✅ |

**Exemple de connexion** :

```bash
curl -X POST "http://localhost:8000/api/auth/login" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "username=john&password=secret123"
```

**Réponse** :

```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### 👤 Utilisateurs (`/api/users`)

| Méthode | Endpoint | Description | Auth |
|---------|----------|-------------|------|
| `POST` | `/api/users/` | Créer un utilisateur | ❌ |
| `GET` | `/api/users/{id}` | Récupérer un profil | ✅ |
| `PUT` | `/api/users/{id}` | Mettre à jour un profil | ✅ |
| `DELETE` | `/api/users/{id}` | Supprimer un utilisateur | ✅ |

**Exemple d'inscription** :

```bash
curl -X POST "http://localhost:8000/api/users/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "john_doe",
    "email": "john@example.com",
    "password": "secret123",
    "difficulty_level": "intermediate"
  }'
```

---

### 🏋️ Exercices (`/api/exercises`)

| Méthode | Endpoint | Description | Auth |
|---------|----------|-------------|------|
| `GET` | `/api/exercises/` | Lister tous les exercices | ❌ |
| `GET` | `/api/exercises/{id}` | Récupérer un exercice | ❌ |
| `POST` | `/api/exercises/` | Créer un exercice | ✅ |
| `PUT` | `/api/exercises/{id}` | Modifier un exercice | ✅ |
| `DELETE` | `/api/exercises/{id}` | Supprimer un exercice | ✅ |

**Exemple de récupération** :

```bash
curl -X GET "http://localhost:8000/api/exercises/"
```

**Réponse** :

```json
[
  {
    "id": 1,
    "name": "Push-ups",
    "body_part": "chest",
    "difficulty": "beginner",
    "description": "Classic push-ups for upper body strength",
    "reps": 15,
    "points_value": 10
  }
]
```

---

### 💥 Workouts (`/api/workouts`)

| Méthode | Endpoint | Description | Auth |
|---------|----------|-------------|------|
| `POST` | `/api/workouts/generate/{user_id}` | Générer un entraînement auto | ✅ |
| `GET` | `/api/workouts/{id}` | Récupérer un workout | ✅ |
| `PUT` | `/api/workouts/{id}/complete` | Marquer comme terminé | ✅ |
| `DELETE` | `/api/workouts/{id}` | Supprimer un workout | ✅ |

**Exemple de génération automatique** :

```bash
curl -X POST "http://localhost:8000/api/workouts/generate/14" \
  -H "Authorization: Bearer <token>"
```

**Réponse** :

```json
{
  "id": 42,
  "user_id": 14,
  "difficulty_level": "intermediate",
  "total_points": 0,
  "is_completed": false,
  "exercises": [
    {
      "order": 1,
      "target_reps": 10,
      "target_duration": null,
      "exercise": {
        "id": 5,
        "name": "Squats",
        "body_part": "legs",
        "difficulty": "intermediate",
        "points_value": 15
      }
    },
    {
      "order": 2,
      "target_reps": 10,
      "target_duration": null,
      "exercise": {
        "id": 7,
        "name": "Lunges",
        "body_part": "legs",
        "difficulty": "intermediate",
        "points_value": 15
      }
    },
    {
      "order": 3,
      "target_reps": 10,
      "target_duration": null,
      "exercise": {
        "id": 9,
        "name": "Dumbbell Rows",
        "body_part": "back",
        "difficulty": "intermediate",
        "points_value": 15
      }
    }
  ]
}
```

---

## 🗄️ Modèles de données

### User

| Champ | Type | Description |
|-------|------|-------------|
| `id` | Integer | ID unique |
| `username` | String | Nom d'utilisateur (unique) |
| `email` | String | Email (unique) |
| `hashed_password` | String | Mot de passe hashé (bcrypt) |
| `difficulty_level` | Enum | `beginner`, `intermediate`, `advanced` |
| `total_points` | Integer | Points cumulés |

### Exercise

| Champ | Type | Description |
|-------|------|-------------|
| `id` | Integer | ID unique |
| `name` | String | Nom de l'exercice |
| `body_part` | String | Partie du corps (`chest`, `legs`, `back`, etc.) |
| `difficulty` | Enum | `beginner`, `intermediate`, `advanced` |
| `description` | Text | Description détaillée |
| `reps` | Integer | Nombre de répétitions recommandées |
| `points_value` | Integer | Points gagnés à la complétion |

### Workout

| Champ | Type | Description |
|-------|------|-------------|
| `id` | Integer | ID unique |
| `user_id` | Integer | FK vers User |
| `difficulty_level` | Enum | Niveau de l'entraînement |
| `total_points` | Integer | Points totaux de la séance |
| `is_completed` | Boolean | Statut de complétion |
| `exercises` | Relation | Liste des exercices liés via `WorkoutExercise` |

### WorkoutExercise (table de liaison)

| Champ | Type | Description |
|-------|------|-------------|
| `id` | Integer | ID unique |
| `workout_id` | Integer | FK vers Workout |
| `exercise_id` | Integer | FK vers Exercise |
| `order` | Integer | Position dans la séance |
| `target_reps` | Integer | Répétitions cibles |
| `target_duration` | Integer | Durée (optionnel) |

---

## 🔍 Linting

Pour vérifier la qualité du code :

```bash
ruff check . --fix
```

---

## 🚧 Prochaines étapes

- [ ] Ajouter tests pour `complete_workout` et `delete_workout`
- [ ] Implémenter le calcul automatique des points à la complétion
- [ ] Ajouter un système de leaderboard
- [ ] Intégrer des GIFs d'exercices (API externe)
- [ ] Créer le frontend React/Next.js
- [ ] Déployer sur Railway/Render avec PostgreSQL

---

## 👨‍💻 Auteur

**Ton Nom**  
Formation Développeur Full Stack — Holberton School, La Défense  
Back Office @ BNP Paribas

📧 ton.email@example.com  
🔗 [LinkedIn](https://linkedin.com/in/ton-profil)  
🐙 [GitHub](https://github.com/ton-username)

---

## 📄 Licence

Ce projet est développé dans un cadre pédagogique (Holberton School).

---

## 🙏 Remerciements

- **FastAPI** pour le framework moderne et performant
- **SQLAlchemy** pour l'ORM puissant
- **Holberton School** pour la formation de qualité
