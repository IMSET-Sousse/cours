# TP 1 : Initiation à Django (Version 4.2)

## Introduction

Django est un framework web Python de haut niveau qui encourage un développement rapide et une conception propre et pragmatique([1](https://docs.djangoproject.com/en/4.2/)). Il suit le modèle architectural MVT (Model-View-Template), une variation du MVC, et inclut de nombreuses fonctionnalités "batteries included" comme un ORM puissant, un système d'administration automatique et un système de templates flexible.

Ce TP a pour objectif de vous initier aux bases de Django, de vous guider dans la création d'une application web simple et de vous préparer à explorer ses fonctionnalités avancées.

## Objectifs

- Installer Python et pip
- Créer un environnement virtuel
- Installer Django
- Créer un nouveau projet Django
- Comprendre la structure d'un projet Django
- Créer une première application
- Configurer les URLs et les vues
- Utiliser le système de templates

## Prérequis

- Un éditeur de code (VS Code recommandé)
- Un terminal de commande
- Une connexion internet
- Connaissances de base en Python, HTML et CSS

> **Ressources recommandées** :
>
> - [Python](https://www.python.org/)
> - [HTML & CSS](https://www.w3schools.com/html/)
> - [Documentation Django](https://docs.djangoproject.com/)

## Étapes

### 1. Installation de l'environnement

1. Téléchargez et installez Python depuis [python.org](https://python.org/)
   - Version 3.8 ou ultérieure recommandée
   - Cochez l'option "Add Python to PATH" lors de l'installation

2. Vérifiez l'installation en ouvrant un terminal :

   Pour vérifier Python :
   ```powershell
   python --version
   ```

   Pour vérifier pip :
   ```powershell
   pip --version
   ```

### 2. Configuration de l'environnement de développement

1. Installez VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/)
2. Installez les extensions recommandées :
   - Python (Microsoft)
   - Django (Baptiste Darthenay)
   - SQLite Viewer

3. Créez un environnement virtuel :
   ```powershell
   # Créez un dossier pour votre projet
   mkdir mon-projet-django
   cd mon-projet-django
   
   # Créez l'environnement virtuel
   python -m venv env
   
   # Activez l'environnement virtuel
   # Sur Windows :
   env\Scripts\activate
   # Sur Unix/MacOS :
   source env/bin/activate
   ```

4. Installez Django :
   ```powershell
   pip install django
   ```

### 3. Création d'un projet Django

1. Créez un nouveau projet([2](https://docs.djangoproject.com/en/4.2/intro/tutorial01/)) :
   ```powershell
   django-admin startproject monsite .
   ```

2. Structure du projet créé :
   ```text
   monsite/
   ├── manage.py          # Utilitaire en ligne de commande
   └── monsite/           # Package Python du projet
       ├── __init__.py    # Indique que c'est un package Python
       ├── settings.py    # Configuration du projet
       ├── urls.py        # Configuration des URLs
       ├── asgi.py        # Point d'entrée ASGI
       └── wsgi.py        # Point d'entrée WSGI
   ```

3. Lancez le serveur de développement :
   ```powershell
   python manage.py runserver
   ```
   Visitez [http://127.0.0.1:8000/](http://127.0.0.1:8000/) pour voir la page de bienvenue.

### 4. Création d'une première application

1. Créez une nouvelle application :
   ```powershell
   python manage.py startapp blog
   ```

2. Structure de l'application :
   ```text
   blog/
   ├── migrations/        # Dossier des migrations de base de données
   ├── __init__.py
   ├── admin.py          # Configuration de l'interface d'administration
   ├── apps.py           # Configuration de l'application
   ├── models.py         # Modèles de données
   ├── tests.py          # Tests unitaires
   └── views.py          # Vues de l'application
   ```

3. Ajoutez l'application dans `settings.py` :
   ```python:monsite/settings.py
   INSTALLED_APPS = [
       'django.contrib.admin',
       'django.contrib.auth',
       'django.contrib.contenttypes',
       'django.contrib.sessions',
       'django.contrib.messages',
       'django.contrib.staticfiles',
       'blog',  # Ajoutez votre application ici
   ]
   ```

### 5. Création des premiers modèles

1. Définissez un modèle dans `blog/models.py` :
   ```python:blog/models.py
   from django.db import models
   from django.utils import timezone

   class Article(models.Model):
       titre = models.CharField(max_length=200)
       contenu = models.TextField()
       date_creation = models.DateTimeField(default=timezone.now)
       
       def __str__(self):
           return self.titre
   ```

2. Créez et appliquez les migrations :
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

### 6. Création des vues et URLs

1. Créez une vue dans `blog/views.py` :
   ```python:blog/views.py
   from django.shortcuts import render
   from .models import Article

   def liste_articles(request):
       articles = Article.objects.all().order_by('-date_creation')
       return render(request, 'blog/liste_articles.html', {'articles': articles})
   ```

2. Créez un fichier `blog/urls.py` :
   ```python:blog/urls.py
   from django.urls import path
   from . import views

   app_name = 'blog'
   urlpatterns = [
       path('', views.liste_articles, name='liste_articles'),
   ]
   ```

3. Modifiez `monsite/urls.py` :
   ```python:monsite/urls.py
   from django.contrib import admin
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('blog/', include('blog.urls')),
   ]
   ```

### 7. Création des templates

1. Créez la structure des templates :
   ```text
   blog/
   └── templates/
       └── blog/
           ├── base.html
           └── liste_articles.html
   ```

2. Créez le template de base `blog/templates/blog/base.html` :
   ```html:blog/templates/blog/base.html
   <!DOCTYPE html>
   <html lang="fr">
   <head>
       <meta charset="UTF-8">
       <title>{% block title %}Mon Blog{% endblock %}</title>
       <style>
           body {
               max-width: 800px;
               margin: 0 auto;
               padding: 20px;
               font-family: Arial, sans-serif;
           }
           .article {
               margin-bottom: 20px;
               padding: 15px;
               border: 1px solid #ddd;
           }
       </style>
   </head>
   <body>
       <header>
           <h1>Mon Blog Django</h1>
       </header>
       <main>
           {% block content %}
           {% endblock %}
       </main>
   </body>
   </html>
   ```

3. Créez le template de liste `blog/templates/blog/liste_articles.html` :
   ```html:blog/templates/blog/liste_articles.html
   {% extends 'blog/base.html' %}

   {% block title %}Articles - {{ block.super }}{% endblock %}

   {% block content %}
   <h2>Liste des articles</h2>
   {% for article in articles %}
       <article class="article">
           <h3>{{ article.titre }}</h3>
           <p>{{ article.contenu|truncatewords:30 }}</p>
           <small>Publié le {{ article.date_creation|date:"d/m/Y" }}</small>
       </article>
   {% empty %}
       <p>Aucun article disponible.</p>
   {% endfor %}
   {% endblock %}
   ```

## Exercices Pratiques

### Exercice 1 : Créer un Superutilisateur

1. Créez un superutilisateur :
   ```powershell
   python manage.py createsuperuser
   ```

2. Enregistrez le modèle Article dans l'admin (`blog/admin.py`) :
   ```python:blog/admin.py
   from django.contrib import admin
   from .models import Article

   admin.site.register(Article)
   ```

3. Accédez à l'interface d'administration sur [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

### Exercice 2 : Ajouter une Page de Détail

1. Ajoutez une vue de détail dans `views.py` :
   ```python:blog/views.py
   from django.shortcuts import render, get_object_or_404

   def detail_article(request, article_id):
       article = get_object_or_404(Article, pk=article_id)
       return render(request, 'blog/detail_article.html', {'article': article})
   ```

2. Ajoutez l'URL dans `blog/urls.py` :
   ```python:blog/urls.py
   urlpatterns = [
       path('', views.liste_articles, name='liste_articles'),
       path('article/<int:article_id>/', views.detail_article, name='detail_article'),
   ]
   ```

3. Créez le template `blog/templates/blog/detail_article.html` :
   ```html:blog/templates/blog/detail_article.html
   {% extends 'blog/base.html' %}

   {% block title %}{{ article.titre }} - {{ block.super }}{% endblock %}

   {% block content %}
   <article>
       <h2>{{ article.titre }}</h2>
       <p>{{ article.contenu }}</p>
       <p><small>Publié le {{ article.date_creation|date:"d/m/Y" }}</small></p>
       <a href="{% url 'blog:liste_articles' %}">Retour à la liste</a>
   </article>
   {% endblock %}
   ```

### Exercice 3 : Ajouter des Catégories

1. Ajoutez un modèle Categorie :
   ```python:blog/models.py
   class Categorie(models.Model):
       nom = models.CharField(max_length=100)
       description = models.TextField(blank=True)

       def __str__(self):
           return self.nom

   class Article(models.Model):
       # ... code existant ...
       categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE)
   ```

2. Créez et appliquez les migrations :
   ```powershell
   python manage.py makemigrations
   python manage.py migrate
   ```

## Ressources Supplémentaires

- [Documentation officielle de Django](https://docs.djangoproject.com/)
- [Django Girls Tutorial](https://tutorial.djangogirls.org/)
- [Django REST framework](https://www.django-rest-framework.org/) (pour les APIs)
- [Awesome Django](https://github.com/wsvincent/awesome-django)

## Conclusion

Ce TP vous a permis de découvrir les bases de Django et de créer une application web simple. Les concepts abordés serviront de base pour des fonctionnalités plus avancées dans les prochains TPs.
