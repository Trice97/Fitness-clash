import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const Register = () => {
  // 1. Déclaration des états pour chaque champ du formulaire
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState(''); // Pour afficher les messages d'erreur

  // 2. Fonction appelée lors de la soumission du formulaire
  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault(); // Empêche le rechargement de la page

    // Validation simple (Vérification Front-End)
    if (password !== confirmPassword) {
      setError('Les mots de passe ne correspondent pas.');
      return;
    }
    
    setError(''); // Réinitialise l'erreur

    // --- LOGIQUE D'APPEL API (Tâche 2.1 - Action 4) ---
    // C'est ici que nous enverrons : username, email, password
    console.log('Données d\'inscription prêtes à être envoyées (simulé) :');
    console.log({ username, email, password });

    alert('Inscription simulée réussie ! Vérifiez la console.');
    // Après le succès, nous redirigerons l'utilisateur vers /login ou /dashboard
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
      <h1 style={{ textAlign: 'center', color: '#007BFF' }}>Créer un Compte</h1>
      
      {/* Affichage des erreurs si l'état 'error' est rempli */}
      {error && (
        <p style={{ color: 'red', textAlign: 'center', fontWeight: 'bold' }}>
          Erreur: {error}
        </p>
      )}

      {/* Le formulaire géré par React */}
      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        
        <input
          type="text"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          style={inputStyle}
        />

        <input
          type="email"
          placeholder="Adresse Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Confirmer le Mot de passe"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
          style={inputStyle}
        />

        <button 
          type="submit"
          style={buttonStyle}
        >
          S'inscrire
        </button>
      </form>
      
      <p style={{ marginTop: '20px', textAlign: 'center' }}>
        Déjà un compte ? <Link to="/login" style={{ color: '#007BFF' }}>Connectez-vous</Link>
      </p>
    </div>
  );
};

// Styles rapides pour la lisibilité
const inputStyle: React.CSSProperties = {
  padding: '10px',
  borderRadius: '4px',
  border: '1px solid #ccc',
  fontSize: '16px'
};

const buttonStyle: React.CSSProperties = {
  padding: '12px',
  backgroundColor: '#007BFF',
  color: 'white',
  border: 'none',
  borderRadius: '4px',
  fontSize: '16px',
  cursor: 'pointer',
  marginTop: '10px'
};

export default Register;

