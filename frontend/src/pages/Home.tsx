// src/pages/Home.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext'; // Import du contexte

const Home = () => {
    const { isAuthenticated, user } = useAuth();

    return (
        <div style={homeContainerStyle}>
            {isAuthenticated ? (
                // --- Accueil pour utilisateur Connecté ---
                <div style={contentBoxStyle}>
                    <h1 style={titleStyle}>Bienvenue, {user?.username} !</h1>
                    <p style={taglineStyle}>Prêt à exploser vos objectifs ?</p>
                    <div style={{display: 'flex', gap: '20px', justifyContent: 'center', marginTop: '30px'}}>
                        <Link to="/generate-workout" style={buttonLinkStyle}>
                            Générer mon Entraînement
                        </Link>
                        <Link to="/dashboard" style={{...buttonLinkStyle, backgroundColor: '#ffc107', color: '#333'}}>
                            Voir mon Profil
                        </Link>
                    </div>
                </div>
            ) : (
                // --- Accueil pour visiteur Déconnecté ---
                <div style={contentBoxStyle}>
                    <h1 style={titleStyle}>Fitness-Clash : Votre Coach IA Personnel</h1>
                    <p style={taglineStyle}>Des entraînements personnalisés basés sur l'IA et vos progrès.</p>
                    <div style={{display: 'flex', gap: '20px', justifyContent: 'center', marginTop: '30px'}}>
                        <Link to="/register" style={buttonLinkStyle}>
                            Commencer Gratuitement
                        </Link>
                        <Link to="/login" style={{...buttonLinkStyle, backgroundColor: '#6c757d'}}>
                            J'ai déjà un compte
                        </Link>
                    </div>
                </div>
            )}
        </div>
    );
};

// Styles rapides
const homeContainerStyle: React.CSSProperties = {
    padding: '100px 20px',
    textAlign: 'center',
    backgroundColor: '#f8f9fa',
    minHeight: 'calc(100vh - 70px)' // Espace restant
};

const contentBoxStyle: React.CSSProperties = {
    maxWidth: '800px',
    margin: '0 auto',
    padding: '40px',
    backgroundColor: 'white',
    borderRadius: '12px',
    boxShadow: '0 8px 16px rgba(0,0,0,0.1)'
};

const titleStyle: React.CSSProperties = {
    fontSize: '3em',
    color: '#007BFF',
    marginBottom: '10px'
};

const taglineStyle: React.CSSProperties = {
    fontSize: '1.5em',
    color: '#6c757d',
    marginBottom: '40px'
};

const buttonLinkStyle: React.CSSProperties = {
    padding: '15px 30px',
    backgroundColor: '#28a745',
    color: 'white',
    textDecoration: 'none',
    borderRadius: '6px',
    fontSize: '1.2em',
    fontWeight: 'bold',
    transition: 'background-color 0.3s'
};


export default Home;
