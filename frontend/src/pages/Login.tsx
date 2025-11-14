// src/pages/Login.tsx
 

import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

const API_BASE_URL = "http://localhost:8000";

const Login: React.FC = () => {
    const { login } = useAuth();
    const navigate = useNavigate();

    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [isLoading, setIsLoading] = useState(false);

    const [error, setError] = useState<string | null>(null);

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setError(null);
        setIsLoading(true);

        const formBody = new URLSearchParams();
        formBody.append("username", username);
        formBody.append("password", password);

        try {
            const response = await fetch(`${API_BASE_URL}/api/auth/login`, {
                method: "POST",
                headers: {
                    "Content-Type": "application/x-www-form-urlencoded",
                },
                body: formBody.toString(),
            });

            const data = await response.json();

            if (response.ok && data.access_token) {
                login(data.access_token); // >>> STOCKE LE TOKEN ET TRIGGER fetchUser()
                navigate("/dashboard"); // redirection après login réussi
            } else {
                setError(data.detail || "Identifiants incorrects.");
            }
        } catch (err) {
            console.error("Erreur réseau :", err);
            setError("Impossible de contacter le serveur.");
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div style={containerStyle}>
            <h1 style={titleStyle}>Connexion</h1>

            {error && <div style={errorMessageStyle}>{error}</div>}

            <form onSubmit={handleSubmit} style={formStyle}>
                <label style={labelStyle}>Nom d’utilisateur</label>
                <input
                    type="text"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    placeholder="Votre nom d'utilisateur"
                    required
                    style={inputStyle}
                />

                <label style={labelStyle}>Mot de passe</label>
                <input
                    type="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    placeholder="Votre mot de passe"
                    required
                    style={inputStyle}
                />

                <button type="submit" disabled={isLoading} style={buttonStyle}>
                    {isLoading ? "Connexion..." : "Se connecter"}
                </button>
            </form>

            <p style={linkTextStyle}>
                Pas de compte ?
                <Link to="/register" style={linkStyle}> Créer un compte</Link>
            </p>
        </div>
    );
};

// === Styles ===

const containerStyle: React.CSSProperties = {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    justifyContent: "center",
    minHeight: "100vh",
    backgroundColor: "#1C1C1E",
    color: "white",
    padding: "20px",
};

const titleStyle: React.CSSProperties = {
    fontSize: "32px",
    fontWeight: "bold",
    marginBottom: "40px",
};

const formStyle: React.CSSProperties = {
    display: "flex",
    flexDirection: "column",
    width: "100%",
    maxWidth: "350px",
};

const labelStyle: React.CSSProperties = {
    marginBottom: "8px",
    fontSize: "16px",
};

const inputStyle: React.CSSProperties = {
    padding: "14px",
    marginBottom: "20px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#383838",
    color: "white",
};

const buttonStyle: React.CSSProperties = {
    padding: "15px",
    borderRadius: "8px",
    border: "none",
    backgroundColor: "#FF3B3F",
    color: "white",
    fontSize: "18px",
    cursor: "pointer",
};

const errorMessageStyle: React.CSSProperties = {
    padding: "10px",
    marginBottom: "20px",
    backgroundColor: "rgba(220, 53, 69, 0.2)",
    color: "#dc3545",
    borderRadius: "4px",
    textAlign: "center",
};

const linkTextStyle: React.CSSProperties = {
    marginTop: "20px",
    color: "#A0A0A0",
};

const linkStyle: React.CSSProperties = {
    color: "#FF3B3F",
    marginLeft: "5px",
    fontWeight: "bold",
};

export default Login;
