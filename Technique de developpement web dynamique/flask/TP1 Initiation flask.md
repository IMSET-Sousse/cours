# TP1: Initiation à Flask

![Flask Logo](assets/flask-logo.webp)

## Objectifs

- Comprendre les bases de Flask et son architecture
- Configurer un environnement de développement Python professionnel
- Maîtriser la gestion des dépendances avec pipenv
- Créer et exécuter une première application Flask
- Comprendre le cycle de vie d'une requête Flask

## Prérequis

- Python 3.8+ installé sur votre machine
- Un éditeur de code (VS Code recommandé)
- Connaissances de base en Python

## Étapes Détaillées

### 1. Préparation de l'Environnement

#### Installation de Python

1. Vérifiez votre version de Python :

   ```bash
   python --version
   # ou
   python3 --version
   ```

   Si Python n'est pas installé ou si la version est < 3.8, téléchargez-le depuis [python.org](https://www.python.org/downloads/)

2. Vérifiez que pip est installé :

   ```bash
   pip --version
   # ou
   pip3 --version
   ```

#### Installation de pipenv

pipenv est un outil moderne pour gérer les environnements virtuels Python et les dépendances du projet.

```bash
# Installation globale de pipenv
pip install pipenv

# Vérification de l'installation
pipenv --version
```

### 2. Configuration du Projet

1. Naviguez vers votre bureau :
2. Créez un nouveau dossier pour votre projet :

   ```bash
   mkdir mon_projet_flask
   cd mon_projet_flask
   ```

3. Initialisez un environnement virtuel avec Flask :

   ```bash
   # Création de l'environnement virtuel et installation de Flask
   pipenv install flask
   ```

   Cette commande va :

   - Créer un nouvel environnement virtuel
   - Installer Flask et ses dépendances
   - Créer les fichiers Pipfile et Pipfile.lock

### 3. Structure du Projet

Créez la structure de base suivante :

```plaintext
mon_projet_flask/
├── Pipfile           # Fichier de dépendances de pipenv
├── Pipfile.lock     # Verrouillage des versions des dépendances
├── app.py           # Point d'entrée de l'application
└── README.md        # Documentation du projet
```

### 4. Création de l'Application

Créez le fichier `app.py` avec le code minimal suivant :

```python
from flask import Flask

# Création de l'instance de l'application
app = Flask(__name__)

# Définition de la route racine
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Point d'entrée de l'application
if __name__ == '__main__':
    # Active le mode debug pour le développement
    app.run(debug=True)
```

### 5. Lancement de l'Application

1. Activez l'environnement virtuel :

   ```bash
   pipenv shell
   ```

2. Lancez l'application :

   ```bash
   python app.py
   ```

3. Visitez http://127.0.0.1:5000 dans votre navigateur

### 6. Configuration de VS Code (Recommandé)

Pour une meilleure expérience de développement :

1. Installez les extensions VS Code recommandées :

   - Python (Microsoft)
   - Python Debugger
   - Python Environment Manager
   - Python Indent
   - autoDocstring - Python

2. Configurez l'interpréteur Python :
   - Appuyez sur `Ctrl+Shift+P` (Windows/Linux) ou `Cmd+Shift+P` (Mac)
   - Tapez "Python: Select Interpreter"
   - Sélectionnez l'environnement virtuel créé par pipenv

## Points Importants à Retenir

### Architecture Flask

- Flask suit le pattern de conception "microframework"
- Une application Flask est une instance de la classe `Flask`
- Les routes définissent comment l'application répond aux requêtes URL
- Le mode debug permet le rechargement automatique et des messages d'erreur détaillés

### Environnement Virtuel

- Isole les dépendances du projet
- Évite les conflits entre différents projets
- Facilite la reproduction de l'environnement
- Pipfile liste toutes les dépendances du projet

### Bonnes Pratiques

1. **Gestion des Dépendances**

   - Toujours utiliser un environnement virtuel
   - Maintenir à jour le Pipfile
   - Spécifier les versions des dépendances

2. **Organisation du Code**

   - Un fichier par fonctionnalité
   - Séparer la configuration de l'application
   - Utiliser des commentaires descriptifs

3. **Sécurité**
   - Ne jamais désactiver le debug en production
   - Ne pas exposer d'informations sensibles
   - Suivre les recommandations de sécurité Flask

## Résolution des Problèmes Courants

### 1. Erreur "Port already in use"

**Symptôme** : L'application ne démarre pas, message d'erreur mentionnant le port 5000.

**Solutions** :

- Fermez toutes les instances Python en cours
- Changez le port dans `app.run()` :

  ```python
  app.run(debug=True, port=5001)
  ```

### 2. Problèmes avec pipenv

**Symptôme** : Commandes pipenv non reconnues

**Solutions** :

- Réinstallez pipenv : `pip install --user --upgrade pipenv`
- Utilisez `python -m pipenv` au lieu de `pipenv`

### 3. Erreurs d'Import

**Symptôme** : ModuleNotFoundError lors de l'import de Flask

**Solutions** :

- Vérifiez que vous êtes dans l'environnement virtuel
- Réinstallez Flask : `pipenv install flask`
- Vérifiez le Pipfile

## Ressources Utiles

- [Documentation officielle Flask](https://flask.palletsprojects.com/)
- [Documentation pipenv](https://pipenv.pypa.io/)
- [Guide de démarrage Flask](https://flask.palletsprojects.com/quickstart/)
- [Python Virtual Environments](https://docs.python.org/3/tutorial/venv.html)
