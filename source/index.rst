.. CHATBOT_PSY documentation master file, created by
   sphinx-quickstart on Sun Dec 29 17:18:55 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to CHATBOT_PSY documentation
======================================

Bienvenue dans la documentation officielle du projet Chatbot PSY. Cette application Streamlit interactive est conçue pour aider les utilisateurs 
à mieux comprendre leurs émotions et à améliorer leur bien-être mental.

* Table des matières *
  - introduction
  - Fonctionnalités
  - Prérequis
  - installation
  - Collecte de donnees
  - Detection des émotions
  - Generation des recommandations aléatoires
  - Modèle de langage
  - Reponse Chatbot
  - Historique Chatbot
  - Affichage
  - Interface STREAMLIT 
  - Conclusion

Introduction
==================
Le Chatbot PSY est capable de détecter des émotions comme le stress, la dépression, l'anxiété et les difficultés d'adaptabilité, puis de recommander des ressources adaptées. 
L’application propose des vidéos, des exercices de relaxation, et d'autres conseils personnalisés pour aider les utilisateurs à gérer leurs émotions.

Fonctionnalités
==================

Détection d'émotions
=================

Le chatbot analyse les messages de l’utilisateur pour identifier les émotions suivantes :

. Stress

. Dépression

. Anxiété

. Adaptabilité

Recommandations personnalisées
=================

En fonction des émotions détectées, le chatbot propose :

. Des exercices de respiration et de relaxation.

. Des vidéos de motivation et de méditation.

. Des techniques pour améliorer la gestion du stress et de l’anxiété.

Interface intuitive
=================

L'application offre une interface simple via Streamlit permettant aux utilisateurs de :

Discuter avec le chatbot.
=================

Recevoir des recommandations adaptées.

Consulter l’historique de conversation.

Modèle de langage avancé
=================

Le chatbot intègre le modèle llama3.2 via OllamaLLM pour fournir des réponses précises et pertinentes.

Prérequis
==================

Langages et outils requis :
==============

Python 3.8+

Streamlit

LangChain

OllamaLLM

Installation des dépendances :
==============
Un fichier requirements.txt est fourni pour installer toutes les bibliothèques nécessaires.,

Installation
==================
Les bibliothèques suivantes sont nécessaires pour le projet :
   
  1. streamlit : Développer rapidement des applications web interactives pour partager des modèles et des analyses.
  2. OllamaLLM :
  3. langchain_ollama:
  4. difflib:
  5. random:

.. code-block:: python
   import streamlit as st
   from langchain_ollama import OllamaLLM
   import difflib
   import random

* Collecte de donnees * :
   ==================
   Pour la collecte du donnees, on a introduit de differentes videos et exercices adaptees aux differentes troubles.
   Le fichier 'resources/resources.json' contient des vidéos et des exercices de relaxation et de méditation. 
   Il est utilisé pour fournir des recommandations personnalisées.
