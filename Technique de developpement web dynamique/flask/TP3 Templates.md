# TP3: Templates avec Flask

## Objectifs d'apprentissage

- Comprendre le concept des templates et leur importance
- Maîtriser les bases de Jinja2, le moteur de templates de Flask
- Apprendre à créer des layouts réutilisables
- Utiliser les variables et les structures de contrôle dans les templates
- Gérer les fichiers statiques (CSS, JavaScript, images)

## Prérequis

- Avoir complété le TP2 sur les Routes
- Connaissances de base en HTML et CSS
- Python et Flask installés
- Un éditeur de code (VS Code recommandé)

## 1. Introduction aux Templates

Les templates permettent de séparer la logique Python (backend) de la présentation HTML (frontend). Flask utilise Jinja2 comme moteur de templates par défaut.

### Structure du Projet

```bash
mon_app/
├── static/
│   ├── css/
│   │   └── style.css
│   └── img/
│       └── logo.png
├── templates/
│   ├── base.html
│   ├── index.html
│   └── about.html
└── app.py
```

## 2. Création des Templates de Base

### Template Principal (base.html)

```html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}{% endblock %} - Mon Site</title>
    <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}">
</head>
<body>
    <nav>
        <ul>
            <li><a href="{{ url_for('index') }}">Accueil</a></li>
            <li><a href="{{ url_for('about') }}">À propos</a></li>
        </ul>
    </nav>
    
    <main>
        {% block content %}{% endblock %}
    </main>

    <footer>
        <p>&copy; 2024 Mon Site Flask</p>
    </footer>
</body>
</html>
```

### Page d'Accueil (index.html)

```html
{% extends "base.html" %}

{% block title %}Accueil{% endblock %}

{% block content %}
<h1>Bienvenue sur mon site</h1>
<p>Cette page utilise l'héritage de template.</p>
{% endblock %}
```

## 3. Syntaxe Jinja2 Essentielle

### Variables et Expressions

```html
<!-- Affichage simple -->
{{ variable }}

<!-- Expressions -->
{{ nombre * 2 }}
{{ "Bonjour " + nom }}

<!-- Accès aux attributs -->
{{ user.name }}
{{ dict['key'] }}
```

### Structures de Contrôle

```html
<!-- Conditions -->
{% if user %}
    <h1>Bonjour {{ user.name }}</h1>
{% else %}
    <h1>Bonjour visiteur</h1>
{% endif %}

<!-- Boucles -->
<ul>
{% for item in items %}
    <li>{{ item }}</li>
{% endfor %}
</ul>
```

## 4. Configuration dans Flask

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    user = {'name': 'John', 'age': 30}
    posts = [
        {'title': 'Post 1', 'content': 'Contenu du post 1'},
        {'title': 'Post 2', 'content': 'Contenu du post 2'}
    ]
    return render_template('index.html', user=user, posts=posts)
```

## 5. Fonctionnalités Avancées

### Filtres

```html
<!-- Modification de texte -->
{{ name|upper }}
{{ text|truncate(100) }}

<!-- Formatage de dates -->
{{ date|dateformat('%Y-%m-%d') }}

<!-- Valeurs par défaut -->
{{ variable|default('valeur par défaut') }}
```

### Macros (Fonctions Réutilisables)

```html
{% macro input(name, label, type='text') %}
<div class="form-group">
    <label for="{{ name }}">{{ label }}</label>
    <input type="{{ type }}" id="{{ name }}" name="{{ name }}">
</div>
{% endmacro %}

<!-- Utilisation -->
{{ input('username', 'Nom d\'utilisateur') }}
{{ input('password', 'Mot de passe', type='password') }}
```

## 6. Gestion des Fichiers Statiques

### Structure CSS (static/css/style.css)

```css
/* Style de base */
body {
    font-family: Arial, sans-serif;
    line-height: 1.6;
    margin: 0;
    padding: 20px;
}

nav {
    background: #333;
    padding: 1rem;
}

nav ul {
    list-style: none;
    display: flex;
    gap: 1rem;
}

nav a {
    color: white;
    text-decoration: none;
}
```

## 7. Exercices Pratiques

1. **Template de Base**
   - Créez un layout de base avec en-tête et pied de page
   - Ajoutez un menu de navigation
   - Incluez des fichiers CSS personnalisés

2. **Pages Dynamiques**
   - Créez une page qui affiche une liste d'articles
   - Ajoutez une page de détail pour chaque article
   - Utilisez des conditions pour gérer l'affichage

3. **Formulaires**
   - Créez un template pour un formulaire de contact
   - Utilisez des macros pour les champs de formulaire
   - Ajoutez une validation côté client

## 8. Bonnes Pratiques

1. **Organisation**
   - Gardez vos templates simples et modulaires
   - Utilisez l'héritage de templates pour éviter la répétition
   - Séparez la logique Python du HTML

2. **Performance**
   - Minimisez les fichiers CSS et JavaScript
   - Utilisez la mise en cache des templates
   - Optimisez les images

3. **Sécurité**
   - Échappez toujours les données utilisateur
   - Utilisez `{{ }}` pour l'auto-échappement
   - Validez les entrées côté serveur

## Ressources Utiles

- [Documentation Jinja2](https://jinja.palletsprojects.com/)
- [Documentation Flask Templates](https://flask.palletsprojects.com/templating/)
- [Flask Mega-Tutorial - Templates](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-ii-templates)

## Dépannage Courant

1. **Erreurs de Template**
   - Vérifiez la syntaxe Jinja2
   - Assurez-vous que les variables existent
   - Utilisez le mode debug de Flask

2. **Problèmes de Fichiers Statiques**
   - Vérifiez les chemins dans `url_for()`
   - Assurez-vous que les fichiers sont dans le bon dossier
   - Videz le cache du navigateur
