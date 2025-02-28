import pandas as pd
import matplotlib as plt
import seaborn as sns
import streamlit as st
from streamlit_authenticator import Authenticate
from streamlit_option_menu import option_menu

# Nos données utilisateurs doivent respecter ce format
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'utilisateur'
        },
        'root': {
            'name': 'root',
            'password': 'rootMDP',
            'email': 'admin@gmail.com',
            'failed_login_attemps': 0,  # Sera géré automatiquement
            'logged_in': False,  # Sera géré automatiquement
            'role': 'administrateur'
        }
    }
}

authenticator = Authenticate(
    lesDonneesDesComptes,  # Les données des comptes
    "cookie name",  # Le nom du cookie, un str quelconque
    "cookie key",  # La clé du cookie, un str quelconque
    30,  # Le nombre de jours avant que le cookie expire 
)

# Methode pour afficher les champs
authenticator.login()

def accueil():
    st.title("Bienvenu sur mon service de produits de soins naturels")
    st.image("https://th.bing.com/th/id/OIP.Sc73CNz3g0TnfaxljGQkBwHaEK?rs=1&pid=ImgDetMain")

    # Using "with" notation
    with st.sidebar:
        # Ajout du bouton de déconnexion dans la barre latérale
        if st.session_state["authentication_status"]:
            authenticator.logout("Déconnexion")
        
        # Coche choix de l'envois
        add_radio = st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )

        # Création du menu qui va afficher les choix qui se trouvent dans la variable options
        selection = option_menu(
            menu_title=None,
            options=["Soins chat", "Soins chien", "Soins catcheur"]
        )

    # Affichage de l'image correspondante en fonction de la sélection
    if selection == "Soins chat":
        st.header("Soins chat")
        st.image("https://static.streamlit.io/examples/cat.jpg")
    elif selection == "Soins chien":
        st.header("Soins chien")
        st.image("https://static.streamlit.io/examples/dog.jpg")
    elif selection == "Soins catcheur":
        st.header("Soins catcheur")
        st.image("https://www.wwe.com/f/all/2019/04/132_SD_04232019ca_3144--ca4e6a0f0a79d2cf3c3bf6231e7470e7.jpg")


if st.session_state["authentication_status"]:
    accueil()

elif st.session_state["authentication_status"] is False:
    st.error("L'username ou le password est/sont incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Les champs username et mot de passe doivent être remplis')