import React from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';
import { AuthProvider, useAuth } from './context/AuthContext'; // 1. Import du Context
import './App.css'; 

// Pages
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Register from './pages/Register'; 

// Composant pour protéger les routes
// Il vérifie l'état d'authentification et redirige si l'utilisateur n'est pas connecté.
const ProtectedRoute: React.FC<{ children: React.ReactNode }> = ({ children }) => {
  const { isAuthenticated } = useAuth();
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
        <Routes>
          {/* ROUTES PUBLIQUES */}
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/" element={<Navigate to="/dashboard" replace />} /> {/* Redirection par défaut */}

          {/* ROUTES PROTÉGÉES - Utilisation du ProtectedRoute */}
          <Route
            path="/dashboard"
            element={
              // Le composant ProtectedRoute décide si Dashboard est affiché
              <ProtectedRoute>
                <Dashboard />
              </ProtectedRoute>
            }
          />
        </Routes>
      </AuthProvider>
    </BrowserRouter>
  );
}

export default App;

