import React from 'react';
import { useAuth } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

// Composant temporaire pour le bouton de génération
const WorkoutAction: React.FC = () => {
    const buttonStyle: React.CSSProperties = {
        padding: '15px 30px',
        backgroundColor: '#28a745', // Vert pour l'action principale
        color: 'white',
        border: 'none',
        borderRadius: '8px',
        fontSize: '20px',
        cursor: 'pointer',
        marginTop: '30px',
        transition: 'background-color 0.3s'
    };

    const handleClick = () => {
        alert("Action : Demander au Back-End de générer un Workout ! (Simulé)");
        // TODO: Prochaine étape : appel à POST /workouts/generate
    };

    return (
        <button 
            onClick={handleClick}
            style={buttonStyle}
            onMouseOver={(e) => (e.currentTarget.style.backgroundColor = '#218838')}
            onMouseOut={(e) => (e.currentTarget.style.backgroundColor = '#28a745')}
        >
            Générer un Workout
        </button>
    );
};

// Composant principal du Dashboard
const Dashboard = () => {
    const { logout } = useAuth();
    const navigate = useNavigate();

    const handleLogout = () => {
        logout();
        navigate('/login');
    };

    const containerStyle: React.CSSProperties = {
        maxWidth: '800px',
        margin: '50px auto',
        padding: '30px',
        border: '1px solid #007BFF',
        borderRadius: '12px',
        boxShadow: '0 8px 16px rgba(0,0,0,0.2)',
        backgroundColor: '#f9f9f9',
        textAlign: 'center'
    };

    const logoutButtonStyle: React.CSSProperties = {
        padding: '8px 16px',
        backgroundColor: '#dc3545',
        color: 'white',
        border: 'none',
        borderRadius: '6px',
        fontSize: '16px',
        cursor: 'pointer',
        marginTop: '25px',
        position: 'absolute',
        top: '20px',
        right: '20px',
        transition: 'background-color 0.3s'
    };

    return (
        <div style={{ position: 'relative' }}>
            <button 
                onClick={handleLogout}
                style={logoutButtonStyle}
                onMouseOver={(e) => (e.currentTarget.style.backgroundColor = '#c82333')}
                onMouseOut={(e) => (e.currentTarget.style.backgroundColor = '#dc3545')}
            >
                Déconnexion
            </button>
            
            <div style={containerStyle}>
                <h1 style={{ color: '#007BFF', marginBottom: '10px' }}>Bienvenue dans Fitness Clash !</h1>
                <p style={{ fontSize: '1.2em', color: '#333' }}>
                    Prêt pour le défi ?
                </p>

                <WorkoutAction />

                <div style={{ marginTop: '50px', borderTop: '1px solid #ddd', paddingTop: '20px' }}>
                    {/* Placeholder pour le composant d'historique ou le Workout en cours */}
                    <p style={{ fontStyle: 'italic', color: '#555' }}>
                        Historique des Workouts et Clashs s'afficheront ici.
                    </p>
                </div>
            </div>
        </div>
    );
};

export default Dashboard;

