import React from "react";
import { useNavigate } from "react-router-dom";
import { useAuth } from "../contexts/AuthContext";

const Dashboard = () => {
    const navigate = useNavigate();
    const { user, isAuthenticated, isLoading, logout } = useAuth();

    if (isLoading) {
        return <p style={{ textAlign: "center", padding: "20px" }}>Chargement...</p>;
    }

    if (!isAuthenticated || !user) {
        navigate("/login");
        return null;
    }

    return (
        <div style={{ padding: "20px", textAlign: "center" }}>
            <h1>Tableau de bord de {user.username}</h1>

            <div style={{ marginTop: "20px" }}>
                <p><strong>Email :</strong> {user.email}</p>
                <p><strong>Niveau :</strong> {user.difficulty_level}</p>
                <p><strong>Points cumulés :</strong> {user.total_points}</p>
            </div>

            <button onClick={logout} style={{ marginTop: "20px" }}>
                Se déconnecter
            </button>
        </div>
    );
};

export default Dashboard;
