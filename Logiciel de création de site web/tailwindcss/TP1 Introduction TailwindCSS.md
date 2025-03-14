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

### Méthode CDN

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

## Ressources supplémentaires

- [Documentation officielle Tailwind CSS](https://tailwindcss.com/docs)
- [Tailwind UI](https://tailwindui.com/)
- [Tailwind Components](https://tailwindcomponents.com/)
