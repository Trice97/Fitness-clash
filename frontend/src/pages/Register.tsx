import React from 'react';
import { Link } from 'react-router-dom';

const Register = () => {
  return (
    <div style={{ padding: '20px', textAlign: 'center' }}>
      {/* Titre et Formulaire (Squelette en attendant l'API) */}
      <h1>Inscription - Nouveau Compte</h1>
      <p>Ici, le formulaire d'inscription (qui appellera POST /api/auth/register).</p>
      
      {/* Espace pour les futurs champs : Username, Email, Password et confirmation */}
      <div style={{ margin: '30px 0' }}>
        <p>— Futurs champs de formulaire ici —</p>
      </div>

      <button 
        onClick={() => alert('Simuler inscription')}
        style={{ padding: '10px 20px', backgroundColor: '#4CAF50', color: 'white', border: 'none', borderRadius: '5px', cursor: 'pointer' }}
      >
        Créer mon compte
      </button>
      
      {/* Lien vers la page de connexion */}
      <p style={{ marginTop: '20px' }}>
        Vous avez déjà un compte ? <Link to="/login" style={{ color: '#007BFF' }}>Connectez-vous ici</Link>
      </p>
    </div>
  );
};

export default Register;

