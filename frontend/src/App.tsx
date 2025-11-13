import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './contexts/AuthContext'; // 1. Import du Context
import './App.css'; 

// ===================================
// NOUVEAUX IMPORTS
// ===================================
import Header from './components/Header'; // La barre de navigation
import Home from './pages/Home';         // La nouvelle page d'accueil
import ExercisesPage from './pages/ExercisesPage'; // Le catalogue d'exercices
import WorkoutGenerator from './pages/WorkoutGenerator'; // Le générateur d'entraînement

// Pages existantes
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Register from './pages/Register'; 

// Composant pour protéger les routes (inchangé)
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
    const { isAuthenticated, isLoading } = useAuth();

    // Attendre la fin du chargement initial du contexte
    if (isLoading) {
        return <div style={{textAlign: 'center', padding: '100px'}}>Chargement de l'application...</div>;
    }
    
    if (!isAuthenticated) {
        // Si l'utilisateur n'est pas connecté, le rediriger vers la page de connexion
        return <Navigate to="/login" replace />;
    }
    return <>{children}</>;
};

function App() {
    return (
        <BrowserRouter>
            {/* 2. Envelopper toutes les routes avec le AuthProvider */}
            <AuthProvider> 
                {/* Le Header doit être hors de <Routes> pour s'afficher sur toutes les pages */}
                <Header /> 
                
                <main> {/* Utilisation d'une balise <main> pour la sémantique */}
                    <Routes>
                        
                        {/* 1. NOUVELLE PAGE D'ACCUEIL */}
                        <Route path="/" element={<Home />} /> 
                        
                        {/* 2. PAGE D'EXERCICES (Publique) */}
                        <Route path="/exercises" element={<ExercisesPage />} />
                        
                        {/* ROUTES PUBLIQUES D'AUTHENTIFICATION */}
                        <Route path="/login" element={<Login />} />
                        <Route path="/register" element={<Register />} />
                        
                        {/* ==================================== */}
                        {/* ROUTES PROTÉGÉES (NÉCESSITENT CONNEXION) */}
                        {/* ==================================== */}

                        <Route
                            path="/dashboard"
                            element={
                                <ProtectedRoute>
                                    <Dashboard />
                                </ProtectedRoute>
                            }
                        />

                        {/* NOUVELLE ROUTE PROTÉGÉE POUR LE GÉNÉRATEUR */}
                        <Route
                            path="/generate-workout"
                            element={
                                <ProtectedRoute>
                                    <WorkoutGenerator />
                                </ProtectedRoute>
                            }
                        />

                        {/* GESTION DES ERREURS 404 */}
                        <Route path="*" element={<h1 style={{textAlign: 'center', marginTop: '50px'}}>404 - Page Introuvable</h1>} />

                    </Routes>
                </main>
            </AuthProvider>
        </BrowserRouter>
    );
}

export default App;
