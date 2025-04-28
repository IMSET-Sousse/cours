# TP 4 : Django Forms and Form Validation

![Django Logo](./assets/django-logo.png)

## Introduction

Django Forms est un système puissant qui permet de générer des formulaires HTML, traiter les entrées utilisateur et effectuer des validations. Ce TP vous guidera à travers les concepts essentiels des formulaires Django, en vous montrant comment créer et manipuler des formulaires efficacement dans vos applications web.

## Objectifs

- Comprendre les concepts fondamentaux des formulaires Django
- Créer et manipuler des formulaires personnalisés
- Implémenter la validation côté client et côté serveur
- Utiliser les ModelForms pour simplifier les opérations CRUD
- Intégrer des formulaires dynamiques avec JavaScript

## Prérequis

- Compréhension de base de Django
- Connaissance des modèles Django et des templates
- Familiarité avec les concepts de base de HTML, CSS et JavaScript
- Un projet Django existant (vous pouvez utiliser celui des TPs précédents)

> **Ressources recommandées** :
>
> - [Documentation Django sur les Forms](https://docs.djangoproject.com/en/5.1/topics/forms/)
> - [Documentation ModelForms](https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/)
> - [MDN Web Forms Guide](https://developer.mozilla.org/en-US/docs/Learn/Forms)

## Étapes

### 1. Introduction aux Formulaires Django

#### Concepts de base

Un formulaire Django est une classe Python qui hérite de `django.forms.Form` et définit les champs que le formulaire doit contenir. Chaque type de champ (texte, nombre, email, etc.) est représenté par une classe spécifique.

```python
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
```

#### Rendu des formulaires dans un template

Django fournit différentes méthodes pour afficher un formulaire dans un template :

```html
<form method="post">
    {% csrf_token %}
    
    <!-- Affichage complet automatique -->
    {{ form.as_p }}
    
    <!-- Ou affichage personnalisé champ par champ -->
    <div class="form-group">
        <label for="{{ form.name.id_for_label }}">Nom :</label>
        {{ form.name }}
        {% if form.name.errors %}
            <div class="error">{{ form.name.errors }}</div>
        {% endif %}
    </div>
    
    <button type="submit">Envoyer</button>
</form>
```

#### Traitement des données dans une vue

```python
def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Traitement des données valides
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            # Faites quelque chose avec les données (envoi d'email, etc.)
            # ...
            
            return redirect('success_page')
    else:
        form = ContactForm()  # Formulaire vide pour GET
    
    return render(request, 'contact.html', {'form': form})
```

### 2. Création de Formulaires Personnalisés

#### Définition de widgets personnalisés

Les widgets contrôlent le rendu HTML des champs de formulaire. Vous pouvez personnaliser leur apparence :

```python
class FancyContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Votre nom'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'votre@email.com'
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'rows': 4,
            'placeholder': 'Votre message...'
        })
    )
```

#### Utilisation de différents types de champs

Django propose de nombreux types de champs adaptés à différents besoins :

```python
class AdvancedForm(forms.Form):
    # Champs de base
    name = forms.CharField(max_length=100)
    age = forms.IntegerField(min_value=0, max_value=120)
    
    # Champs de sélection
    CHOICES = [('FR', 'France'), ('US', 'États-Unis'), ('CA', 'Canada')]
    country = forms.ChoiceField(choices=CHOICES)
    
    # Champs de date et heure
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    
    # Case à cocher
    newsletter = forms.BooleanField(required=False)
    
    # Fichiers
    profile_picture = forms.ImageField(required=False)
```

### 3. Validation des Formulaires

#### Validation côté serveur

Django effectue automatiquement des validations basées sur le type de champ. Vous pouvez ajouter des validations personnalisées :

```python
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator

# Validateur personnalisé
def validate_starts_with_a(value):
    if not value.lower().startswith('a'):
        raise ValidationError('Le texte doit commencer par la lettre A.')

class MyForm(forms.Form):
    # Validation intégrée
    code = forms.CharField(
        validators=[RegexValidator(r'^[A-Z]{3}\d{4}$', 'Le code doit être au format XXX0000.')]
    )
    
    # Validation avec fonction personnalisée
    special_field = forms.CharField(validators=[validate_starts_with_a])
    
    # Validation dans une méthode de nettoyage de champ spécifique
    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 3:
            raise ValidationError('Le nom doit contenir au moins 3 caractères.')
        return name
    
    # Validation impliquant plusieurs champs
    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')
        
        if start_date and end_date and start_date > end_date:
            raise ValidationError('La date de fin doit être après la date de début.')
        
        return cleaned_data
```

#### Validation côté client

La validation côté client améliore l'expérience utilisateur. Vous pouvez utiliser HTML5 et JavaScript :

```python
class ClientValidatedForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'required': True,
            'pattern': '[A-Za-z ]+',
            'title': 'Lettres uniquement'
        })
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'required': True
        })
    )
    phone = forms.CharField(
        widget=forms.TextInput(attrs={
            'pattern': '\\d{10}',
            'title': '10 chiffres sans espaces'
        })
    )
```

```html
<!-- Dans votre template, ajoutez le JavaScript de validation -->
<script>
    document.addEventListener('DOMContentLoaded', function() {
        const form = document.querySelector('#my-form');
        
        form.addEventListener('submit', function(event) {
            const nameField = form.querySelector('#id_name');
            
            if (nameField.value.length < 3) {
                event.preventDefault();
                alert('Le nom doit avoir au moins 3 caractères.');
            }
        });
    });
</script>
```

### 4. ModelForms - Formulaires liés aux modèles

Les ModelForms sont des formulaires qui sont automatiquement générés à partir de vos modèles Django.

#### Création d'un ModelForm

```python
from django import forms
from .models import Article, Comment

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'tags']
        # Ou utilisez '__all__' pour inclure tous les champs
        # fields = '__all__'
        # Ou exclude pour exclure certains champs
        # exclude = ['author', 'created_at']
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
        }
        
        labels = {
            'title': 'Titre de l\'article',
            'content': 'Contenu',
        }
        
        help_texts = {
            'tags': 'Séparez les tags par des virgules.',
        }
```

#### Utilisation dans une vue CRUD

```python
def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            # Pour personnaliser avant la sauvegarde
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            # Pour sauvegarder les relations ManyToMany
            form.save_m2m()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm()
    
    return render(request, 'create_article.html', {'form': form})

def update_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('article_detail', pk=article.pk)
    else:
        form = ArticleForm(instance=article)
    
    return render(request, 'update_article.html', {'form': form})
```

### 5. Formulaires Avancés

#### Formulaires avec des ensembles de champs (formsets)

Les formsets permettent de gérer plusieurs instances du même formulaire :

```python
from django.forms import formset_factory, modelformset_factory

# Formset basique
CommentFormSet = formset_factory(CommentForm, extra=3)

# Dans votre vue
def add_comments(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    
    if request.method == 'POST':
        formset = CommentFormSet(request.POST)
        if formset.is_valid():
            for form in formset:
                if form.cleaned_data:  # Vérifie si le formulaire n'est pas vide
                    comment = form.save(commit=False)
                    comment.article = article
                    comment.save()
            return redirect('article_detail', pk=article_id)
    else:
        formset = CommentFormSet()
    
    return render(request, 'add_comments.html', {'formset': formset})

# ModelFormset - travaille directement avec des instances de modèle
ArticleFormSet = modelformset_factory(
    Article, 
    fields=['title', 'content'],
    extra=2
)

# Inline Formset - pour les relations parent-enfant
from django.forms import inlineformset_factory

ArticleCommentFormset = inlineformset_factory(
    Article, Comment,
    fields=['author_name', 'content'],
    extra=2,
    can_delete=True
)
```

#### Intégration avec JavaScript pour des formulaires dynamiques

Exemple d'intégration avec JavaScript pour ajouter/supprimer des champs dynamiquement :

```html
<form method="post" id="dynamic-form">
    {% csrf_token %}
    {{ form.as_p }}
    
    <div id="form-container">
        {{ formset.management_form }}
        {% for form in formset %}
            <div class="formset-row">
                {{ form.as_p }}
                <button type="button" class="remove-form">Supprimer</button>
            </div>
        {% endfor %}
    </div>
    
    <button type="button" id="add-form">Ajouter un élément</button>
    <button type="submit">Enregistrer</button>
</form>

<script>
    document.addEventListener('DOMContentLoaded', function() {
        const container = document.querySelector('#form-container');
        const addButton = document.querySelector('#add-form');
        
        // Récupère le nombre total de formulaires
        const totalForms = document.querySelector('#id_form-TOTAL_FORMS');
        
        // Ajoute un nouveau formulaire
        addButton.addEventListener('click', function() {
            const formCount = parseInt(totalForms.value);
            const newForm = document.querySelector('.formset-row').cloneNode(true);
            
            // Met à jour les indices
            newForm.innerHTML = newForm.innerHTML.replace(/form-(\d+)/g, `form-${formCount}`);
            newForm.innerHTML = newForm.innerHTML.replace(/id_form-(\d+)/g, `id_form-${formCount}`);
            
            // Vide les champs
            newForm.querySelectorAll('input, textarea').forEach(input => {
                input.value = '';
            });
            
            container.appendChild(newForm);
            totalForms.value = formCount + 1;
        });
        
        // Supprime un formulaire
        container.addEventListener('click', function(e) {
            if (e.target.classList.contains('remove-form')) {
                e.target.closest('.formset-row').remove();
                
                // Met à jour le nombre total de formulaires
                const forms = container.querySelectorAll('.formset-row');
                totalForms.value = forms.length;
                
                // Réindexe les formulaires
                forms.forEach((form, index) => {
                    form.innerHTML = form.innerHTML.replace(/form-(\d+)/g, `form-${index}`);
                    form.innerHTML = form.innerHTML.replace(/id_form-(\d+)/g, `id_form-${index}`);
                });
            }
        });
    });
</script>
```

### 6. Utilisation de Crispy Forms pour l'amélioration des formulaires

Le package `django-crispy-forms` permet d'améliorer l'apparence et la gestion des formulaires :

```bash
pip install django-crispy-forms
```

Configuration dans `settings.py` :

```python
INSTALLED_APPS = [
    # ...
    'crispy_forms',
    'crispy_bootstrap5',  # Si vous utilisez Bootstrap 5
]

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'
CRISPY_TEMPLATE_PACK = 'bootstrap5'
```

Utilisation dans les formulaires :

```python
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class CrispyArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content', 'category', 'is_published']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                Column('category', css_class='form-group col-md-6 mb-0'),
                css_class='form-row'
            ),
            'content',
            'is_published',
            Submit('submit', 'Enregistrer', css_class='btn btn-primary')
        )
```

Dans le template :

```html
{% load crispy_forms_tags %}

<form method="post">
    {% csrf_token %}
    {% crispy form %}
    <!-- Le bouton Submit est déjà inclus dans le formulaire grâce à crispy_forms -->
</form>
```

## Exercices

### Exercice 1 : Formulaire de Contact

**Objectif :** Créer un formulaire de contact avec validation.

**Instructions :**

1. Créez une nouvelle application `contact` dans votre projet Django
2. Définissez un formulaire `ContactForm` avec les champs suivants :
   - Nom (obligatoire, max 100 caractères)
   - Email (obligatoire, format email)
   - Sujet (obligatoire, max 200 caractères)
   - Message (obligatoire, widget Textarea)
   - Type de demande (ChoiceField avec options : Question, Problème, Suggestion)
3. Ajoutez des validations personnalisées :
   - Le nom doit contenir au moins 3 caractères
   - Le sujet ne doit pas contenir certains mots (ex : "spam", "publicité")
4. Créez une vue pour afficher et traiter le formulaire
5. Créez des templates pour afficher le formulaire et une page de confirmation
6. Configurez les URLs nécessaires

### Exercice 2 : CRUD pour un Blog avec ModelForms

**Objectif :** Créer un système CRUD complet pour un blog en utilisant des ModelForms.

**Instructions :**

1. Créez un modèle `Post` avec les champs :
   - Titre
   - Contenu
   - Auteur (ForeignKey vers User)
   - Date de création
   - Catégorie (ForeignKey vers une table Catégorie)
   - Tags (ManyToManyField vers une table Tag)
   - Image de couverture (ImageField, optionnel)
   - Statut (ChoiceField : Brouillon, Publié)

2. Créez un ModelForm pour ce modèle avec :
   - Des widgets personnalisés pour chaque champ
   - Des labels et help_texts pour guider l'utilisateur
   - Des validations supplémentaires

3. Implémentez des vues pour :
   - Créer un article
   - Lire (détail et liste)
   - Mettre à jour
   - Supprimer

4. Créez les templates nécessaires avec une interface responsive

### Exercice 3 : Formulaire Dynamique avec JavaScript

**Objectif :** Créer un formulaire de commande avec des champs dynamiques.

**Instructions :**

1. Créez un modèle `Order` (Commande) et `OrderItem` (Produit commandé)

2. Utilisez un formset inline pour permettre à l'utilisateur d'ajouter plusieurs produits à une commande

3. Implémentez du JavaScript pour :
   - Ajouter/supprimer dynamiquement des produits
   - Mettre à jour automatiquement le prix total
   - Valider les quantités (doit être supérieur à 0)

4. Ajoutez des styles pour améliorer l'interface utilisateur

### Exercice 4 : Formulaire d'Inscription avec Validation Complète

**Objectif :** Créer un formulaire d'inscription utilisateur complet.

**Instructions :**

1. Créez un formulaire d'inscription avec les champs :
   - Nom d'utilisateur
   - Email
   - Mot de passe
   - Confirmation de mot de passe
   - Date de naissance
   - Photo de profil
   - Biographie

2. Implémentez des validations côté serveur :
   - Vérification que le nom d'utilisateur n'est pas déjà pris
   - Validation de la complexité du mot de passe
   - Vérification que les mots de passe correspondent
   - Vérification de l'âge minimal (18 ans)
   - Limitation de la taille et du type des fichiers pour la photo de profil

3. Ajoutez des validations côté client avec JavaScript

4. Intégrez le formulaire dans une interface à étapes multiples (multi-step form)

5. Ajoutez une confirmation par email après l'inscription

## Ressources Supplémentaires

- [Documentation Django sur les Forms](https://docs.djangoproject.com/en/5.1/topics/forms/)
- [Documentation ModelForms](https://docs.djangoproject.com/en/5.1/topics/forms/modelforms/)
- [Documentation sur la validation des formulaires](https://docs.djangoproject.com/en/5.1/ref/forms/validation/)
- [Django Crispy Forms](https://django-crispy-forms.readthedocs.io/en/latest/)
- [MDN Web Forms Guide](https://developer.mozilla.org/en-US/docs/Learn/Forms)
