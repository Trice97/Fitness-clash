// src/pages/Register.tsx (VERSION STYLISÉE)

import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';

const API_BASE_URL = "http://localhost:8000";

const Register = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    
    // États pour les messages de statut
    const [error, setError] = useState<string | null>(null);
    const [success, setSuccess] = useState<string | null>(null);
    
    const navigate = useNavigate();

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);
        setSuccess(null);
        setIsLoading(true);

        const API_URL = `${API_BASE_URL}/api/users/`;

        try {
            const response = await fetch(API_URL, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ username, email, password }),
            });

            const responseData = await response.json();

            if (response.ok) {
                setSuccess("Inscription réussie ! Vous pouvez maintenant vous connecter.");
                // Redirection vers la page de connexion après un court délai
                setTimeout(() => {
                    navigate('/login'); 
                }, 2000); 

            } else {
                const errorMessage = responseData.detail || "Erreur lors de l'inscription.";
                setError(errorMessage);
            }
        } catch (error) {
            console.error("Erreur réseau:", error);
            setError("Impossible de joindre le serveur. Veuillez réessayer.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div style={containerStyle}>
            {/* Icône de l'haltère */}
            <div style={logoStyle}>
                <svg width="50" height="50" viewBox="0 0 50 50" fill="none" xmlns="http://www.w3.org/2000/svg">
                    <path d="M4.16667 20.8333H0V29.1667H4.16667V20.8333ZM45.8333 20.8333H50V29.1667H45.8333V20.8333ZM10.4167 20.8333C10.4167 15.1167 15.1167 10.4167 20.8333 10.4167H29.1667C34.8833 10.4167 39.5833 15.1167 39.5833 20.8333V29.1667C39.5833 34.8833 34.8833 39.5833 29.1667 39.5833H20.8333C15.1167 39.5833 10.4167 34.8833 10.4167 29.1667V20.8333ZM12.5 25C12.5 16.275 19.275 9.58333 25 9.58333C30.725 9.58333 37.5 16.275 37.5 25C37.5 33.725 30.725 40.4167 25 40.4167C19.275 40.4167 12.5 33.725 12.5 25Z" fill="#FF3B3F"/>
                </svg>
            </div>
            <h1 style={titleStyle}>S'inscrire</h1>

            {/* Affichage des messages de statut */}
            {success && <div style={successMessageStyle}>{success}</div>}
            {error && <div style={errorMessageStyle}>{error}</div>}

            <form onSubmit={handleSubmit} style={formStyle}>
                
                <label htmlFor="username" style={labelStyle}>Nom d'utilisateur</label>
                <input 
                    id="username"
                    type="text" 
                    value={username} 
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Entrez votre nom d'utilisateur"
                    required 
                    style={inputStyle}
                />
                
                <label htmlFor="email" style={labelStyle}>E-mail</label>
                <input 
                    id="email"
                    type="email" 
                    value={email} 
                    onChange={(e) => setEmail(e.target.value)}
                    placeholder="Entrez votre e-mail"
                    required 
                    style={inputStyle}
                />
                
                <label htmlFor="password" style={labelStyle}>Mot de passe</label>
                <input 
                    id="password"
                    type="password" 
                    value={password} 
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Choisissez un mot de passe"
                    required 
                    style={inputStyle}
                />
                
                <button type="submit" disabled={isLoading} style={buttonStyle}>
                    {isLoading ? "Inscription en cours..." : "S'inscrire"}
                </button>
            </form>

            <p style={linkTextStyle}>
                Déjà un compte ? 
                <Link to="/login" style={linkStyle}> Se connecter</Link>
            </p>
        </div>
    );
};

// Styles pour les messages (identiques à Login.tsx)
const successMessageStyle: React.CSSProperties = {
    padding: '10px',
    marginBottom: '20px',
    backgroundColor: 'rgba(40, 167, 69, 0.2)', // Vert transparent
    color: '#28a745',
    borderRadius: '4px',
    textAlign: 'center'
};

const errorMessageStyle: React.CSSProperties = {
    padding: '10px',
    marginBottom: '20px',
    backgroundColor: 'rgba(220, 53, 69, 0.2)', // Rouge transparent
    color: '#dc3545',
    borderRadius: '4px',
    textAlign: 'center'
};

// Styles du composant (identiques à Login.tsx)
const containerStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh',
    backgroundColor: '#1C1C1E', // Fond noir profond
    color: 'white',
    padding: '20px',
    fontFamily: 'Arial, sans-serif'
};

const logoStyle: React.CSSProperties = {
    marginBottom: '20px'
};

const titleStyle: React.CSSProperties = {
    fontSize: '32px',
    fontWeight: 'bold',
    marginBottom: '50px',
    color: 'white'
};

const formStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    maxWidth: '350px'
};

const labelStyle: React.CSSProperties = {
    textAlign: 'left',
    marginBottom: '8px',
    fontSize: '16px',
    fontWeight: 'bold',
    color: 'white'
};

const inputStyle: React.CSSProperties = {
    padding: '15px',
    marginBottom: '20px',
    border: 'none',
    borderRadius: '8px',
    backgroundColor: '#383838', // Gris foncé pour les champs
    color: 'white',
    fontSize: '16px',
    '::placeholder': { 
        color: '#A0A0A0'
    }
};

const buttonStyle: React.CSSProperties = {
    padding: '15px',
    border: 'none',
    borderRadius: '8px',
    backgroundColor: '#FF3B3F', // Bouton rouge vif
    color: 'white',
    fontSize: '18px',
    fontWeight: 'bold',
    cursor: 'pointer',
    marginTop: '10px',
    transition: 'background-color 0.3s ease'
};

const linkTextStyle: React.CSSProperties = {
    marginTop: '30px',
    fontSize: '16px',
    color: '#A0A0A0'
};

const linkStyle: React.CSSProperties = {
    color: '#FF3B3F', // Rouge vif pour le lien
    textDecoration: 'none',
    fontWeight: 'bold'
};

export default Register;
