import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Données des comptes (structure correcte pour streamlit-authenticator)
credentials = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',  # Mot de passe en clair (sera haché si nécessaire)
            'email': 'utilisateur@gmail.com'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com'
        }
    }
}

# Initialisation de l'authentificateur
authenticator = Authenticate(
    credentials,           # Passe le dictionnaire complet avec 'usernames'
    "cookie_name",        # Nom du cookie
    "cookie_key",         # Clé du cookie
    30                    # Durée d'expiration (jours)
)

# Affichage du formulaire de connexion
name, authentication_status, username = authenticator.login('Login', 'main')

# Fonction pour la page d'accueil
def accueil():
    st.title("Bienvenu sur mon service de produits de soins naturels")
    st.image("https://th.bing.com/th/id/OIP.Sc73CNz3g0TnfaxljGQkBwHaEK?rs=1&pid=ImgDetMain")

    with st.sidebar:
        if st.session_state["authentication_status"]:
            authenticator.logout("Déconnexion", "sidebar")
        
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

        selection = option_menu(
            menu_title=None,
            options=["Soins chat", "Soins chien", "Soins catcheur"]
        )

    if selection == "Soins chat":
        st.header("Soins chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    elif selection == "Soins chien":
        st.header("Soins chien")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    elif selection == "Soins catcheur":
        st.header("Soins catcheur")
        st.image("https://www.wwe.com/f/all/2019/04/132_SD_04232019ca_3144--ca4e6a0f0a79d2cf3c3bf6231e7470e7.jpg")

# Gestion de l'état d'authentification
if authentication_status:
    accueil()
elif authentication_status is False:
    st.error("L'username ou le password est/sont incorrect")
elif authentication_status is None:
    st.warning("Les champs username et mot de passe doivent être remplis")
