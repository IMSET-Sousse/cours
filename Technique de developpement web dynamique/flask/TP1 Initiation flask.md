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

2. Installer les packages requis avec `pipenv` :

    ```bash
    python -m pipenv install flask
    ```

3. Créer un fichier nommé `app.py` et ajouter le code suivant :

    ```python
    from flask import Flask

    app = Flask(__name__)

    @app.route('/')
    def hello_world():
        return 'Hello, World!'

    if __name__ == '__main__':
        app.run(debug=True)
    ```

4. Exécuter l'application Flask :

    ```bash
    pipenv run python app.py
    ```

## Exercices

1. Modifiez la route principale pour afficher "Bonjour, [votre nom]!" au lieu de "Hello, World!"
2. Ajoutez une nouvelle route `/date` qui affiche la date actuelle
3. Créez une route `/info` qui affiche des informations sur vous

## Conseils
- Utilisez la documentation officielle de Flask comme référence
- N'oubliez pas de redémarrer le serveur après chaque modification
- Vérifiez que vous êtes dans le bon environnement virtuel
    Pour plus de détails sur l'objet `Flask`, consultez la [documentation Flask](https://flask.palletsprojects.com/en/latest/api/#flask.Flask).