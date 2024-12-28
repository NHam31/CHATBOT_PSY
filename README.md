
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

### 1. Cloner le dépôt

git clone https://github.com/votre-utilisateur/chatbot-psy.git
cd chatbot-psy

### 2.Créer un environnement virtuel (optionel)
python -m venv venv
source venv/bin/activate   # Sur Windows, utilisez `venv\Scripts\activate`

### 3. Installer les dépendances
pip install -r requirements.txt

### 4. Exécuter l'application Streamlit
streamlit run src/chatbot_psy.py

#Structure du projet
chatbot_psy/
│
├── config.py                    # Configuration du projet
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


### Resources

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