.. code-block:: python
   resources = {
      "stress": {
         "videos": {
               "respiration": [
                  "https://youtu.be/7jKUxl_2Lfs?si=V7FejJbSMPvwsGNL",
                  "https://youtu.be/DfJtdQ4FCaw?si=zv4fVSdFTawvEQ4g",
                  "https://youtu.be/5tBtaK4fAdA?si=GDzZyYAVqjq0qm5r",
                  "https://youtu.be/CK6OMG_5LMQ?si=63K7w5hi17KXCLBe",
                  "https://youtu.be/nAzPZG6h_S8?si=GiNPFp39xyZLzyHS"
               ],
               "meditation": [
                  "https://youtu.be/bQoOev5GNYM?si=gpd9Qiw26BGdYuXv",
                  "https://youtu.be/EL6gQWo_aSM?si=m1zrqT3jbTwD2MYE",
                  "https://youtu.be/5bxBcbkSrtY?si=wL4UfW0oTQq3PmEt",
                  "https://youtu.be/sbivsrlopOw?si=JVS_5_cJezRSdMb_",
                  "https://youtu.be/Zz1MH0nfS1U?si=NDAERbcJxybCSZ-j"
               ],
               "yoga": [
                  "https://youtu.be/ra1buV7Wi5M?si=oWe4w7wMA_IWo4Ub",
                  "https://youtu.be/kyyVPp3iNEs?si=bfxULbgo-_RjckF5",
                  "https://youtu.be/8z_40RD1pQU?si=i6T8xqtmzm79puXc",
                  "https://youtu.be/Ecq4xvL1c5c?si=rYzEAVyH1dLL6MG7",
                  "https://youtu.be/sd49ER2kF2M?si=cfeDn7i7BWcgJZfY",
                  "https://youtu.be/yNdKHEHRGpg?si=nbZFG_mrIYnhV_su",
                  "https://youtu.be/XwCGrtfh7J0?si=GVSCb3lIoH_e4yWq"
               ]
         },
         "exercise": [
               "Respiration 4-7-8 : Inspirez 4 secondes, retenez votre souffle 7 secondes, expirez lentement pendant 8 secondes.",
               "Étirement corporel : Faites des étirements doux pour relâcher les tensions musculaires.",
               "Relaxation progressive : Contractez et relâchez chaque groupe musculaire, en partant des orteils jusqu'à la tête.",
               "Visualisation positive : Imaginez un endroit calme et relaxant, comme une plage ou une montagne.",
               "Exercice d'ancrage : Concentrez-vous sur vos cinq sens pour revenir au moment présent.",
               "Écoute de sons apaisants : Écoutez des bruits de la nature, comme le son de la pluie ou des vagues.",
               "Jardinage ou soin des plantes : Prenez soin de plantes ou de fleurs pour apaiser votre esprit.",
               "Journal de stress : Écrivez ce qui vous stresse et proposez-vous des solutions réalistes.",
               "Pause numérique : Éloignez-vous des écrans pendant 30 minutes.",
               "Boisson relaxante : Préparez une infusion de camomille ou une tisane apaisante."
         ]
      },
      "depression": {
         "videos": {
               "motivation": {
                  "en francais": [
                     "https://youtu.be/IpubFyxxz04?si=Fbz2HmyDtXqh9JiW",
                     "https://youtu.be/lcylR1ki2RA?si=c1RfaciEdFjntZ9j",
                     "https://youtu.be/oiIqZS85xho?si=5QNAIhPkuqWXAV8Q",
                     "https://youtu.be/NIi9zddDov4?si=OquhbWJRJxps5PCl",
                     "https://youtu.be/_g-cXUbEduM?si=YVtGfZDvFG5UiJ6g"
                  ],
                  "en arabe": [
                     "https://youtu.be/9oPW3ydDIE4?si=WWkrZeiXbgRK_bFv",
                     "https://youtu.be/uWdn0cL4HHQ?si=vC4_HnyFXeYUXvyv",
                     "https://youtu.be/igIdKdjU5WE?si=dfpgN5uC0Skrymkc"
                  ]
               }
         },
         "exercise": [
               "Prenez une promenade de 10 minutes à l'extérieur pour vous connecter avec la nature.",
               "Écriture positive : Notez trois choses positives qui se sont passées dans la journée.",
               "Respiration diaphragmatique : Inspirez profondément en gonflant votre ventre, puis expirez lentement.",
               "Exercice de gratitude : Écrivez une lettre ou un message à quelqu'un pour exprimer votre gratitude.",
               "Méditation guidée : Suivez une vidéo de méditation pour la relaxation.",
               "Contact social : Appelez ou envoyez un message à un ami ou un proche.",
               "Routine matinale : Réveillez-vous à une heure fixe et commencez votre journée avec un rituel positif.",
               "Exposition au soleil : Passez 10 à 15 minutes dehors pour stimuler votre production de vitamine D."
         ]
      },
      "anxiety": {
         "videos": {
               "relaxation": [
                  "https://youtu.be/l4fQ0GA1oOI?si=owBoZgsVwqMhUjCG",
                  "https://youtu.be/Ufohfe3PeRM?si=pJCT2WRk4h6SnF2e",
                  "https://youtu.be/E2_VV0dwqDU?si=-6j3upbD6X1Xx2jF",
                  "https://youtu.be/nVqQO93RQxY?si=4eVKSon867lwteU1",
                  "https://youtu.be/3nyQpBu2BSc?si=JJb3Po2oAiHnBOZZ",
                  "https://youtu.be/Zz1MH0nfS1U?si=NDAERbcJxybCSZ-j",
                  "https://youtu.be/nAzPZG6h_S8?si=GiNPFp39xyZLzyHS"
               ],
               "yoga": [
                  "https://youtu.be/ra1buV7Wi5M?si=oWe4w7wMA_IWo4Ub",
                  "https://youtu.be/kyyVPp3iNEs?si=bfxULbgo-_RjckF5",
                  "https://youtu.be/8z_40RD1pQU?si=i6T8xqtmzm79puXc",
                  "https://youtu.be/Ecq4xvL1c5c?si=rYzEAVyH1dLL6MG7",
                  "https://youtu.be/sd49ER2kF2M?si=cfeDn7i7BWcgJZfY",
                  "https://youtu.be/yNdKHEHRGpg?si=nbZFG_mrIYnhV_su",
                  "https://youtu.be/XwCGrtfh7J0?si=GVSCb3lIoH_e4yWq"
               ]
         },
         "exercise": [
               "Respiration en carré : Inspirez 4 secondes, retenez votre souffle 4 secondes, expirez 4 secondes, puis restez en pause 4 secondes.",
               "Observation des pensées : Notez vos pensées anxieuses et remplacez-les par des affirmations positives.",
               "Défi cognitif : Posez-vous des questions sur la probabilité que vos peurs se réalisent vraiment.",
               "Écriture des peurs : Écrivez vos craintes sur une feuille, puis déchirez-la symboliquement.",
               "Marche lente : Marchez lentement en étant attentif à vos pas et à votre respiration.",
               "Yoga pour débutants : Faites une courte séance de yoga pour calmer l’esprit et détendre le corps.",
               "Objets réconfortants : Tenez un objet doux ou réconfortant, comme une couverture ou un oreiller.",
               "Planification : Faites une liste de tâches pour organiser votre journée et réduire l'incertitude.",
               "Pause sensuelle : Sentez un parfum agréable ou écoutez une musique relaxante pour calmer votre esprit.",
               "Affirmations positives : Répétez des phrases comme : 'Je peux gérer cela', 'Je suis en sécurité'."
         ]
      },
      "adaptability": {
         "categories": {
               "soft skills": [
                  "https://youtu.be/xJM_CQN8-ns?si=xxfPJeNiF1Iq18Lw",
                  "https://youtu.be/eSX-Kuo4ulw?si=wlDe54qMNsNBlZTy",
                  "https://youtu.be/0g3IotDlSSY?si=IVNQW3dcDqFGz3nT"
               ]
         }
      }
   }

