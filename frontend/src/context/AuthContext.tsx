// src/contexts/AuthContext.tsx (VERSION MISE À JOUR)

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

// Interface pour les données utilisateur (similaire à ce que /auth/me renvoie)
interface UserData {
    id: number;
    username: string;
    email: string;
    difficulty_level: string;
    total_points: number;
}

// Interface pour le contexte d'authentification complet
interface AuthContextType {
    user: UserData | null;           // AJOUTÉ : Les données de l'utilisateur connecté
    token: string | null;
    isLoading: boolean;              // AJOUTÉ : État de chargement initial (vérification du token)
    isAuthenticated: boolean;
    login: (token: string) => void;
    logout: () => void;
}

const AuthContext = createContext<AuthContextType | undefined>(undefined);
const API_BASE_URL = "http://localhost:8000"; // URL de base de l'API de Patrice

// Le Provider (Fournisseur)
interface AuthProviderProps {
    children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
    // Changement : Utilisation de 'accessToken' au lieu de 'authToken'
    const [token, setToken] = useState<string | null>(localStorage.getItem('accessToken'));
    
    // NOUVEAU : État pour les données utilisateur et le chargement
    const [user, setUser] = useState<UserData | null>(null);
    const [isLoading, setIsLoading] = useState(true);

    const isAuthenticated = !!token && !!user;

    // Fonction pour déconnecter (réinitialise tout)
    const handleLogout = () => {
        localStorage.removeItem('accessToken');
        setToken(null);
        setUser(null);
        setIsLoading(false);
    };

    // NOUVEAU : Fonction pour récupérer les données utilisateur avec le token
    const fetchUser = async (accessToken: string) => {
        const API_URL = `${API_BASE_URL}/auth/me`;
        
        try {
            const response = await fetch(API_URL, {
                method: 'GET',
                headers: {
                    'Authorization': `Bearer ${accessToken}`, 
                    'Content-Type': 'application/json',
                },
            });

            if (response.ok) {
                const userData: UserData = await response.json();
                setUser(userData);
            } else {
                // Token invalide ou expiré (401), on déconnecte
                handleLogout();
            }
        } catch (error) {
            console.error("Erreur lors de la récupération du profil:", error);
            handleLogout(); // Déconnexion en cas d'erreur réseau
        } finally {
            setIsLoading(false);
        }
    };

    // Gestion du login/register (stocke le token et lance la récupération des données)
    const handleLogin = (accessToken: string) => {
        localStorage.setItem('accessToken', accessToken);
        setToken(accessToken);
        // La récupération des données sera lancée par l'useEffect ci-dessous
    };
    
    // Fonction d'inscription (qui connecte directement)
    // Note : Votre ancienne fonction 'register' est désormais 'handleLogin'
    const register = handleLogin; 

    // Effet pour vérifier le token au chargement OU si le token change
    useEffect(() => {
        if (token) {
            // Un token est présent, on tente de récupérer les données utilisateur
            fetchUser(token);
        } else {
            // Pas de token, on met fin au chargement
            setIsLoading(false); 
        }
    }, [token]); // Se déclenche uniquement si le token change

    const contextValue: AuthContextType = {
        user, // MAINTENANT DISPONIBLE !
        token,
        isLoading,
        isAuthenticated,
        login: handleLogin,
        logout: handleLogout,
    };

    return (
        <AuthContext.Provider value={contextValue}>
            {/* Si en cours de chargement, on peut afficher un spinner global */}
            {isLoading ? <div style={{textAlign: 'center', padding: '100px'}}>Chargement de l'application...</div> : children}
        </AuthContext.Provider>
    );
};

// Hook personnalisé (inchangé)
export const useAuth = () => {
    const context = useContext(AuthContext);
    if (context === undefined) {
        throw new Error('useAuth doit être utilisé à l\'intérieur d\'un AuthProvider');
    }
    return context;
};
