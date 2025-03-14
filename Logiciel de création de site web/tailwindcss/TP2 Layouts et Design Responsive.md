# TP2 : Layouts et Design Responsive avec Tailwind CSS

## Objectifs du TP

- Maîtriser les systèmes de mise en page Flexbox et Grid
- Comprendre et implémenter le design responsive
- Créer des layouts complexes et adaptatifs
- Utiliser les breakpoints et classes conditionnelles

## 1. Systèmes de mise en page

### Flexbox

```html
<!-- Container Flex -->
<div class="flex flex-col md:flex-row gap-4">
  <!-- Éléments flexibles -->
  <div class="flex-1 bg-blue-100 p-4">Élément 1</div>
  <div class="flex-1 bg-green-100 p-4">Élément 2</div>
  <div class="flex-1 bg-red-100 p-4">Élément 3</div>
</div>

<!-- Alignement Flex -->
<div class="flex items-center justify-between">
  <div>Logo</div>
  <nav class="flex space-x-4">
    <a href="#">Accueil</a>
    <a href="#">À propos</a>
    <a href="#">Contact</a>
  </nav>
</div>
```

### Grid

```html
<!-- Grid Simple -->
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
  <div class="bg-gray-100 p-4">Colonne 1</div>
  <div class="bg-gray-100 p-4">Colonne 2</div>
  <div class="bg-gray-100 p-4">Colonne 3</div>
</div>

<!-- Grid Complexe -->
<div class="grid grid-cols-1 md:grid-cols-12 gap-4">
  <div class="md:col-span-8 bg-blue-100 p-4">Contenu principal</div>
  <div class="md:col-span-4 bg-green-100 p-4">Sidebar</div>
</div>
```

## 2. Design Responsive

### Breakpoints Tailwind

- `sm`: 640px
- `md`: 768px
- `lg`: 1024px
- `xl`: 1280px
- `2xl`: 1536px

### Exemple de Navigation Responsive

```html
<nav class="bg-white shadow-lg">
  <div class="max-w-6xl mx-auto px-4">
    <div class="flex justify-between items-center">
      <!-- Logo -->
      <div class="flex items-center">
        <a href="#" class="text-xl font-bold">Logo</a>
      </div>

      <!-- Menu Desktop -->
      <div class="hidden md:flex space-x-8">
        <a href="#" class="text-gray-700 hover:text-blue-600">Accueil</a>
        <a href="#" class="text-gray-700 hover:text-blue-600">Services</a>
        <a href="#" class="text-gray-700 hover:text-blue-600">Contact</a>
      </div>

      <!-- Menu Mobile -->
      <div class="md:hidden">
        <button class="text-gray-700 hover:text-blue-600">
          <svg
            class="w-6 h-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              stroke-linecap="round"
              stroke-linejoin="round"
              stroke-width="2"
              d="M4 6h16M4 12h16M4 18h16"
            />
          </svg>
        </button>
      </div>
    </div>
  </div>
</nav>
```

## 3. Layouts Complexes

### Layout de Blog

```html
<div class="max-w-6xl mx-auto px-4 py-8">
  <!-- En-tête -->
  <header class="text-center mb-12">
    <h1 class="text-4xl font-bold mb-4">Mon Blog</h1>
    <p class="text-gray-600">Articles et actualités</p>
  </header>

  <!-- Contenu principal -->
  <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
    <!-- Articles -->
    <div class="lg:col-span-2 space-y-8">
      <!-- Article 1 -->
      <article class="bg-white rounded-lg shadow-md overflow-hidden">
        <img src="image.jpg" alt="Article" class="w-full h-48 object-cover" />
        <div class="p-6">
          <h2 class="text-xl font-semibold mb-2">Titre de l'article</h2>
          <p class="text-gray-600 mb-4">Description de l'article...</p>
          <a href="#" class="text-blue-600 hover:text-blue-800">Lire plus →</a>
        </div>
      </article>
    </div>

    <!-- Sidebar -->
    <div class="lg:col-span-1">
      <div class="bg-white rounded-lg shadow-md p-6">
        <h3 class="text-lg font-semibold mb-4">À propos</h3>
        <p class="text-gray-600">Informations sur le blog...</p>
      </div>
    </div>
  </div>
</div>
```

## 4. Techniques Avancées

### Aspect Ratio

```html
<div class="aspect-w-16 aspect-h-9">
  <img src="video-thumbnail.jpg" alt="Video" class="object-cover" />
</div>
```

### Positionnement

```html
<!-- Position relative -->
<div class="relative">
  <!-- Position absolue -->
  <div class="absolute top-0 right-0 bg-red-500 text-white px-2 py-1">
    Nouveau
  </div>
  <!-- Contenu -->
  <div class="p-4">Contenu</div>
</div>
```

### Z-index

```html
<div class="relative">
  <div class="absolute inset-0 bg-black opacity-50 z-10"></div>
  <div class="relative z-20 bg-white p-4">Contenu</div>
</div>
```

## 5. Exercices Pratiques

### Exercice 1 : Page de Dashboard

Créez un dashboard responsive avec :

- Une barre latérale rétractable
- Un en-tête avec recherche
- Des cartes de statistiques
- Un tableau de données
- Un graphique

### Exercice 2 : Galerie d'Images

Réalisez une galerie d'images responsive avec :

- Une grille adaptative
- Des images avec effet de survol
- Un modal pour l'aperçu
- Des filtres de catégories

### Exercice 3 : Page de Produit E-commerce

Créez une page de produit avec :

- Une galerie d'images
- Des informations produit
- Des options de personnalisation
- Un panier flottant

## 6. Projet final du TP2

Créez un site de portfolio responsive avec :

- Une navigation adaptative
- Une section héro avec animation
- Une grille de projets
- Un formulaire de contact
- Un pied de page

## Ressources supplémentaires

- [Documentation Flexbox](https://tailwindcss.com/docs/flex)
- [Documentation Grid](https://tailwindcss.com/docs/grid)
- [Documentation Responsive Design](https://tailwindcss.com/docs/responsive-design)
