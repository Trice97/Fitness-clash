import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Navigate } from 'react-router-dom';

// ------------------------------------
// 1. IMPORTS DES PAGES LOCALES
// Les pages sont importées après les librairies externes
// ------------------------------------
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';
import Register from './pages/Register';

// ------------------------------------
// 2. IMPORT DU STYLE (laissez le style en bas du bloc d'imports)
// ------------------------------------
import './App.css'; 
// Note : Les imports de logos (viteLogo, reactLogo) et useState() sont retirés
// car ils étaient uniquement pour la démo initiale de Vite et ne servent plus au routage.

// ------------------------------------
// COMPOSANT PRINCIPAL DE L'APPLICATION
// ------------------------------------
function App() {
  // Ici, nous simulerons l'état d'authentification.
  // Plus tard, cette variable sera alimentée par un Context ou un hook d'authentification.
  const [isAuthenticated, setIsAuthenticated] = useState(false); 

  return (
    <BrowserRouter>
      <Routes>
        {/* ========================================================== */}
        {/* ROUTES PUBLIQUES (ACCESSIBLES SANS CONNEXION) */}
        {/* ========================================================== */}
        
        {/* Tâche 1.2 : Connexion */}
        <Route path="/login" element={<Login />} /> 
        
        {/* Tâche 1.4 : Inscription */}
        <Route path="/register" element={<Register />} />

        {/* ========================================================== */}
        {/* ROUTES PROTÉGÉES (ACCESSIBLES SEULEMENT APRÈS CONNEXION) */}
        {/* ========================================================== */}
        
        {/* Si authentifié, affiche le Dashboard. Sinon, redirige vers la page de connexion. */}
        <Route 
          path="/dashboard" 
          element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" replace />} 
        />

        {/* Redirection par défaut (si l'utilisateur arrive sur '/') */}
        <Route 
          path="/" 
          element={isAuthenticated ? <Navigate to="/dashboard" replace /> : <Navigate to="/login" replace />} 
        />
        
      </Routes>
    </BrowserRouter>
  );
}

export default App;

