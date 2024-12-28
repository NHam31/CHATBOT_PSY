from setuptools import setup, find_packages

setup(
    name="chatbot_psy",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "streamlit",
        "langchain_ollama",
        "difflib",
        "random",
        "requests",  # Ajoutez ici d'autres dépendances si nécessaire
    ],
    entry_points={
        "console_scripts": [
            "chatbot_psy=src.chatbot_psy:main",  # Point d'entrée du projet
        ],
    },
)
