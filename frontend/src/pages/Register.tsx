import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // Import de useNavigate

const Register = () => {
    const navigate = useNavigate(); // Hook pour la redirection
    
    // 1. Déclaration des états pour chaque champ du formulaire
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confirmPassword, setConfirmPassword] = useState('');
    const [error, setError] = useState(''); 
    const [isLoading, setIsLoading] = useState(false); // AJOUT: État de chargement

    // 2. Fonction asynchrone appelée lors de la soumission du formulaire
    const handleSubmit = async (e: React.FormEvent) => { // AJOUT: 'async'
        e.preventDefault(); 

        // Validation simple (Vérification Front-End)
        if (password !== confirmPassword) {
            setError('Les mots de passe ne correspondent pas.');
            return;
        }
        
        setError(''); 
        setIsLoading(true); // Début du chargement

        // --- LOGIQUE D'APPEL API ---
        const API_URL = "http://localhost:8000/users/"; 

        // Corps de la requête (FastAPI attend du JSON pour UserCreate)
        const requestBody = {
            username,
            email,
            password,
            // Si l'API UserCreate nécessite d'autres champs (ex: difficulty_level), ajoutez-les ici.
            // Pour l'instant, nous nous en tenons à la base.
        };

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json', // IMPORTANT: On envoie du JSON
                },
                body: JSON.stringify(requestBody), // Conversion de l'objet JS en chaîne JSON
            });

            const responseData = await response.json();

            if (response.ok) {
                // Succès: Code 201 Created est attendu
                console.log('Inscription réussie. Utilisateur créé:', responseData);
                
                // Redirection après succès (le plus souvent vers la page de connexion)
                alert("Compte créé avec succès ! Vous pouvez maintenant vous connecter.");
                navigate('/login'); 
            } else {
                // Échec: Ex: Email déjà utilisé, mot de passe trop court, données manquantes
                // FastAPI renvoie souvent un objet avec un champ 'detail'
                const errorMessage = responseData.detail 
                                   ? (Array.isArray(responseData.detail) ? responseData.detail[0].msg : responseData.detail)
                                   : 'Erreur lors de l\'inscription.';
                setError(errorMessage);
            }
        } catch (err) {
            // Échec réseau (serveur non démarré, CORS, etc.)
            console.error("Erreur réseau ou du serveur:", err);
            setError("Impossible de joindre le serveur. Veuillez vérifier si le back-end est démarré.");
        } finally {
            setIsLoading(false); // Fin du chargement (dans tous les cas)
        }
    };

    return (
        <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
            <h1 style={{ textAlign: 'center', color: '#007BFF' }}>Créer un Compte</h1>
            
            {/* Affichage des erreurs si l'état 'error' est rempli */}
            {error && (
                <p style={{ color: 'red', textAlign: 'center', fontWeight: 'bold' }}>
                    Erreur: {error}
                </p>
            )}

            <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
                
                {/* Inputs existants */}
                <input type="text" placeholder="Nom d'utilisateur" value={username} onChange={(e) => setUsername(e.target.value)} required style={inputStyle} disabled={isLoading} />
                <input type="email" placeholder="Adresse Email" value={email} onChange={(e) => setEmail(e.target.value)} required style={inputStyle} disabled={isLoading} />
                <input type="password" placeholder="Mot de passe" value={password} onChange={(e) => setPassword(e.target.value)} required style={inputStyle} disabled={isLoading} />
                <input type="password" placeholder="Confirmer le Mot de passe" value={confirmPassword} onChange={(e) => setConfirmPassword(e.target.value)} required style={inputStyle} disabled={isLoading} />

                <button 
                    type="submit" 
                    style={buttonStyle}
                    disabled={isLoading}
                >
                    {isLoading ? "Inscription en cours..." : "S'inscrire"}
                </button>
            </form>
            
            <p style={{ marginTop: '20px', textAlign: 'center' }}>
                Déjà un compte ? <Link to="/login" style={{ color: '#007BFF' }}>Connectez-vous</Link>
            </p>
        </div>
    );
};

// Styles rapides (inchangés)
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

export default Register;
