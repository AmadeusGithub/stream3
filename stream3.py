import streamlit as st
import streamlit_authenticator as stauth

# Définition des données des comptes
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attempts': 0,
            'logged_in': False,
            'role': 'administrateur'
        }
    }
}

# Initialisation de l'authentificateur
authenticator = stauth.Authenticate(
    lesDonneesDesComptes['usernames'],  # Passe directement le dictionnaire des utilisateurs
    "cookie_name",                      # Nom du cookie
    "cookie_key",                       # Clé du cookie
    30                                  # Durée d'expiration (jours)
)

# Affichage du formulaire de connexion
name, authentication_status, username = authenticator.login('Login', 'main')

# Gestion du statut d'authentification
if authentication_status:
    st.write(f"Bienvenue, {name} !")
    authenticator.logout('Logout', 'sidebar')  # Bouton de déconnexion
elif authentication_status == False:
    st.error("Nom d'utilisateur ou mot de passe incorrect")
elif authentication_status == None:
    st.warning("Veuillez entrer vos identifiants")
