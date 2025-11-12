import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // Pour la déconnexion/redirection

// Interface pour typer les données utilisateur
interface UserData {
    id: number;
    username: string;
    email: string;
    difficulty_level: string;
    total_points: number;
}

const Dashboard = () => {
    const navigate = useNavigate();
    const [user, setUser] = useState<UserData | null>(null);
    const [isLoading, setIsLoading] = useState(true);
    const [error, setError] = useState('');

    useEffect(() => {
        const fetchUserData = async () => {
            const token = localStorage.getItem('accessToken');
            
            // 1. VÉRIFICATION DU TOKEN
            if (!token) {
                console.log("Token non trouvé. Redirection vers la page de connexion.");
                // Si pas de token, on redirige l'utilisateur
                navigate('/login'); 
                return;
            }

            // 2. APPEL SÉCURISÉ À /auth/me
            const API_URL = "http://localhost:8000/auth/me"; 

            try {
                const response = await fetch(API_URL, {
                    method: 'GET',
                    headers: {
                        // --- ENVOI DU TOKEN DANS LE HEADER AUTHORIZATION ---
                        'Authorization': `Bearer ${token}`, 
                        'Content-Type': 'application/json',
                    },
                });

                if (response.ok) {
                    const userData: UserData = await response.json();
                    setUser(userData);
                } else if (response.status === 401) {
                    // Token expiré ou invalide
                    console.log("Token invalide. Déconnexion.");
                    localStorage.removeItem('accessToken');
                    navigate('/login');
                } else {
                    setError('Erreur lors du chargement des données utilisateur.');
                }
            } catch (err) {
                console.error("Erreur réseau ou du serveur:", err);
                setError("Impossible de joindre le serveur ou erreur réseau.");
            } finally {
                setIsLoading(false);
            }
        };

        fetchUserData();
    }, [navigate]); // La dépendance 'navigate' est incluse

    // Logique de déconnexion
    const handleLogout = () => {
        localStorage.removeItem('accessToken');
        navigate('/login');
    }

    // --- Rendu conditionnel ---

    if (isLoading) {
        return (
            <div style={{ padding: '20px', textAlign: 'center' }}>
                <p>Chargement du profil...</p>
            </div>
        );
    }

    if (error) {
        return (
            <div style={{ padding: '20px', textAlign: 'center', color: 'red' }}>
                <p>Erreur: {error}</p>
                <button onClick={handleLogout} style={buttonStyle}>Se déconnecter</button>
            </div>
        );
    }
    
    if (!user) {
         // Ce cas ne devrait pas arriver si le token n'est pas trouvé (redirection gérée au début)
         return <div style={{ padding: '20px', textAlign: 'center' }}><p>Utilisateur non trouvé.</p></div>
    }


    // --- Rendu final du tableau de bord ---
    return (
        <div style={{ padding: '20px', textAlign: 'center', backgroundColor: '#e6ffe6' }}>
            <h1>Tableau de bord de {user.username || user.email}</h1>
            <h2>✅ Connexion sécurisée réussie !</h2>
            
            <div style={{ margin: '30px auto', maxWidth: '500px', border: '1px solid #007BFF', padding: '20px', borderRadius: '8px', textAlign: 'left' }}>
                <h3>Vos Informations (Récupérées via /auth/me)</h3>
                <p><strong>ID:</strong> {user.id}</p>
                <p><strong>Email:</strong> {user.email}</p>
                <p><strong>Niveau de difficulté:</strong> {user.difficulty_level}</p>
                <p><strong>Points cumulés:</strong> {user.total_points}</p>
            </div>

            <p style={{ marginTop: '20px' }}>Le contenu principal de notre application sera développé ici.</p>

            <button onClick={handleLogout} style={{...buttonStyle, backgroundColor: '#dc3545'}}>
                Se Déconnecter
            </button>
        </div>
    );
};

// Style du bouton de déconnexion
const buttonStyle: React.CSSProperties = {
    padding: '10px 20px',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    fontSize: '16px',
    cursor: 'pointer',
    marginTop: '20px'
};

export default Dashboard;
