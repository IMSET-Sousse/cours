# TP1 : Introduction à Tailwind CSS

## Objectifs du TP

- Comprendre les bases de Tailwind CSS
- Apprendre à intégrer Tailwind CSS via CDN
- Créer sa première page web avec Tailwind CSS
- Maîtriser les classes utilitaires fondamentales

## 1. Qu'est-ce que Tailwind CSS ?

Tailwind CSS est un framework CSS utilitaire qui permet de construire rapidement des interfaces utilisateur personnalisées. Contrairement aux frameworks CSS traditionnels comme Bootstrap, Tailwind ne fournit pas de composants prédéfinis mais plutôt des classes utilitaires de bas niveau que vous pouvez utiliser pour construire votre design.

### Avantages de Tailwind CSS

- Développement rapide
- Personnalisation facile
- Pas besoin d'écrire du CSS personnalisé
- Cohérence dans le design
- Intégration simple via CDN

## 2. Installation de Tailwind CSS

### Méthode CDN (Play CDN)

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Premier Projet Tailwind</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

### Configuration via CDN

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Projet Tailwind</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              clifford: '#da373d',
            }
          }
        }
      }
    </script>
  </head>
  <body>
    <h1 class="text-3xl font-bold text-clifford">
      Hello world!
    </h1>
  </body>
</html>
```

## 3. Premiers pas avec Tailwind CSS

### Création d'une page d'accueil simple

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Ma Page d'Accueil</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body class="bg-gray-100">
    <div class="container mx-auto px-4 py-8">
      <header class="text-center mb-8">
        <h1 class="text-4xl font-bold text-blue-600 mb-4">
          Bienvenue sur mon site
        </h1>
        <p class="text-gray-600">Créé avec Tailwind CSS</p>
      </header>

      <main class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Carte 1 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h2 class="text-xl font-semibold mb-4">Première Section</h2>
          <p class="text-gray-600">
            Lorem ipsum dolor sit amet, consectetur adipiscing elit.
          </p>
        </div>

        <!-- Carte 2 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h2 class="text-xl font-semibold mb-4">Deuxième Section</h2>
          <p class="text-gray-600">
            Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
          </p>
        </div>

        <!-- Carte 3 -->
        <div class="bg-white p-6 rounded-lg shadow-md">
          <h2 class="text-xl font-semibold mb-4">Troisième Section</h2>
          <p class="text-gray-600">
            Ut enim ad minim veniam, quis nostrud exercitation ullamco.
          </p>
        </div>
      </main>
    </div>
  </body>
</html>
```

## 4. Les classes utilitaires de base

### Typographie

- `text-sm`, `text-base`, `text-lg`, `text-xl`, etc. : Tailles de texte
- `font-bold`, `font-semibold`, `font-normal` : Poids de la police
- `text-center`, `text-left`, `text-right` : Alignement du texte
- `text-blue-600`, `text-gray-600`, etc. : Couleurs de texte

### Espacement

- `p-4`, `px-4`, `py-4` : Padding
- `m-4`, `mx-4`, `my-4` : Margin
- `space-x-4`, `space-y-4` : Espacement entre les éléments

### Mise en page

- `container` : Conteneur responsive
- `flex`, `grid` : Systèmes de mise en page
- `grid-cols-1`, `grid-cols-2`, etc. : Colonnes de grille

### Couleurs et fonds

- `bg-white`, `bg-gray-100`, etc. : Couleurs de fond
- `text-white`, `text-gray-600`, etc. : Couleurs de texte

### Bordures et ombres

- `rounded-lg`, `rounded-full` : Coins arrondis
- `shadow-md`, `shadow-lg` : Ombres

## 5. Exercices pratiques

### Exercice 1 : Page de profil

Créez une page de profil personnelle avec :

- Une photo de profil
- Un nom et un titre
- Une courte biographie
- Des liens vers les réseaux sociaux

### Exercice 2 : Carte de produit

Réalisez une carte de produit avec :

- Une image
- Un titre
- Une description
- Un prix
- Un bouton d'action

### Exercice 3 : Barre de navigation

Créez une barre de navigation simple avec :

- Un logo
- Des liens de navigation
- Un bouton de connexion

## 6. Projet final du TP1

Créez une page d'accueil pour un restaurant avec :

- Une barre de navigation
- Une section héro avec image de fond
- Une section menu avec des cartes de plats
- Une section contact
- Un pied de page

## 6. Pièges Courants et Solutions

### Problèmes Fréquents avec le CDN

