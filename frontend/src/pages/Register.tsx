import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext'; // Import crucial

const Register = () => {
  const { register } = useAuth(); // Utiliser le hook pour récupérer la fonction 'register'
  const navigate = useNavigate();

  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setIsLoading(true);

    if (password !== confirmPassword) {
      setError('Les mots de passe ne correspondent pas.');
      setIsLoading(false);
      return;
    }

    // --- LOGIQUE D'APPEL API RÉEL ---
    
    try {
      console.log('Tentative d\'inscription à l\'API Back-End...');
      
      // *** SIMULATION D'APPEL API EN ATTENDANT PATRICE ***
      await new Promise(resolve => setTimeout(resolve, 1500)); 

      // Ici, le token réel de l'API serait récupéré. Nous utilisons un token bidon.
      const fakeToken = "fake-jwt-token-after-register-987654321"; 

      register(fakeToken); // Utilise la fonction du Context pour connecter immédiatement
      
      alert('Inscription réussie ! Connexion automatique et redirection vers le tableau de bord.');
      navigate('/dashboard');

    } catch (err) {
      setError('Échec de l\'inscription. L\'utilisateur existe peut-être déjà.');
    } finally {
      setIsLoading(false);
    }
  };

  // Styles... (les mêmes que dans Login.tsx pour la cohérence)
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
    cursor: isLoading ? 'not-allowed' : 'pointer',
    marginTop: '10px',
    opacity: isLoading ? 0.7 : 1
  };

  return (
    <div style={{ maxWidth: '400px', margin: '50px auto', padding: '20px', border: '1px solid #ccc', borderRadius: '8px', boxShadow: '0 4px 6px rgba(0,0,0,0.1)' }}>
      <h1 style={{ textAlign: 'center', color: '#007BFF' }}>Inscription - Nouveau Compte</h1>
      
      {error && (
        <p style={{ color: 'red', textAlign: 'center', fontWeight: 'bold' }}>
          Erreur: {error}
        </p>
      )}

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        
        <input
          type="text"
          placeholder="Nom d'utilisateur"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          required
          disabled={isLoading}
          style={inputStyle}
        />
        
        <input
          type="email"
          placeholder="Adresse Email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          required
          disabled={isLoading}
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Mot de passe"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          required
          disabled={isLoading}
          style={inputStyle}
        />

        <input
          type="password"
          placeholder="Confirmer le mot de passe"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
          required
          disabled={isLoading}
          style={inputStyle}
        />

        <button 
          type="submit"
          disabled={isLoading}
          style={buttonStyle}
        >
          {isLoading ? 'Inscription en cours...' : 'S\'inscrire'}
        </button>
      </form>
      
      <p style={{ marginTop: '20px', textAlign: 'center' }}>
        Vous avez déjà un compte ? <Link to="/login" style={{ color: '#007BFF' }}>Connectez-vous ici</Link>
      </p>
    </div>
  );
};

export default Register;

