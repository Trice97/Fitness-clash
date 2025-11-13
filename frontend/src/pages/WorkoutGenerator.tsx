// src/pages/WorkoutGenerator.tsx

import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext'; // On utilise le contexte mis à jour

// ===========================================
// INTERFACES (Définitions des types de données)
// ===========================================

// Interface pour les exercices inclus dans le workout
interface WorkoutExercise {
    exercise_id: number;
    name: string;
    sets: number;
    reps: string;
}

// Interface pour le Workout généré (basée sur WorkoutResponse de FastAPI)
interface Workout {
    id: number;
    user_id: number;
    title: string;
    created_at: string;
    is_completed: boolean;
    exercises: WorkoutExercise[];
}

const API_BASE_URL = "http://localhost:8000";

const WorkoutGenerator = () => {
    // 1. Récupération des données utilisateur (ID, Token) et des fonctions de contexte
    const { user, token, isAuthenticated, fetchUser } = useAuth(); // fetchUser est crucial pour la mise à jour des points

    const [workout, setWorkout] = useState<Workout | null>(null);
    const [isLoading, setIsLoading] = useState(false); // Pour la génération
    const [isCompleting, setIsCompleting] = useState(false); // Pour la complétion
    const [error, setError] = useState('');

    // ==========================================
    // GÉNÉRATION D'UN WORKOUT (POST)
    // ==========================================
    const handleGenerateWorkout = async () => {
        if (!user || !token) {
            setError("Erreur: Utilisateur non connecté ou ID manquant.");
            return;
        }

        setError('');
        setIsLoading(true);

        const userId = user.id; 
        const API_URL = `${API_BASE_URL}/workouts/generate/${userId}`;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`, // Sécurité
                },
                // Body vide (l'ID est dans l'URL)
            });

            const responseData = await response.json();

            if (response.ok) {
                setWorkout(responseData);
                setError('');
            } else {
                setError(responseData.detail || 'Erreur lors de la génération de l\'entraînement.');
                setWorkout(null);
            }
        } catch (err) {
            console.error("Erreur réseau:", err);
            setError("Impossible de joindre le serveur. Veuillez réessayer.");
        } finally {
            setIsLoading(false);
        }
    };

    // ==========================================
    // MARQUER COMME TERMINÉ (PUT)
    // ==========================================
    const handleCompleteWorkout = async () => {
        if (!workout || !token || workout.is_completed) {
            alert("L'entraînement est déjà terminé ou n'a pas été généré.");
            return;
        }

        setIsCompleting(true);
        setError('');

        const API_URL = `${API_BASE_URL}/workouts/${workout.id}/complete`;

        // Hypothèse pour le corps de la requête WorkoutComplete
        const completionData = {
            is_completed: true,
            points_awarded: 100, // Exemple : à ajuster si Patrice le calcule côté back-end
        };

        try {
            const response = await fetch(API_URL, {
                method: 'PUT',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`, 
                },
                body: JSON.stringify(completionData),
            });

            const updatedWorkout: Workout = await response.json();

            if (response.ok) {
                // Succès : Mettre à jour l'état du workout
                setWorkout(updatedWorkout); 
                alert(`Félicitations ! Entraînement terminé et ${completionData.points_awarded} points gagnés !`);
                
                // CRUCIAL : Mettre à jour le profil utilisateur via le contexte
                // pour que les points totaux se mettent à jour dans le Dashboard.
                fetchUser(token); 
            } else {
                setError(updatedWorkout.detail || "Erreur lors de la mise à jour du statut.");
            }
        } catch (err) {
            console.error("Erreur réseau:", err);
            setError("Impossible de marquer l'entraînement comme terminé.");
        } finally {
            setIsCompleting(false);
        }
    };


    // --- Rendu ---
    
    if (!isAuthenticated) {
        return <div style={containerStyle}><p>Veuillez vous connecter pour générer un entraînement.</p></div>;
    }
    
    return (
        <div style={containerStyle}>
            <h1 style={{color: '#007BFF'}}>Générer un Nouvel Entraînement</h1>
            
            <button 
                onClick={handleGenerateWorkout} 
                disabled={isLoading} 
                style={buttonStyle}
            >
                {isLoading ? 'Génération en cours...' : 'Générer mon Entraînement !'}
            </button>
            
            {error && <p style={{ color: 'red', marginTop: '15px' }}>Erreur: {error}</p>}

            {workout && (
                <div style={workoutCardStyle}>
                    <h2>{workout.title} (ID: {workout.id})</h2>
                    <p>Créé le: {new Date(workout.created_at).toLocaleDateString()}</p>
                    <p>Statut: {workout.is_completed ? '✅ Terminé' : '⏳ En attente'}</p>
                    
                    <h3 style={{marginTop: '20px'}}>Détails des Exercices ({workout.exercises.length})</h3>
                    <ul style={listStyle}>
                        {workout.exercises.map((item, index) => (
                            <li key={item.exercise_id || index} style={listItemStyle}>
                                <strong>{item.name}</strong> : {item.sets} séries de {item.reps}
                            </li>
                        ))}
                    </ul>
                    
                    {/* Bouton de complétion */}
                    <button 
                        style={{...buttonStyle, 
                                backgroundColor: workout.is_completed ? '#6c757d' : '#28a745', 
                                marginTop: '20px'}} 
                        onClick={handleCompleteWorkout}
                        disabled={workout.is_completed || isCompleting}
                    >
                        {isCompleting 
                            ? 'Finalisation...' 
                            : (workout.is_completed 
                                ? '✅ Entraînement Terminé' 
                                : 'Marquer comme Terminé')
                        }
                    </button>
                </div>
            )}
        </div>
    );
};

// Styles pour le composant (inchangés pour la mise à jour)
const containerStyle: React.CSSProperties = {
    padding: '40px', 
    textAlign: 'center', 
    maxWidth: '800px', 
    margin: '30px auto',
    backgroundColor: '#f8f9fa',
    borderRadius: '8px',
    boxShadow: '0 4px 12px rgba(0,0,0,0.1)'
};

const buttonStyle: React.CSSProperties = {
    padding: '12px 25px',
    backgroundColor: '#ffc107',
    color: '#333',
    border: 'none',
    borderRadius: '6px',
    fontSize: '18px',
    cursor: 'pointer',
    marginTop: '20px',
    fontWeight: 'bold'
};

const workoutCardStyle: React.CSSProperties = {
    marginTop: '30px',
    padding: '25px',
    border: '2px solid #007BFF',
    borderRadius: '8px',
    backgroundColor: '#fff',
    textAlign: 'left'
};

const listStyle: React.CSSProperties = {
    listStyleType: 'none',
    padding: 0
};

const listItemStyle: React.CSSProperties = {
    padding: '8px 0',
    borderBottom: '1px dotted #ccc'
};

export default WorkoutGenerator;
