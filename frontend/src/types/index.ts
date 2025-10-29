// Basé sur app/schemas/exercise.py
export interface Exercise {
    id: number;
    name: string;
    description: string;
    body_part: 'UPPER' | 'CORE' | 'LOWER'; // Correspond à l'Enum BodyPart de Patrice
    difficulty: 1 | 2 | 3 | 4 | 5; // Niveau de 1 (facile) à 5 (difficile)
    points: number; // Points attribués pour l'exercice
}

// Représente un exercice spécifique dans un Workout (avec le nombre de répétitions/séries)
// Basé sur app/models.py (WorkoutExercise)
export interface WorkoutExercise {
    id: number;
    exercise: Exercise; // Le détail de l'exercice
    sets: number;
    reps: number;
    duration_seconds: number | null; // Pour les exercices basés sur le temps
}

// Basé sur app/schemas/workout.py (WorkoutResponse)
export interface Workout {
    id: number;
    user_id: number;
    created_at: string;
    is_completed: boolean;
    total_points: number;
    difficulty_level: 1 | 2 | 3 | 4 | 5;
    exercises: WorkoutExercise[]; // La liste des exercices avec sets/reps
}

// Basé sur app/schemas/user.py (UserResponse)
export interface User {
    id: number;
    username: string;
    email: string;
    difficulty_level: 1 | 2 | 3 | 4 | 5;
    total_points: number;
    total_workouts: number;
    clashes_won: number;
    clashes_lost: number;
    clashes_draw: number;
    created_at: string;
}

// Types pour l'API Auth
// Basé sur app/schemas/user.py (Token)
export interface Token {
    access_token: string;
    token_type: string;
}

