# TP 5 : Django Authentication System

![Django Logo](./assets/django-logo.png)

## Introduction

L'authentification est un aspect fondamental de presque toutes les applications web. Django fournit un système d'authentification complet qui gère les comptes utilisateurs, les groupes, les permissions et les sessions utilisateur. Ce TP vous guidera à travers l'implémentation et la personnalisation du système d'authentification de Django dans vos applications.

## Objectifs

- Comprendre l'architecture du système d'authentification Django
- Implémenter les fonctionnalités d'inscription, de connexion et de déconnexion
- Créer et personnaliser des profils utilisateur
- Configurer la vérification par email et la réinitialisation de mot de passe
- Gérer les permissions et les groupes d'utilisateurs
- Sécuriser les vues avec les décorateurs d'authentification

## Prérequis

- Compréhension de base de Django (modèles, vues, templates, formulaires)
- Un projet Django existant (vous pouvez utiliser celui des TPs précédents)
- Compréhension des concepts de base de sécurité web

> **Ressources recommandées** :
>
> - [Documentation Authentication Django](https://docs.djangoproject.com/en/5.1/topics/auth/)
> - [Documentation sur les Permissions Django](https://docs.djangoproject.com/en/5.1/topics/auth/default/#permissions-and-authorization)
> - [OWASP Authentication Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)

## Étapes

### 1. Comprendre le Système d'Authentification de Django

#### Le modèle User par défaut

Django inclut un modèle `User` qui contient les champs de base :

- username
- password
- email
- first_name
- last_name
- is_active
- is_staff
- is_superuser
- date_joined
- last_login

#### Les modules intégrés

Django fournit plusieurs modules pour gérer l'authentification :

```python
from django.contrib.auth.models import User, Group, Permission
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
```

### 2. Inscription, Connexion et Déconnexion

#### Implémentation de l'inscription utilisateur

```python
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Compte créé pour {username}')
            return redirect('login')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})
```

#### Formulaire d'inscription personnalisé

```python
# forms.py
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Champ email obligatoire
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
```

#### Vues de connexion et déconnexion

```python
# views.py
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"Vous êtes connecté en tant que {username}")
                return redirect('home')
            else:
                messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
        else:
            messages.error(request, "Nom d'utilisateur ou mot de passe invalide.")
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "Vous avez été déconnecté.")
    return redirect('home')
```

#### Configuration des URLs

```python
# urls.py
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    
    # Alternative: utiliser les vues intégrées de Django
    # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
]
```

#### Templates d'authentification

Template d'inscription (`register.html`) :

```html
{% extends 'base.html' %}

{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Rejoignez-nous aujourd'hui</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">S'inscrire</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Déjà un compte? <a class="ml-2" href="{% url 'login' %}">Se connecter</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

Template de connexion (`login.html`) :

```html
{% extends 'base.html' %}

{% block content %}
    <div class="content-section">
        <form method="POST">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Connexion</legend>
                {{ form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Se connecter</button>
            </div>
        </form>
        <div class="border-top pt-3">
            <small class="text-muted">
                Besoin d'un compte? <a class="ml-2" href="{% url 'register' %}">S'inscrire</a>
            </small>
        </div>
    </div>
{% endblock content %}
```

Template de déconnexion (`logout.html`) :

```html
{% extends 'base.html' %}

{% block content %}
    <h2>Vous avez été déconnecté</h2>
    <div class="border-top pt-3">
        <small class="text-muted">
            <a href="{% url 'login' %}">Se reconnecter</a>
        </small>
    </div>
{% endblock content %}
```

### 3. Profils Utilisateurs Personnalisés

#### Extension du modèle User avec un modèle de profil

```python
# models.py
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    bio = models.TextField(blank=True)
    location = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.user.username} Profile'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        # Redimensionner l'image si nécessaire
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
```

#### Création automatique de profil avec les signaux

```python
# signals.py
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
```

Configurez les signaux dans `apps.py` :

```python
# apps.py
from django.apps import AppConfig

class UsersConfig(AppConfig):
    name = 'users'
    
    def ready(self):
        import users.signals
```

#### Mise à jour du profil utilisateur

```python
# forms.py
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'bio', 'location', 'birth_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
```

```python
# views.py
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm, ProfileUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Votre compte a été mis à jour!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    
    return render(request, 'users/profile.html', context)
```

Template de profil (`profile.html`) :

```html
{% extends 'base.html' %}

{% block content %}
    <div class="content-section">
        <div class="media">
            <img class="rounded-circle account-img" src="{{ user.profile.image.url }}">
            <div class="media-body">
                <h2 class="account-heading">{{ user.username }}</h2>
                <p class="text-secondary">{{ user.email }}</p>
                {% if user.profile.bio %}
                    <p>{{ user.profile.bio }}</p>
                {% endif %}
                {% if user.profile.location %}
                    <p><small>{{ user.profile.location }}</small></p>
                {% endif %}
            </div>
        </div>
        
        <form method="POST" enctype="multipart/form-data">
            {% csrf_token %}
            <fieldset class="form-group">
                <legend class="border-bottom mb-4">Informations du profil</legend>
                {{ u_form.as_p }}
                {{ p_form.as_p }}
            </fieldset>
            <div class="form-group">
                <button class="btn btn-outline-info" type="submit">Mettre à jour</button>
            </div>
        </form>
    </div>
{% endblock content %}
```

### 4. Vérification par Email et Réinitialisation de Mot de Passe

#### Configuration de l'envoi d'emails

Dans `settings.py` :

```python
# Pour le développement (affiche les emails dans la console)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Pour la production (utilise SMTP)
"""
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'votre_email@gmail.com'
EMAIL_HOST_PASSWORD = 'votre_mot_de_passe'
"""
```

#### Réinitialisation de mot de passe

```python
# urls.py
from django.contrib.auth import views as auth_views

urlpatterns = [
    # ...
    path('password-reset/',
        auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
        name='password_reset'),
    path('password-reset/done/',
        auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
        name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
        name='password_reset_confirm'),
    path('password-reset-complete/',
        auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
        name='password_reset_complete'),
]
```

Templates pour la réinitialisation de mot de passe :

1. `password_reset.html` - Formulaire pour demander la réinitialisation
2. `password_reset_done.html` - Message de confirmation après envoi de l'email
3. `password_reset_confirm.html` - Formulaire pour définir un nouveau mot de passe
4. `password_reset_complete.html` - Message de confirmation après réinitialisation

#### Vérification d'email lors de l'inscription

```python
# utils.py
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMessage
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import six

class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (
            six.text_type(user.pk) + six.text_type(timestamp) +
            six.text_type(user.is_active)
        )

account_activation_token = TokenGenerator()

def send_activation_email(user, request):
    current_site = get_current_site(request)
    mail_subject = 'Activez votre compte'
    message = render_to_string('users/account_activation_email.html', {
        'user': user,
        'domain': current_site.domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
    })
    to_email = user.email
    email = EmailMessage(mail_subject, message, to=[to_email])
    email.send()
```

```python
# views.py
from .utils import account_activation_token, send_activation_email
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Désactiver l'utilisateur jusqu'à confirmation
            user.save()
            send_activation_email(user, request)
            messages.info(request, 'Veuillez confirmer votre email pour compléter l\'inscription')
            return redirect('login')
    else:
        form = UserRegisterForm()
    
    return render(request, 'users/register.html', {'form': form})

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Votre compte a été activé avec succès. Vous pouvez maintenant vous connecter.')
        return redirect('login')
    else:
        messages.error(request, 'Le lien d\'activation est invalide!')
        return redirect('home')
```

### 5. Permissions et Groupes

#### Travailler avec les permissions

```python
# Vérifier si un utilisateur a une permission spécifique
if user.has_perm('app.add_model'):
    # L'utilisateur peut ajouter des instances du modèle
    
# Lister toutes les permissions d'un utilisateur
user.get_all_permissions()

# Ajouter une permission à un utilisateur
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

content_type = ContentType.objects.get_for_model(YourModel)
permission = Permission.objects.get(
    codename='change_yourmodel',
    content_type=content_type,
)
user.user_permissions.add(permission)

# Créer une permission personnalisée
class Meta:
    permissions = (
        ("can_publish", "Can publish posts"),
        ("can_archive", "Can archive posts"),
    )
```

#### Travailler avec les groupes

```python
# Créer un groupe
from django.contrib.auth.models import Group, Permission

editors_group, created = Group.objects.get_or_create(name='Editors')

# Ajouter des permissions au groupe
permissions = Permission.objects.filter(
    codename__in=['add_post', 'change_post', 'view_post']
)
editors_group.permissions.add(*permissions)

# Ajouter un utilisateur à un groupe
user.groups.add(editors_group)

# Vérifier si un utilisateur appartient à un groupe
if user.groups.filter(name='Editors').exists():
    # L'utilisateur est un éditeur
```

#### Restreindre l'accès aux vues

Avec des décorateurs pour les vues basées sur des fonctions :

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
def profile_view(request):
    # Vue accessible uniquement aux utilisateurs connectés
    return render(request, 'profile.html')

@permission_required('blog.add_post')
def add_post(request):
    # Vue accessible uniquement aux utilisateurs ayant la permission 'blog.add_post'
    return render(request, 'add_post.html')

@permission_required('blog.change_post', raise_exception=True)
def edit_post(request, post_id):
    # raise_exception=True génère une erreur 403 au lieu de rediriger vers la page de connexion
    return render(request, 'edit_post.html')
```

Avec des mixins pour les vues basées sur des classes :

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import CreateView, UpdateView

class PostCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    permission_required = 'blog.add_post'
    
    # Rediriger vers cette URL si l'utilisateur n'est pas connecté
    login_url = '/login/'
    
    # Message à afficher si l'utilisateur n'a pas la permission
    permission_denied_message = "Vous n'avez pas la permission de créer des articles."
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    fields = ['title', 'content']
    template_name = 'post_form.html'
    permission_required = 'blog.change_post'
```

### 6. Authentification avec les réseaux sociaux

L'intégration de l'authentification via réseaux sociaux peut être réalisée avec [django-allauth](https://django-allauth.readthedocs.io/) ou [python-social-auth](https://python-social-auth.readthedocs.io/).

#### Installation de django-allauth

```bash
pip install django-allauth
```

Configuration dans `settings.py` :

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # Fournisseurs spécifiques
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
    # ...
]

MIDDLEWARE = [
    # ...
    'allauth.account.middleware.AccountMiddleware',
]

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    # ...
    'allauth.account.auth_backends.AuthenticationBackend',
]

# Paramètres de allauth
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_AUTHENTICATION_METHOD = 'username_email'
```

Configuration des URLs :

```python
# urls.py
from django.urls import path, include

urlpatterns = [
    # ...
    path('accounts/', include('allauth.urls')),
]
```

### 7. Sécurité Avancée

#### Protection contre les attaques CSRF

Django inclut une protection CSRF par défaut. Assurez-vous d'utiliser `{% csrf_token %}` dans tous vos formulaires.

#### Stockage sécurisé des mots de passe

Django utilise par défaut un hachage sécurisé des mots de passe. Vous pouvez vérifier les paramètres dans `settings.py` :

```python
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]
```

#### Sessions sécurisées

```python
# settings.py
SESSION_COOKIE_SECURE = True  # Cookies uniquement via HTTPS
SESSION_COOKIE_HTTPONLY = True  # Empêche l'accès JavaScript aux cookies
SESSION_COOKIE_SAMESITE = 'Lax'  # Contrôle le comportement cross-site des cookies
```

## Exercices

### Exercice 1 : Système d'Authentification de Base

**Objectif :** Créer un système d'authentification complet avec inscription, connexion, déconnexion et profil utilisateur.

**Instructions :**

1. Créez une nouvelle application `accounts` dans votre projet Django.
2. Implémentez les vues pour l'inscription, la connexion et la déconnexion.
3. Créez un modèle `Profile` étendu avec :
   - Une photo de profil
   - Une biographie
   - Un site web
   - Les réseaux sociaux
4. Implémentez la création automatique de profil lors de l'inscription.
5. Créez les templates nécessaires pour l'authentification et le profil.
6. Ajoutez la possibilité pour l'utilisateur de modifier son profil.
7. Testez toutes les fonctionnalités.

### Exercice 2 : Réinitialisation de Mot de Passe et Vérification d'Email

**Objectif :** Ajouter la réinitialisation de mot de passe et la vérification d'email.

**Instructions :**

1. Configurez Django pour envoyer des emails (utilisez la console en développement).
2. Implémentez la fonctionnalité de réinitialisation de mot de passe.
3. Ajoutez la vérification d'email lors de l'inscription.
4. Créez les templates pour tous les emails et pages de confirmation.
5. Testez le processus complet de réinitialisation et de vérification.

### Exercice 3 : Système de Permissions et de Groupes

**Objectif :** Créer un système de blog avec différents niveaux d'utilisateurs.

**Instructions :**

1. Créez une application `blog` avec un modèle `Post`.
2. Définissez les groupes suivants :
   - Lecteurs (peuvent seulement lire)
   - Auteurs (peuvent créer et modifier leurs propres articles)
   - Éditeurs (peuvent modifier tous les articles)
   - Administrateurs (peuvent tout faire, y compris supprimer)
3. Définissez les permissions appropriées pour chaque groupe.
4. Créez des vues pour afficher, créer, modifier et supprimer des articles.
5. Restreignez l'accès aux vues en fonction des permissions.
6. Ajoutez une interface pour que les administrateurs puissent gérer les groupes et les permissions.

### Exercice 4 : Authentification à Deux Facteurs

**Objectif :** Implémenter l'authentification à deux facteurs (2FA).

**Instructions :**

1. Installez et configurez `django-two-factor-auth`.
2. Ajoutez l'option d'activation du 2FA dans le profil utilisateur.
3. Intégrez l'authentification 2FA au processus de connexion.
4. Créez un système de codes de secours pour les utilisateurs.
5. Testez le système 2FA avec différents mécanismes (TOTP, SMS, etc.).

## Ressources Supplémentaires

- [Documentation Django Authentication](https://docs.djangoproject.com/en/5.1/topics/auth/)
- [Django Allauth Documentation](https://django-allauth.readthedocs.io/)
- [Django Two-Factor Authentication](https://django-two-factor-auth.readthedocs.io/)
- [OWASP Authentication Best Practices](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html)
- [Django Security Best Practices](https://docs.djangoproject.com/en/5.1/topics/security/)
