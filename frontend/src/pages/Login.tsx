import React from 'react';
import { Link } from 'react-router-dom';

const Login = () => {
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      <h1>Connexion</h1>
      <p>Formulaire de connexion (Email et Mot de passe)</p>
      <button onClick={() => alert('Simuler connexion')}>Se connecter</button>
      <p style={{ marginTop: '20px' }}>
        Pas encore inscrit ? <Link to="/register">Créer un compte</Link>
      </p>
    </div>
  );
};

export default Login;
