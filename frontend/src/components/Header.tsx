// src/components/Header.tsx

import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext'; // Import crucial

const Header = () => {
    // 1. Récupération de l'état d'authentification et de la fonction de déconnexion
    const { isAuthenticated, user, logout } = useAuth();

    return (
        <header style={headerStyle}>
            <div style={logoStyle}>
                {/* Lien vers la page d'accueil */}
                <Link to="/" style={linkStyle}>
                    💪 Fitness-Clash
                </Link>
            </div>
            
            <nav style={navStyle}>
                {/* Lien vers le catalogue des exercices */}
                <Link to="/exercises" style={linkStyle}>
                    Exercices
                </Link>

                {/* 2. Affichage conditionnel basé sur l'état d'authentification */}
                {isAuthenticated ? (
                    // --- État Connecté ---
                    <>
                        {/* Lien vers la page de génération d'entraînement */}
                        <Link to="/generate-workout" style={linkStyle}>
                            Générateur
                        </Link>
                        {/* Lien vers le Tableau de Bord */}
                        <Link to="/dashboard" style={linkStyle}>
                            Tableau de Bord ({user?.username})
                        </Link>
                        {/* Bouton de Déconnexion */}
                        <button onClick={logout} style={buttonStyle}>
                            Déconnexion
                        </button>
                    </>
                ) : (
                    // --- État Déconnecté ---
                    <>
                        <Link to="/login" style={linkStyle}>
                            Connexion
                        </Link>
                        <Link to="/register" style={{...linkStyle, border: '1px solid white', padding: '5px 10px', borderRadius: '4px'}}>
                            Inscription
                        </Link>
                    </>
                )}
            </nav>
        </header>
    );
};

// Styles rapides
const headerStyle: React.CSSProperties = {
    display: 'flex',
    justifyContent: 'space-between',
    alignItems: 'center',
    padding: '10px 40px',
    backgroundColor: '#007BFF',
    color: 'white',
    boxShadow: '0 2px 4px rgba(0,0,0,0.1)'
};

const logoStyle: React.CSSProperties = {
    fontSize: '24px',
    fontWeight: 'bold'
};

const navStyle: React.CSSProperties = {
    display: 'flex',
    gap: '20px',
    alignItems: 'center'
};

const linkStyle: React.CSSProperties = {
    color: 'white',
    textDecoration: 'none',
    fontSize: '16px',
    padding: '5px 0'
};

const buttonStyle: React.CSSProperties = {
    backgroundColor: 'transparent',
    color: 'white',
    border: '1px solid white',
    padding: '5px 10px',
    borderRadius: '4px',
    cursor: 'pointer',
    fontSize: '16px'
};

export default Header;
