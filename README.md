# CHATBOT_PSY
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
