// src/pages/Home.tsx (VERSION STYLISÉE)

import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../contexts/AuthContext'; // Assurez-vous que le chemin est correct

const Home = () => {
    const { isAuthenticated, user } = useAuth();

    return (
        <div style={containerStyle}>
            <div style={cardStyle}>
                {isAuthenticated ? (
                    <>
                        <h1 style={welcomeTitleStyle}>Bienvenue, {user?.username || 'Utilisateur'} !</h1>
                        <p style={taglineStyle}>Que voulez-vous faire aujourd'hui ?</p>
                        <div style={buttonGroupStyle}>
                            <Link to="/generate-workout" style={primaryButtonStyle}>
                                Générer mon Entraînement
                            </Link>
                            <Link to="/dashboard" style={secondaryButtonStyle}>
                                Voir mon Profil
                            </Link>
                        </div>
                    </>
                ) : (
                    <>
                        <h1 style={titleStyle}>
                            Fitness-Clash
                        </h1>
                        <p style={taglineStyle}>
                            Des entraînements personnalisés basés sur vos progrès.
                        </p>
                        <div style={buttonGroupStyle}>
                            <Link to="/register" style={primaryButtonStyle}>
                                Commencer Gratuitement
                            </Link>
                            <Link to="/login" style={secondaryButtonStyle}>
                                J'ai déjà un compte
                            </Link>
                        </div>
                    </>
                )}
            </div>
        </div>
    );
};

// ============================================
// STYLES (Adaptés au thème sombre/rouge/gris)
// ============================================

const THEME_DARK_BG = '#1C1C1E'; // Fond sombre général
const CARD_LIGHT_BG = '#28282B'; // Fond plus clair pour la carte
const ACCENT_RED = '#FF3B3F'; // Rouge vif pour les accents
const TEXT_LIGHT = 'white';
const TEXT_GRAY = '#A0A0A0';

const containerStyle: React.CSSProperties = {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    minHeight: 'calc(100vh - 60px)', // Prend en compte la hauteur du header
    backgroundColor: THEME_DARK_BG,
    padding: '20px',
    fontFamily: 'Arial, sans-serif'
};

const cardStyle: React.CSSProperties = {
    backgroundColor: CARD_LIGHT_BG,
    borderRadius: '12px',
    padding: '40px',
    textAlign: 'center',
    boxShadow: '0 8px 20px rgba(0, 0, 0, 0.4)',
    maxWidth: '600px',
    width: '100%',
    color: TEXT_LIGHT
};

const titleStyle: React.CSSProperties = {
    fontSize: '36px',
    fontWeight: 'bold',
    marginBottom: '20px',
    color: ACCENT_RED // Titre en rouge
};

const welcomeTitleStyle: React.CSSProperties = {
    fontSize: '36px',
    fontWeight: 'bold',
    marginBottom: '20px',
    color: TEXT_LIGHT // Titre de bienvenue en blanc
};

const taglineStyle: React.CSSProperties = {
    fontSize: '18px',
    marginBottom: '40px',
    color: TEXT_GRAY
};

const buttonGroupStyle: React.CSSProperties = {
    display: 'flex',
    flexDirection: 'column', // Boutons empilés pour une meilleure mobile-friendliness
    gap: '20px',
    marginTop: '30px'
};

const baseButtonStyle: React.CSSProperties = {
    padding: '15px 30px',
    borderRadius: '8px',
    fontSize: '18px',
    fontWeight: 'bold',
    cursor: 'pointer',
    textDecoration: 'none', // Pour les liens
    transition: 'background-color 0.3s ease, transform 0.2s ease',
    display: 'inline-block', // Pour que les padding et margin fonctionnent
    textAlign: 'center'
};

const primaryButtonStyle: React.CSSProperties = {
    ...baseButtonStyle,
    backgroundColor: ACCENT_RED, // Bouton principal rouge
    color: TEXT_LIGHT,
    border: 'none',
    ':hover': {
        backgroundColor: '#CC2E31', // Rouge plus foncé au survol
        transform: 'translateY(-2px)'
    }
};

const secondaryButtonStyle: React.CSSProperties = {
    ...baseButtonStyle,
    backgroundColor: '#383838', // Bouton secondaire gris foncé
    color: TEXT_LIGHT,
    border: '1px solid #555',
    ':hover': {
        backgroundColor: '#4A4A4A', // Gris plus clair au survol
        transform: 'translateY(-2px)'
    }
};

export default Home;
