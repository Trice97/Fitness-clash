import React, { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom'; // Ajout de useNavigate
import { useAuth } from '../context/AuthContext'; // Import crucial

const Login = () => {
  const { login } = useAuth(); // Utiliser le hook pour récupérer la fonction 'login'
  const navigate = useNavigate(); // Hook pour la redirection après succès

  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false); // État pour le chargement

  const handleSubmit = async (e: React.FormEvent) => { // Rendre la fonction asynchrone
    e.preventDefault();
    
    setError('');
    setIsLoading(true);

    try {
      // ----------------------------------------------------
      // APPEL API RÉEL (sera décommenté quand Patrice aura fini)
      // ----------------------------------------------------
      
      console.log('Tentative de connexion à l\'API Back-End...');
      
      // *** SIMULATION D'APPEL API EN ATTENDANT PATRICE ***
      await new Promise(resolve => setTimeout(resolve, 1000)); // Simule un délai réseau de 1 seconde
      
      // Ici, le token réel de l'API serait récupéré. Nous utilisons un token bidon.
      const fakeToken = "fake-jwt-token-1234567890"; 
      
      login(fakeToken); // Utilise la fonction du Context pour stocker le token et mettre à jour l'état
      
      alert('Connexion réussie ! Redirection vers le tableau de bord.');
      navigate('/dashboard'); // Redirige vers la page protégée

    } catch (err) {
      setError('Échec de la connexion. Veuillez vérifier vos identifiants.');
    } finally {
      setIsLoading(false);
    }
  };

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
      <h1 style={{ textAlign: 'center', color: '#007BFF' }}>Se Connecter</h1>
      
      {error && (
        <p style={{ color: 'red', textAlign: 'center', fontWeight: 'bold' }}>
          Erreur: {error}
        </p>
      )}

      <form onSubmit={handleSubmit} style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
        
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

        <button 
          type="submit"
          disabled={isLoading}
          style={buttonStyle}
        >
          {isLoading ? 'Connexion en cours...' : 'Connexion'}
        </button>
      </form>
      
      <p style={{ marginTop: '20px', textAlign: 'center' }}>
        Pas encore inscrit ? <Link to="/register" style={{ color: '#007BFF' }}>Créer un compte</Link>
      </p>
    </div>
  );
};

export default Login;