1. **Classes qui ne s'appliquent pas**
   - Vérifier que le script CDN est bien chargé
   - S'assurer qu'il n'y a pas d'erreurs dans la console
   - Vérifier que la configuration est correcte

2. **Styles non pris en compte**
   - Vérifier que le script CDN est dans le `<head>`
   - S'assurer que la configuration est correctement définie
   - Vérifier les erreurs dans la console

3. **Problèmes de Responsive**
   - Utiliser les bons breakpoints (sm, md, lg, xl)
   - Vérifier l'ordre des classes responsive
   - S'assurer que la meta viewport est correcte

### Debugging avec le CDN

```html
<!-- Ajouter des bordures pour debug -->
<div class="border border-red-500">
  <!-- Contenu à debugger -->
</div>

<!-- Vérifier le chargement du CDN -->
<script>
  if (typeof tailwind !== 'undefined') {
    console.log('Tailwind CSS est chargé');
  } else {
    console.error('Tailwind CSS n\'est pas chargé');
  }
</script>
```

### Outils de Debugging

1. **Extension Chrome**
   - Tailwind CSS DevTools
   - Permet de voir les classes appliquées
   - Aide à identifier les conflits

2. **VS Code**
   - Extension Tailwind CSS IntelliSense
   - Autocomplétion des classes
   - Vérification des classes valides

## 7. Exemples du Monde Réel

### Page de Produit E-commerce

```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
    <!-- Image du produit -->
    <div class="relative">
      <img src="product.jpg" alt="Produit" class="rounded-lg shadow-lg" />
      <div class="absolute top-4 right-4 bg-red-500 text-white px-2 py-1 rounded">
        -20%
      </div>
    </div>
    
    <!-- Informations produit -->
    <div class="space-y-6">
      <h1 class="text-3xl font-bold">Nom du Produit</h1>
      <div class="flex items-center space-x-4">
        <span class="text-2xl font-bold">€99.99</span>
        <span class="text-gray-500 line-through">€124.99</span>
      </div>
      <div class="flex space-x-4">
        <button class="px-6 py-3 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
          Ajouter au panier
        </button>
        <button class="px-6 py-3 border border-gray-300 rounded-lg hover:bg-gray-50">
          Favoris
        </button>
      </div>
    </div>
  </div>
</div>
```

### Page de Blog

```html
<div class="max-w-4xl mx-auto px-4 py-8">
  <!-- En-tête -->
  <header class="mb-8">
    <h1 class="text-4xl font-bold mb-4">Titre de l'article</h1>
    <div class="flex items-center space-x-4 text-gray-500">
      <span>Par Auteur</span>
      <span>•</span>
      <span>15 Mars 2024</span>
      <span>•</span>
      <span>5 min de lecture</span>
    </div>
  </header>
  
  <!-- Contenu -->
  <article class="prose max-w-none">
    <p>Introduction...</p>
    <h2>Sous-titre</h2>
    <p>Contenu...</p>
  </article>
  
  <!-- Pied de page -->
  <footer class="mt-8 pt-8 border-t">
    <div class="flex justify-between items-center">
      <div class="flex space-x-4">
        <button class="text-gray-500 hover:text-gray-700">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5" />
          </svg>
        </button>
        <button class="text-gray-500 hover:text-gray-700">
          <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 12h.01M12 12h.01M16 12h.01M21 12c0 4.418-4.03 8-9 8a9.863 9.863 0 01-4.255-.949L3 20l1.395-3.72C3.512 15.042 3 13.574 3 12c0-4.418 4.03-8 9-8s9 3.582 9 8z" />
          </svg>
        </button>
      </div>
      <button class="text-blue-600 hover:text-blue-800">
        Partager
      </button>
    </div>
  </footer>
</div>
```

## 8. Exercices Pratiques Supplémentaires

### Exercice 4 : Page de Profil

Créez une page de profil avec :

- Photo de profil avec effet de survol
- Informations personnelles
- Statistiques
- Réseaux sociaux
- Section compétences

### Exercice 5 : Dashboard

Réalisez un dashboard avec :

- Navigation latérale
- En-tête avec recherche
- Cartes de statistiques
- Graphiques
- Tableau de données

### Exercice 6 : Galerie d'Images

Créez une galerie avec :

- Grille responsive
- Filtres de catégories
- Lightbox pour l'aperçu
- Animations au survol
- Chargement progressif

## Ressources supplémentaires

- [Documentation officielle Tailwind CSS](https://tailwindcss.com/docs/installation/play-cdn)
- [Tailwind UI](https://tailwindui.com/)
- [Tailwind Components](https://tailwindcomponents.com/)
