# TP2: Routes avec Flask

## Objectifs d'apprentissage

- Comprendre le concept de routage web et son importance
- Créer et gérer différents types de routes avec Flask
- Apprendre à manipuler les requêtes HTTP (GET, POST)
- Pratiquer la gestion des erreurs HTTP

## Prérequis

- Python 3.8+ installé
- Connaissance basique de Python
- Un éditeur de code (VS Code recommandé)
- pipenv installé (`pip install pipenv`)

## 1. Introduction au Routage Web

Le routage est la façon dont une application web associe des URLs (comme `/about` ou `/contact`) à des fonctions Python qui génèrent les réponses. Dans Flask, le routage est géré par des décorateurs.

### Types de Routes dans Flask

1. **Route Simple**

   ```python
   @app.route('/') # décorateur
   def home():
       return 'Page d\'accueil'
   ```

2. **Route avec Variable**

   ```python
   @app.route('/user/<username>')
   def show_user(username):
       return f'Profil de {username}'
   ```

3. **Route avec Type de Variable**

   ```python
   @app.route('/article/<int:id>')
   def show_article(id):
       return f'Article numéro {id}'
   ```

## 2. Mise en Place du Projet

### Création de l'environnement

```bash
# Créer un nouveau dossier pour le projet
mkdir TP2
cd TP2

# Initialiser l'environnement virtuel
pipenv install flask
```

### Code de Base (app.py)

créer un fichier app.py

```python
from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bienvenue sur mon application Flask!'

if __name__ == '__main__':
    app.run(debug=True)
```

Activer l'environnement virtuel :

```bash
pipenv shell
```

Exécuter l'application Flask :

```bash
pipenv run python app.py
```

### Structure du Projet

``` bash
TP2/
├── app.py           # Application Flask
├── Pipfile          # Dépendances du projet
└── Pipfile.lock     # Versions exactes des dépendances
```

## 3. Types de Routes Essentiels

### Routes Statiques

```python
@app.route('/about')
def about():
    return 'À propos de nous'
```

### Routes Dynamiques

```python
# Route avec paramètre string
@app.route('/user/<username>')
def user_profile(username):
    return f'Profil de {username}'

# Route avec paramètre entier
@app.route('/article/<int:article_id>')
def show_article(article_id):
    return f'Article numéro {article_id}'
```
## 4. Convertisseurs de Variables

Flask propose plusieurs types de convertisseurs pour les variables dans les URLs:

| Type    | Description                    | Exemple                        |
|---------|--------------------------------|--------------------------------|
| string  | Texte sans slash (défaut)      | `/user/<string:name>`          |
| int     | Nombres entiers                | `/article/<int:id>`            |
| float   | Nombres décimaux               | `/prix/<float:montant>`        |
| path    | Chemin complet avec slashes    | `/fichier/<path:chemin>`       |
| uuid    | Identifiants uniques UUID      | `/doc/<uuid:id>`               |

### Routes avec Méthodes HTTP

```python
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        return f'Message reçu de {name}'
    return '''
        <form method="POST">
            <input type="text" name="name">
            <button type="submit">Envoyer</button>
        </form>
    '''
```

## 5. Exercices Pratiques

1. **Routes Basiques**
   - Créez une route `/info` qui affiche des informations statiques
   - Ajoutez une route `/date` qui affiche la date actuelle

   ```python
   from datetime import datetime
   
   @app.route('/date')
   def show_date():
       return datetime.now().strftime('%Y-%m-%d %H:%M:%S')
   ```

2. **Routes Dynamiques**
   - Créez une route `/produit/<id>` qui simule l'affichage d'un produit
   - Implémentez une route `/calcul/<int:x>/<int:y>` qui affiche la somme

3. **Formulaire Simple**
   - Créez une route `/inscription` qui accepte GET et POST
   - Affichez un formulaire en GET
   - Traitez les données en POST

## 6. Gestion des Erreurs

```python
@app.errorhandler(404)
def page_not_found(error):
    return 'Page non trouvée', 404

@app.errorhandler(500)
def server_error(error):
    return 'Erreur serveur', 500
```

## 7. Bonnes Pratiques

1. **Nommage des Routes**
   - Utilisez des noms descriptifs et cohérents
   - Préférez les minuscules
   - Évitez les caractères spéciaux

2. **Sécurité**
   - Validez toujours les données reçues
   - Échappez les données affichées
   - Ne faites pas confiance aux données utilisateur

3. **Organisation**
   - Groupez les routes logiquement
   - Utilisez des blueprints pour les grandes applications
   - Documentez vos routes

## 8. Démarrage de l'Application

```bash
# Activer l'environnement virtuel
pipenv shell

# Lancer l'application
python app.py
```

Visitez http://127.0.0.1:5000 dans votre navigateur.

## Ressources Utiles

- [Documentation officielle Flask](https://flask.palletsprojects.com/)
- [Flask Mega-Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- [Flask Quickstart](https://flask.palletsprojects.com/quickstart/)

## Dépannage Courant

1. **Erreur "Port already in use"**
   - Fermez toutes les instances de Python
   - Ou changez le port: `app.run(port=5001)`

2. **Modifications non visibles**
   - Vérifiez que `debug=True` est activé
   - Rafraîchissez le cache du navigateur

3. **Erreurs d'encodage**
   - Ajoutez `# -*- coding: utf-8 -*-` en haut des fichiers
   - Utilisez des chaînes unicode (préfixe u)
