import React, { useState } from 'react';
// 1. Import de useNavigate pour la redirection après connexion
import { Link, useNavigate } from 'react-router-dom'; 

const Login = () => {
    // Initialisation du hook de navigation
    const navigate = useNavigate();
    
    // 2. Déclaration des états
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [error, setError] = useState(''); 
    const [isLoading, setIsLoading] = useState(false); // AJOUT: État de chargement

    // 3. Fonction asynchrone appelée lors de la soumission
    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault(); 
        setError(''); // Réinitialise l'erreur
        setIsLoading(true); // Début du chargement

        // 4. Configuration de l'appel API
        // *** VÉRIFIEZ LE PORT (ex: 8000) ET L'URL DE BASE DU BACK-END ***
        const API_URL = "http://localhost:8000/auth/login"; 
        
        // 5. Création des données au format 'form-urlencoded' (requis par FastAPI)
        const data = new URLSearchParams();
        data.append('username', email); // L'email est envoyé comme 'username'
        data.append('password', password);

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded', // IMPORTANT
                },
                body: data,
            });

            const responseData = await response.json();

            if (response.ok) {
                // Succès: Récupérer et stocker le token
                const accessToken = responseData.access_token;
                localStorage.setItem('accessToken', accessToken);
                
                console.log('Connexion réussie. Token stocké:', accessToken);
                
                // Redirection vers le tableau de bord
                navigate('/dashboard'); 

            } else {
                // Échec de l'authentification (ex: 401 Unauthorized)
                setError(responseData.detail || 'Email ou mot de passe incorrect.');
            }
        } catch (err) {
            // Échec réseau ou serveur inaccessible
            console.error("Erreur réseau ou du serveur:", err);
            setError("Impossible de joindre le serveur. Vérifiez que le back-end est démarré.");
        } finally {
            setIsLoading(false); // Fin du chargement
        }
    };

    return (
        <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
            <h1 style={{ textAlign: 'center', color: '#007BFF' }}>Se Connecter</h1>
            
            {/* Affichage des erreurs si l'état 'error' est rempli */}
            {error && (
                <p style={{ color: 'red', textAlign: 'center', fontWeight: 'bold' }}>
                    Erreur: {error}
                </p>
            )}

            {/* Le formulaire géré par React */}
            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                
                <input
                    type="email"
                    placeholder="Adresse Email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    required
                    style={inputStyle}
                    disabled={isLoading} // Désactivation pendant le chargement
                />

                <input
                    type="password"
                    placeholder="Mot de passe"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    required
                    style={inputStyle}
                    disabled={isLoading} // Désactivation pendant le chargement
                />

                <button 
                    type="submit"
                    style={buttonStyle}
                    disabled={isLoading} // Empêche les clics multiples pendant le chargement
                >
                    {/* Affichage conditionnel du texte du bouton */}
                    {isLoading ? 'Connexion en cours...' : 'Connexion'}
                </button>
            </form>
            
            <p style={{ marginTop: '20px', textAlign: 'center' }}>
                Pas encore inscrit ? <Link to="/register" style={{ color: '#007BFF' }}>Créer un compte</Link>
            </p>
        </div>
    );
};

// Styles rapides (réutilisés du composant Register)
const inputStyle: React.CSSProperties = {
    padding: '10px',
    borderRadius: '4px',
    border: '1px solid #ccc',
    fontSize: '16px'
};

const buttonStyle: React.CSSProperties = {
    padding: '12px',
    backgroundColor: '#007BFF',
    color: 'white',
    border: 'none',
    borderRadius: '4px',
    fontSize: '16px',
    cursor: 'pointer',
    marginTop: '10px'
};

export default Login;
