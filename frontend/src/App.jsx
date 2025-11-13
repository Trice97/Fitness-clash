import React, { useState, useEffect, useCallback } from 'react';
import { initializeApp } from 'firebase/app';
import { 
    getAuth, 
    signInAnonymously, 
    signInWithCustomToken, 
    onAuthStateChanged 
} from 'firebase/auth';
import { 
    getFirestore, 
    doc, 
    setDoc, 
    onSnapshot, 
    setLogLevel
} from 'firebase/firestore';
import { ChevronRight, Save, User, Loader2 } from 'lucide-react';

// Déclaration des variables globales fournies par l'environnement Canvas
// Ceci est le "back-end" de l'environnement qui fournit les clés de connexion.
const appId = typeof __app_id !== 'undefined' ? __app_id : 'default-app-id';
const firebaseConfig = typeof __firebase_config !== 'undefined' 
    ? JSON.parse(__firebase_config) 
    : {};
const initialAuthToken = typeof __initial_auth_token !== 'undefined' 
    ? __initial_auth_token 
    : null;

// Initialisation des instances Firebase pour l'utilisation dans le composant
let app, db, auth;

// Le composant principal de l'application
const App = () => {
    // État d'authentification et utilisateur
    const [userId, setUserId] = useState(null);
    const [isAuthReady, setIsAuthReady] = useState(false);
    
    // État pour la note et le statut
    const [collaborativeNote, setCollaborativeNote] = useState('');
    const [isLoading, setIsLoading] = useState(true);
    const [saveStatus, setSaveStatus] = useState('Prêt');
    
    // --- 1. INITIALISATION FIREBASE ET AUTHENTIFICATION ---
    useEffect(() => {
        try {
            // setLogLevel('debug'); // Commenté pour un affichage en production plus propre
            
            app = initializeApp(firebaseConfig);
            db = getFirestore(app);
            auth = getAuth(app);

            const unsubscribe = onAuthStateChanged(auth, async (user) => {
                if (user) {
                    setUserId(user.uid);
                } else if (!initialAuthToken) {
                    await signInAnonymously(auth);
                } else {
                    await signInWithCustomToken(auth, initialAuthToken);
                }
                setIsAuthReady(true);
                // Si l'authentification est prête, le chargement des données démarrera juste après
            });

            return () => unsubscribe();
        } catch (error) {
            console.error("Erreur lors de l'initialisation Firebase:", error);
            setSaveStatus("Erreur d'initialisation. Voir console.");
            setIsAuthReady(false);
            setIsLoading(false);
        }
    }, []);

    // --- 2. LECTURE EN TEMPS RÉEL (onSnapshot) DE FIRESTORE ---
    useEffect(() => {
        if (!isAuthReady || !db) return;

        // Chemin Public: /artifacts/{appId}/public/data/collaborative_notes/{documentId}
        const documentPath = `artifacts/${appId}/public/data/collaborative_notes/main_document`;
        const docRef = doc(db, documentPath);

        setIsLoading(true);

        const unsubscribeSnapshot = onSnapshot(docRef, 
            (docSnapshot) => {
                if (docSnapshot.exists()) {
                    const data = docSnapshot.data();
                    setCollaborativeNote(data.content || '');
                } else {
                    setCollaborativeNote("Bienvenue ! Commencez à éditer cette note collaborative...");
                }
                setIsLoading(false);
            }, 
            (error) => {
                console.error("Erreur d'écoute en temps réel Firestore:", error);
                setSaveStatus("Erreur de connexion en temps réel.");
                setIsLoading(false);
            }
        );

        return () => unsubscribeSnapshot();
    }, [isAuthReady]);

    // --- 3. FONCTION DE SAUVEGARDE (ÉCRITURE) ---
    const saveNote = useCallback(async () => {
        if (!db || !userId) {
            setSaveStatus("Erreur: Non connecté.");
            return;
        }

        setSaveStatus("Sauvegarde en cours...");
        try {
            const documentPath = `artifacts/${appId}/public/data/collaborative_notes/main_document`;
            const docRef = doc(db, documentPath);

            await setDoc(docRef, {
                content: collaborativeNote,
                lastEditorId: userId,
                timestamp: new Date().toISOString()
            });

            setSaveStatus("Sauvegardé !");
            setTimeout(() => setSaveStatus('Prêt'), 3000); // Retour à l'état initial
        } catch (error) {
            console.error("Erreur lors de la sauvegarde de la note:", error);
            setSaveStatus(`Erreur: ${error.message.substring(0, 40)}...`);
        }
    }, [collaborativeNote, userId]);

    // --- RENDER DE L'INTERFACE UTILISATEUR COHÉRENTE ---
    
    // Déterminer la classe de statut pour la barre inférieure
    const getStatusClass = () => {
        if (saveStatus === 'Sauvegarde en cours...') return 'bg-yellow-500 text-white';
        if (saveStatus === 'Sauvegardé !') return 'bg-green-500 text-white';
        if (saveStatus.includes('Erreur')) return 'bg-red-500 text-white';
        return 'bg-gray-200 text-gray-700';
    };

    return (
        <div className="min-h-screen bg-gray-100 flex justify-center p-4">
            <div className="w-full max-w-4xl flex flex-col h-[85vh] bg-white shadow-2xl rounded-xl overflow-hidden">
                
                {/* En-tête de l'application */}
                <header className="flex items-center justify-between p-4 bg-indigo-600 text-white shadow-lg">
                    <h1 className="text-xl font-bold flex items-center">
                        <ChevronRight className="w-6 h-6 mr-2" /> Note Unique Collaborative
                    </h1>
                    <div className="flex items-center text-sm font-medium bg-indigo-700 px-3 py-1 rounded-full">
                        <User className="w-4 h-4 mr-1.5" /> 
                        {userId ? `Utilisateur: ${userId.substring(0, 8)}...` : 'Connexion...'}
                    </div>
                </header>
                
                {/* Zone de Texte Principale */}
                <div className="flex-grow p-4 overflow-y-auto">
                    {isLoading || !isAuthReady ? (
                        <div className="flex flex-col justify-center items-center h-full text-indigo-600">
                            <Loader2 className="animate-spin h-8 w-8 mb-3" />
                            <p className="text-lg font-semibold">
                                Connexion à Firestore et chargement de la note...
                            </p>
                        </div>
                    ) : (
                        <textarea
                            value={collaborativeNote}
                            onChange={(e) => setCollaborativeNote(e.target.value)}
                            rows="10"
                            className="w-full h-full p-2 border-none resize-none focus:ring-0 text-gray-800 font-sans leading-relaxed text-base"
                            placeholder="Commencez à écrire ici. Vos modifications seront partagées instantanément."
                            disabled={!userId || isLoading}
                        ></textarea>
                    )}
                </div>

                {/* Pied de page et Actions */}
                <footer className={`flex items-center justify-between p-3 border-t-2 transition-colors duration-300 ${getStatusClass()}`}>
                    <p className="text-sm font-medium flex items-center">
                        <span className="mr-2">Statut:</span>
                        {saveStatus === 'Sauvegarde en cours...' && <Loader2 className="animate-spin h-4 w-4 mr-1" />}
                        {saveStatus}
                    </p>

                    <button
                        onClick={saveNote}
                        disabled={!userId || isLoading || saveStatus === 'Sauvegarde en cours...'}
                        className={`px-4 py-2 rounded-lg font-semibold text-white transition-all duration-200 shadow-md flex items-center 
                            ${!userId || isLoading ? 'bg-gray-500 cursor-not-allowed' : 'bg-indigo-700 hover:bg-indigo-800 active:scale-[0.98]'}`
                        }
                    >
                        <Save className="w-4 h-4 mr-2" />
                        {saveStatus === 'Sauvegarde en cours...' ? 'Sauvegarde...' : 'Sauvegarder'}
                    </button>
                </footer>
            </div>
        </div>
    );
};

export default App;

