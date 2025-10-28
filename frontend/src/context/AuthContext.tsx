import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

// 1. Définition des types pour le contexte
interface AuthContextType {
  isAuthenticated: boolean;
  token: string | null;
  login: (token: string) => void;
  logout: () => void;
  register: (token: string) => void; // Pour gérer le cas où l'inscription connecte directement
}

// Valeurs par défaut du contexte
const AuthContext = createContext<AuthContextType | undefined>(undefined);

// 2. Le Provider (Fournisseur) qui enveloppera toute l'application
interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  // L'état initial est récupéré du stockage local pour persister la connexion
  const [token, setToken] = useState<string | null>(localStorage.getItem('authToken'));
  const isAuthenticated = !!token; // Devient vrai si un token est présent

  // Effet pour mettre à jour localStorage dès que le token change
  useEffect(() => {
    if (token) {
      localStorage.setItem('authToken', token);
    } else {
      localStorage.removeItem('authToken');
    }
  }, [token]);

  // Fonction appelée après une connexion réussie
  const login = (newToken: string) => {
    setToken(newToken);
  };

  // Fonction de déconnexion
  const logout = () => {
    setToken(null);
  };

  // Fonction d'inscription (similaire au login, car souvent l'inscription connecte)
  const register = (newToken: string) => {
    setToken(newToken);
  };

  const contextValue = {
    isAuthenticated,
    token,
    login,
    logout,
    register,
  };

  return (
    <AuthContext.Provider value={contextValue}>
      {children}
    </AuthContext.Provider>
  );
};

// 3. Hook personnalisé pour utiliser le contexte facilement
export const useAuth = () => {
  const context = useContext(AuthContext);
  if (context === undefined) {
    throw new Error('useAuth doit être utilisé à l\'intérieur d\'un AuthProvider');
  }
  return context;
};

