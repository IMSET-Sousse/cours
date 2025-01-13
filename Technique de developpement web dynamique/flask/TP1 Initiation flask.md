# TP1: Initiation à Flask

## Objectifs

- Comprendre les bases de Flask
- Apprendre à configurer un environnement Flask
- Créer votre première route Flask

## Étapes pour exécuter le projet

1. Installer `pipenv` pour gérer l'environnement virtuel et les dépendances :

    ```bash
    pip install pipenv
    ```

2. Cree dossier TP1 et se placer dedans:

    ```bash
    mkdir TP1
    cd TP1
    ```

3. Installer les packages requis avec `pipenv`.

Voici les différentes options :

    Option 1 - Installation directe avec pipenv :

    ```bash
    pipenv install flask
    ```
    
    Option 2 - Installation explicite avec python -m :
    
    ```bash
    # Pour Python 3
    python -m pipenv install flask
    ```
    
    Option 3 - Installation avec python3 explicite :
    
    ```bash
    # Pour les systèmes utilisant python3
    python3 -m pipenv install flask
    ```

    L'option 1 est recommandée si pipenv est correctement configuré dans votre PATH.
    L'option 2 est utile si vous avez des problèmes avec l'option 1.
    L'option 3 est nécessaire sur certains systèmes où python3 doit être explicitement spécifié.

1. Créer un fichier nommé `app.py` et ajouter le code suivant :

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run(debug=True)
    ```

2. Activer l'environnement virtuel :

    Option 1 - Activation directe avec pipenv :

    ```bash
    pipenv shell
    ```

    Option 2 - Activation explicite avec python -m :

    ```bash
    # Pour Python 3
    python -m pipenv shell
    ```

    Option 3 - Activation avec python3 explicite :

    ```bash
    # Pour les systèmes utilisant python3
    python3 -m pipenv shell
    ```

3. Exécuter l'application Flask :

    ```bash
    pipenv run python app.py
    ```

## Exercices

1. Modifiez la route principale pour afficher "Bonjour, [votre nom]!" au lieu de "Hello, World!"
2. Ajoutez une nouvelle route `/date` qui affiche la date actuelle
3. Créez une route `/info` qui affiche des informations sur vous

## Conseils

- Utilisez la documentation officielle de Flask comme référence
    see [Documentation Flask](https://flask.palletsprojects.com/en/latest/)
- N'oubliez pas de redémarrer le serveur après chaque modification
- Vérifiez que vous êtes dans le bon environnement virtuel
