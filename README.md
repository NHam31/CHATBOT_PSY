<<<<<<< HEAD

# Chatbot PSY 🌼

Le Chatbot PSY est une application Streamlit interactive conçue pour aider les utilisateurs à mieux comprendre leurs émotions et à recevoir des conseils pratiques pour améliorer leur bien-être mental. Le chatbot détecte des émotions comme le stress, la dépression, l'anxiété et les difficultés d'adaptabilité, puis recommande des ressources comme des vidéos et des exercices de relaxation.

## Fonctionnalités

- **Détection d'émotions** : Le chatbot analyse les messages de l'utilisateur pour identifier des émotions comme le stress, la dépression, l'anxiété et les difficultés d'adaptabilité.
- **Recommandations personnalisées** : En fonction des émotions détectées, le chatbot propose des vidéos de relaxation, de méditation, de yoga, ainsi que des exercices de gestion du stress et de la dépression.
- **Interface Streamlit** : Une interface simple et intuitive qui permet à l'utilisateur de discuter avec le chatbot, recevoir des conseils et suivre un historique de la conversation.
- **Modèle LLM :** :    - Intègre le modèle `llama3.2` via `OllamaLLM` pour gérer les interactions utilisateur et analyser les émotions.

## Prérequis

1. **Langages et outils requis :**
   - Python 3.8+
   - Streamlit
   - LangChain
   - OllamaLLM
     
## Installation

Pour installer et exécuter le chatbot localement, suivez ces étapes :

#### 1. Cloner le dépôt

git clone https://github.com/votre-utilisateur/chatbot-psy.git
cd chatbot-psy

#### 2.Créer un environnement virtuel (optionel)
python -m venv venv
source venv/bin/activate   # Sur Windows, utilisez `venv\Scripts\activate`

#### 3. Installer les dépendances
pip install -r requirements.txt


### Structure du projet
chatbot_psy/
│
├── requirements.txt             # Liste des dépendances
├── setup.py                     # Script d'installation
├── src/
│   ├── chatbot_psy.py           # Code principal de votre application
│   └── __init__.py              # Fichier pour marquer le dossier src comme un package
│
├── examples/                    # Répertoire pour les exemples
│   └── sample_input.txt         # Exemples d'entrées utilisateu
│
├── .gitignore                   # Liste des fichiers à ignorer par git
└── README.md                    # Description du projet


## Resources

Le fichier `resources/resources.json` contient des vidéos et des exercices pour gérer le stress, la dépression et l'anxiété. Ce fichier est utilisé pour fournir des recommandations personnalisées dans le chatbot.

- **Stress** : Exercices de respiration, méditation, yoga.
- **Dépression** : Vidéos motivationnelles et exercices positifs.
- **Anxiété** : Techniques de relaxation et de gestion cognitive.

Utilisation dans le code :
```python
import json

with open("resources/resources.json", "r") as file:
    resources = json.load(file)

print(resources["stress"]["exercise"])
   ```
## Structure du Code

Le projet est structuré de manière à faciliter la navigation et la compréhension du code.
```python
- **initialize_session** : Cette fonction configure l'état de la session utilisateur.
  def initialize_session():
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
```

- **detect_and_recommend_emotions** : Cette fonction analyse les entrées utilisateur pour
  ```python
  détecter les émotions et les troubles associés.
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
   ```

- **get_random_resources** : Cette fonction sélectionne aléatoirement des vidéos et des exercices en fonction des émotions détectées.
  ```python
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
   ```
  
- **chat** : Cette fonction gère l'interaction principale avec l'utilisateur via Streamlit. Elle affiche le chatbot et les recommandations en fonction des émotions détectées.
- **get_model** : Cette fonction récupère le modèle de langage pour générer des réponses en fonction des entrées utilisateur.
  ```python
  def get_model():
    return OllamaLLM(model="llama3.2")
   ```
- **resources** : Dictionnaire contenant les ressources disponibles pour chaque émotion et trouble, comme des vidéos et des exercices.

## Exécuter l'application Streamlit
streamlit run src/chatbot_psy.py

=======
# CHATBOT_PSY
>>>>>>> b4e54d3 (Initial commit)
