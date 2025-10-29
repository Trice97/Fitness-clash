import { Workout } from '../types';

// La Base URL pour l'API de Patrice (par défaut: http://localhost:8000)
// Nous allons utiliser une variable d'environnement pour simuler le développement BE
const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000';

/**
 * Fonction utilitaire pour obtenir le header d'autorisation JWT.
 * @returns Headers d'autorisation pour les requêtes protégées.
 */
const getAuthHeaders = (): HeadersInit => {
  // En attendant d'utiliser le Context, nous récupérons le token depuis localStorage (où il est stocké par AuthContext)
  const token = localStorage.getItem('token');
  if (!token) {
    throw new Error("Utilisateur non authentifié. Impossible d'appeler l'API.");
  }
  return {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${token}`,
  };
};

/**
 * Appelle l'API pour générer un nouveau workout pour l'utilisateur connecté.
 * Endpoint BE: POST /workouts/generate
 * @returns Le Workout généré.
 */
export const generateWorkout = async (): Promise<Workout> => {
  const response = await fetch(`${API_BASE_URL}/workouts/generate`, {
    method: 'POST',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    // Si la réponse n'est pas 200 OK
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Erreur lors de la génération du Workout.');
  }

  return response.json();
};

/**
 * Marque un workout spécifique comme terminé.
 * Endpoint BE: POST /workouts/{id}/complete
 * @param workoutId L'ID du workout à compléter.
 * @returns Le Workout mis à jour.
 */
export const completeWorkout = async (workoutId: number): Promise<Workout> => {
  const response = await fetch(`${API_BASE_URL}/workouts/${workoutId}/complete`, {
    method: 'POST',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || `Erreur lors de la finalisation du Workout ${workoutId}.`);
  }

  return response.json();
};

/**
 * Récupère l'historique des workouts de l'utilisateur.
 * Endpoint BE: GET /workouts/history
 * @param limit Nombre maximum de workouts à retourner.
 * @returns Une liste de Workouts.
 */
export const fetchWorkoutHistory = async (limit: number = 10): Promise<Workout[]> => {
  const response = await fetch(`${API_BASE_URL}/workouts/history?limit=${limit}`, {
    method: 'GET',
    headers: getAuthHeaders(),
  });

  if (!response.ok) {
    const errorData = await response.json();
    throw new Error(errorData.detail || 'Erreur lors de la récupération de l\'historique.');
  }

  return response.json();
};