* Detection des émotions * :
   ==================
   Analyse les messages utilisateur pour détecter les émotions associées :
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

* Generation des recommandations aléatoires * :
==================  
Sélectionne des ressources adaptées aux émotions détectées :
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

* Modèle de langage * :
==================
Récupère le modèle de langage pour générer des réponses :
.. code-block:: python 
   def get_model():
    return OllamaLLM(model="llama3.2")
   
* CHAT * :
==================
la fonction chat permet d'implémenter un chatbot de bien-être émotionnel à l'aide de Streamlit. Son objectif est de fournir une interface utilisateur interactive où les utilisateurs peuvent poser des questions, exprimer leurs émotions, et recevoir des réponses adaptées, accompagnées de recommandations pour améliorer leur bien-être.
elle comporte les fonctions suivantes:

   1-  Initialisation de la session
   ==================================
      Configure l’état de la session utilisateur :
      .. code-block:: python
         def initialize_session():
            if "messages" not in st.session_state:
               st.session_state.messages = []
            if "user_input" not in st.session_state:
               st.session_state.user_input = ""
            

   2-  Historique du Chatbot:
   ================================== 
      la Variable "history" permet de stocker les messages entre l'utilisateur et le chat.
      .. code-block:: python
         if 'history' not in st.session_state:
            st.session_state.history = []  
            
   2- Reponse Chatbot:
   ================================== 
      le code suivant permet de generer de la reponse du chatbot(conseils+recommandations)
   .. code-block:: python
      # Détection et recommandations basées sur plusieurs émotions
        detected_emotions = detect_and_recommend_emotions(user_input)  # Retourne une liste d'émotions
        if detected_emotions:
            for emotion in detected_emotions:
                if emotion in resources:  # Vérifie si l'émotion a des ressources associées
                    resource = resources[emotion]
                
                    # Sélection de 2-3 vidéos et exercices aléatoires pour chaque catégorie
                    recommendations = f"\n\n### Recommandations pour l'émotion : {emotion.capitalize()}\n"
                    
                    for category, items in resource.get("videos", {}).items():
                        selected_videos = random.sample(items, min(2, len(items)))
                        recommendations += f"- **{category.capitalize()}**: " + ", ".join(
                            f"[Vidéo {i+1}]({url})" for i, url in enumerate(selected_videos)
                        ) + "\n"
                    
                    selected_exercises = random.sample(
                        resource.get("exercise", []), 
                        min(2, len(resource.get("exercise", [])))
                    )
                    recommendations += "- **Exercices**: " + ", ".join(selected_exercises) + "\n"

                    response += recommendations

   Affichage
   ===============
   1- Afficher la réponse du chatbot après la saisie de l'utilisateur:
    .. code-block:: python
      if user_input:
         st.write(f"### Chatbot :")
         st.write(response)

   2- Afficher l'historique
   .. code-block:: python
      st.write("### Historique de la conversation :")
      for message in st.session_state.history:
         st.write(message) 

   Interface STREAMLIT 
   ===============
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
==================
Le Chatbot PSY est une application utile pour explorer les émotions et accéder à des ressources pratiques. N’hésitez pas à contribuer au projet ou à signaler des problèmes via le dépôt GitHub.
