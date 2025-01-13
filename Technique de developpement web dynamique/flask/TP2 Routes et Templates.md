# TP2: Routes et Templates avec Flask

## Objectifs

- Comprendre et implémenter les routes Flask
- Maîtriser les templates Jinja2
- Créer une structure de navigation avec héritage de templates
- Ajouter des styles et des fichiers statiques

## Prérequis

- Python 3.8+ installé sur Windows
- pipenv installé (`pip install pipenv`)
- Un éditeur de code (VS Code recommandé)

## Étapes à suivre

### 1. Création de l'environnement virtuel

Ouvrez un terminal (PowerShell ou CMD) et exécutez :

```bash
# Créer un nouveau dossier
mkdir TP2
cd TP2

# Initialiser l'environnement virtuel et installer Flask
pipenv install flask
```

### 2. Création de l'application Flask

Créez un fichier `app.py` :

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Accueil")

@app.route('/about')
def about():
    return render_template('about.html', title="À propos")

@app.route('/contact')
def contact():
    return render_template('contact.html', title="Contact")

if __name__ == '__main__':
    app.run(debug=True)
```

### 3. Configuration des Templates

#### a. Créez le template de base (`templates/base.html`)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }} - Mon Application Flask</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <header>
        <nav>
            <ul>
                <li><a href="{{ url_for('home') }}">Accueil</a></li>
                <li><a href="{{ url_for('about') }}">À propos</a></li>
                <li><a href="{{ url_for('contact') }}">Contact</a></li>
            </ul>
        </nav>
    </header>

    <main>
        {% block content %}
        {% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 Mon Application Flask</p>
    </footer>
</body>
</html>
```

#### b. Créez les templates des pages (`templates/index.html`) :

```html
{% extends "base.html" %}

{% block content %}
<h1>Bienvenue sur Flask!</h1>
<p>Cette page d'accueil utilise l'héritage de templates.</p>
{% endblock %}
```

#### c. Créez `templates/about.html` :

```html
{% extends "base.html" %}

{% block content %}
<h1>À propos de nous</h1>
<p>Découvrez notre application Flask.</p>
{% endblock %}
```

#### d. Créez `templates/contact.html` :

```html
{% extends "base.html" %}

{% block content %}
<h1>Contactez-nous</h1>
<form method="POST" action="{{ url_for('contact') }}">
    <div>
        <label for="name">Nom:</label>
        <input type="text" id="name" name="name" required>
    </div>
    <div>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
    </div>
    <div>
        <label for="message">Message:</label>
        <textarea id="message" name="message" required></textarea>
    </div>
    <button type="submit">Envoyer</button>
</form>
{% endblock %}
```

### 4. Ajout des styles CSS

Créez `static/css/style.css` :

```css
/* Style de base */
body {
    font-family: Arial, sans-serif;
    margin: 0;
    padding: 0;
    line-height: 1.6;
}

/* Navigation */
nav {
    background-color: #333;
    padding: 1rem;
}

nav ul {
    list-style: none;
    padding: 0;
    margin: 0;
    display: flex;
    justify-content: center;
}

nav li {
    margin: 0 1rem;
}

nav a {
    color: white;
    text-decoration: none;
}

nav a:hover {
    color: #ddd;
}

/* Contenu principal */
main {
    padding: 2rem;
    max-width: 800px;
    margin: 0 auto;
}

/* Formulaire */
form {
    display: flex;
    flex-direction: column;
    gap: 1rem;
}

form div {
    display: flex;
    flex-direction: column;
}

input, textarea {
    padding: 0.5rem;
    margin-top: 0.25rem;
}

button {
    padding: 0.5rem 1rem;
    background-color: #333;
    color: white;
    border: none;
    cursor: pointer;
}

button:hover {
    background-color: #444;
}

/* Footer */
footer {
    text-align: center;
    padding: 1rem;
    background-color: #f5f5f5;
    margin-top: 2rem;
}
```

## Lancement de l'application

Pour lancer l'application sur Windows :

```bash
# Activer l'environnement virtuel
pipenv shell

# Lancer l'application
python app.py
```

Visitez http://127.0.0.1:5000 dans votre navigateur.

## Exercices pratiques

1. **Route dynamique** :
   - Ajoutez une route `/user/<username>` qui affiche un message personnalisé pour chaque utilisateur

2. **Transmission de données** :
   - Modifiez la route `/contact` pour gérer les soumissions POST du formulaire
   - Affichez un message de confirmation après l'envoi

3. **Template avancé** :
   - Ajoutez une section "Articles" avec une liste d'articles
   - Utilisez une boucle `{% for %}` dans le template pour afficher les articles

## Conseils et bonnes pratiques

- Utilisez toujours `url_for()` pour générer les URLs
- Organisez vos fichiers statiques par type (css, js, images)
- Testez votre application avec différents navigateurs
- Utilisez la fonction `debug=True` uniquement en développement

## Dépannage courant sur Windows

- Si `pipenv` n'est pas reconnu, ajoutez Python et pip aux variables d'environnement
- En cas d'erreur "Port already in use", fermez toutes les instances de Python ou changez le port
- Pour les problèmes d'encodage, ajoutez `# -*- coding: utf-8 -*-` en haut des fichiers Python
