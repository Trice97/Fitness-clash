import React, { useEffect, useState } from 'react';

// 1. Définir l'interface pour les données d'un exercice (basée sur ExerciseResponse de FastAPI)
interface Exercise {
    id: number;
    name: string;
    description: string;
    muscle_group: string;
    difficulty: string;
}

const ExercisesPage = () => {
    const [exercises, setExercises] = useState<Exercise[]>([]);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchExercises = async () => {
            setError('');
            setIsLoading(true);

            // *** VÉRIFIEZ L'URL DE BASE DU BACK-END ***
            // Route : GET http://localhost:8000/exercises/
            const API_URL = "http://localhost:8000/exercises/"; 

            try {
                const response = await fetch(API_URL, {
                    method: 'GET',
                    headers: {
                        'Content-Type': 'application/json',
                        // NOTE : Cette route est publique dans exercises.py, 
                        // donc pas besoin de 'Authorization' pour l'instant.
                    },
                });

                if (response.ok) {
                    const data: Exercise[] = await response.json();
                    setExercises(data);
                } else {
                    const errorData = await response.json();
                    setError(errorData.detail || 'Erreur lors du chargement des exercices.');
                }
            } catch (err) {
                console.error("Erreur réseau:", err);
                setError("Impossible de joindre le serveur. Le back-end est-il démarré ?");
            } finally {
                setIsLoading(false);
            }
        };

        fetchExercises();
    }, []); // Le tableau vide assure que l'appel se fait une seule fois au montage

    // --- Rendu conditionnel ---

    if (isLoading) {
        return <div style={containerStyle}><p>Chargement des exercices...</p></div>;
    }

    if (error) {
        return <div style={{...containerStyle, color: 'red'}}><p>Erreur: {error}</p></div>;
    }
    
    if (exercises.length === 0) {
        return <div style={containerStyle}><p>Aucun exercice trouvé. (Assurez-vous d'avoir des données seedées)</p></div>;
    }

    // --- Rendu de la liste des exercices ---
    return (
        <div style={containerStyle}>
            <h1 style={{color: '#007BFF'}}>Catalogue des Exercices ({exercises.length})</h1>
            <p>Liste des exercices disponibles dans la base de données de Fitness-Clash.</p>

            <div style={listContainerStyle}>
                {exercises.map((exercise) => (
                    <div key={exercise.id} style={exerciseCardStyle}>
                        <h3>{exercise.name}</h3>
                        <p><strong>Groupe musculaire :</strong> {exercise.muscle_group}</p>
                        <p><strong>Difficulté :</strong> {exercise.difficulty}</p>
                        <p style={{fontSize: '0.9em', color: '#666'}}>{exercise.description}</p>
                    </div>
                ))}
            </div>
        </div>
    );
};

// Styles pour le composant
const containerStyle: React.CSSProperties = {
    padding: '20px', 
    textAlign: 'center', 
    maxWidth: '1200px', 
    margin: '0 auto'
};

const listContainerStyle: React.CSSProperties = {
    display: 'grid',
    gridTemplateColumns: 'repeat(auto-fill, minmax(300px, 1fr))',
    gap: '20px',
    marginTop: '30px',
    textAlign: 'left'
};

const exerciseCardStyle: React.CSSProperties = {
    padding: '15px',
    border: '1px solid #ddd',
    borderRadius: '8px',
    boxShadow: '0 2px 4px rgba(0,0,0,0.05)',
    backgroundColor: '#fff'
};

export default ExercisesPage;
