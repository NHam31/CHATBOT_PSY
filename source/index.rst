.. PsyBot Documentation master file, created by
   sphinx-quickstart on Sat Dec 29 2024.
   You can adapt this file completely to your liking, but it should at least contain
   the root `toctree` directive.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   introduction
   fonctionnalites
   prerequis
   installation
   collecte_de_donnees
   detection_emotions
   generation_recommandations
   modele_de_langage
   reponse_chatbot
   historique_chatbot
   affichage
   interface_streamlit
   conclusion


Introduction
============

Ce projet est un chatbot psychologique développé pour aider les utilisateurs à identifier et à gérer leurs émotions, principalement en détectant des troubles comme le stress, l'anxiété, la dépression, et les difficultés d'adaptabilité. Il offre des recommandations personnalisées telles que des vidéos et des exercices de relaxation, ainsi que des conseils pratiques pour améliorer le bien-être mental.

Fonctionnalités
===============
Le chatbot offre plusieurs fonctionnalités pour soutenir les utilisateurs dans la gestion de leurs émotions, notamment :
- Détection des émotions à partir de l'entrée utilisateur.
- Génération de recommandations de vidéos et exercices basées sur les émotions détectées.
- Interaction en temps réel avec l'utilisateur via une interface Streamlit.
- Historique des interactions pour suivre l'évolution du bien-être de l'utilisateur.

Prérequis
==========
Avant de pouvoir exécuter ce projet, assurez-vous que les éléments suivants sont installés :
- Python 3.8+
- Streamlit
- Langchain
- Ollama (modèle Llama 3.2):
- Autres bibliothèques nécessaires : `difflib`, `random`, etc.

Installation
============
- Clonez le dépôt du projet :
  .. code-block:: python
      git clone https://github.com/votre-utilisateur/chatbot-psy.git
      cd chatbot-psy
- Installez les dépendances nécessaires :
  .. code-block:: python
   pip install python
   pip install streamlit
   pip install OllamaLLM
   pip install langchain_ollama
   pip install difflib
   
  .. code-block:: python
   import streamlit as st
   from langchain_ollama import OllamaLLM
   import difflib
   import random
- Lancez l'application Streamlit :
.. code-block:: python
   streamlit run chatbot_psy.py

Collecte de données
===================
Les données utilisées dans ce projet comprennent des vidéos, des exercices, et des ressources pour chaque émotion ciblée (stress, anxiété, dépression, etc.). Ces ressources sont soigneusement sélectionnées pour offrir un soutien pertinent aux utilisateurs.

Détection des émotions
======================
Le chatbot détecte plusieurs émotions en analysant le texte entré par l'utilisateur. À l'aide de mots-clés spécifiques pour chaque émotion (stress, dépression, anxiété, et adaptabilité), le système utilise la fonction `detect_and_recommend_emotions` pour identifier les émotions présentes dans le message de l'utilisateur.
.. code-block:: python
   def detect_and_recommend_emotions(response):
      keywords = {
         "stress": ["stressé", "stress"],
         "depression": ["déprimé", "triste", "sans espoir"],
         "anxiety": ["anxiété", "angoisse", "peur"],
         "adaptability": ["changement", "adaptabilité"]
      }
    detected_emotions = []
    for category, terms in keywords.items():
        for term in terms:
            if term in response.lower():
                detected_emotions.append(category)
    return detected_emotions

Génération des recommandations aléatoires
===========================================
Une fois les émotions détectées, le système génère des recommandations personnalisées. Cela inclut des vidéos et des exercices tirés d'une base de données préétablie. Les vidéos et exercices sont choisis de manière aléatoire pour fournir une variété d'options aux utilisateurs.
.. code-block:: python 
   def get_random_resources(emotion):
      if emotion in resources:
        resource = resources[emotion]
        selected_videos = []
        selected_exercises = []
         if "videos" in resource:
            for category, items in resource["videos"].items():
                selected_videos.extend(random.sample(items, min(2, len(items))))
         if "exercise" in resource:
            selected_exercises = random.sample(resource["exercise"], min(3, len(resource["exercise"])))
         return selected_videos, selected_exercises
      return [], []

Modèle de langage
=================
Le modèle de langage utilisé est le modèle Llama 3.2 d'Ollama, qui permet d'analyser le texte et de générer des réponses pertinentes. Le modèle est chargé via la bibliothèque Langchain et utilise l'API d'Ollama pour fournir des réponses basées sur le contexte de l'utilisateur.
.. code-block:: python 
   def get_model():
    return OllamaLLM(model="llama3.2")

Réponse Chatbot
===============
Le chatbot génère une réponse complète qui inclut une analyse de l'émotion de l'utilisateur ainsi que des recommandations pratiques. La réponse est ensuite envoyée à l'utilisateur via l'interface Streamlit.

Historique Chatbot
==================
Toutes les interactions entre l'utilisateur et le chatbot sont enregistrées dans l'historique de la session. Cela permet à l'utilisateur de revoir ses conversations précédentes et d'observer les tendances de son bien-être au fil du temps.
.. code-block:: python
         if 'history' not in st.session_state:
            st.session_state.history = []  

Affichage
=========
Les réponses du chatbot sont affichées à l'utilisateur dans un format lisible via Streamlit. Les vidéos et exercices recommandés sont fournis avec des liens cliquables. L'historique des messages est également affiché pour permettre une vue d'ensemble des échanges.
- Afficher la réponse du chatbot après la saisie de l'utilisateur:
    .. code-block:: python
      if user_input:
         st.write(f"### Chatbot :")
         st.write(response)

- Afficher l'historique
   .. code-block:: python
      st.write("### Historique de la conversation :")
      for message in st.session_state.history:
         st.write(message) 

Interface STREAMLIT
===================
L'interface utilisateur est développée à l'aide de Streamlit. Elle permet une interaction facile et fluide avec le chatbot. L'utilisateur peut entrer ses messages, consulter les réponses du chatbot, et explorer les recommandations sous forme de vidéos et d'exercices.
.. code-block:: python
    st.title("Chatbot PSY 🌼")
    # Introduction
    st.write("Bonjour ! Je suis Psy, votre chatbot bien-être. Comment puis-je vous aider aujourd'hui ?")
    # Initialisation de 'input' dans session_state si elle n'existe pas
    if 'area' not in st.session_state:
        st.session_state.area = ""  # Initialisation à une chaîne vide

    # Zone de saisie de texte pour l'utilisateur
    user_input = st.text_area("Vous : ", value=st.session_state.area, key="input_box")
    # Informations complémentaires
        st.sidebar.title("À propos")
        st.sidebar.info(
            """
            Ce chatbot est conçu pour vous aider à identifier les problèmes liés aux émotions et à fournir des conseils utiles. 
            Veuillez noter que ce chatbot ne remplace pas un professionnel de la santé mentale.
            """
        )

Conclusion
==========
Ce chatbot fournit un soutien émotionnel accessible et personnalisé pour les utilisateurs en fonction de leurs émotions. Il combine des techniques d'analyse de texte, des recommandations basées sur des ressources variées, et une interface interactive pour améliorer le bien-être mental des étudiants et de toute autre personne cherchant du soutien.


