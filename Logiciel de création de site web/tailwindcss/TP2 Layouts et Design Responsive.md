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

## 4. Grilles Complexes

### Grille Magazine

```html
<div class="grid grid-cols-1 md:grid-cols-12 gap-6">
  <!-- Article principal -->
  <article class="md:col-span-8 lg:col-span-9">
    <div class="aspect-w-16 aspect-h-9 mb-6">
      <img src="main-article.jpg" alt="Article principal" class="object-cover rounded-lg" />
    </div>
    <h2 class="text-3xl font-bold mb-4">Titre de l'article principal</h2>
    <p class="text-lg text-gray-600">Contenu de l'article...</p>
  </article>

  <!-- Sidebar -->
  <aside class="md:col-span-4 lg:col-span-3">
    <div class="sticky top-4 space-y-6">
      <!-- Widget 1 -->
      <div class="bg-white p-6 rounded-lg shadow-md">
        <h3 class="text-xl font-semibold mb-4">Articles récents</h3>
        <ul class="space-y-4">
          <li>
            <a href="#" class="hover:text-blue-600">Article 1</a>
          </li>
          <li>
            <a href="#" class="hover:text-blue-600">Article 2</a>
          </li>
        </ul>
      </div>
    </div>
  </aside>
</div>
```

### Grille de Portfolio

```html
<div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
  <!-- Projet 1 -->
  <div class="group relative overflow-hidden rounded-lg">
    <img src="project1.jpg" alt="Projet 1" class="w-full h-64 object-cover" />
    <div class="absolute inset-0 bg-black bg-opacity-60 group-hover:bg-opacity-40 transition-all duration-300">
      <div class="absolute inset-0 flex items-center justify-center opacity-0 group-hover:opacity-100 transition-opacity duration-300">
        <h3 class="text-white text-xl font-bold">Projet 1</h3>
      </div>
    </div>
  </div>
  <!-- Plus de projets... -->
</div>
```

## 5. Typographie Responsive

### Échelles de Typographie

```html
<div class="prose prose-sm sm:prose lg:prose-lg xl:prose-xl">
  <h1 class="text-2xl sm:text-3xl md:text-4xl lg:text-5xl font-bold">
    Titre Responsive
  </h1>
  <p class="text-base sm:text-lg md:text-xl">
    Paragraphe avec taille de texte responsive
  </p>
</div>
```

### Espacement Responsive

```html
<div class="space-y-4 sm:space-y-6 md:space-y-8">
  <h2 class="text-xl sm:text-2xl md:text-3xl">Titre</h2>
  <p class="text-gray-600">Contenu avec espacement responsive</p>
</div>
```

## 6. Images et Médias Responsives

### Images Responsives

```html
<div class="relative">
  <!-- Image de fond responsive -->
  <div class="aspect-w-16 aspect-h-9">
    <img 
      src="image.jpg" 
      alt="Description" 
      class="object-cover w-full h-full"
      srcset="
        image-small.jpg 300w,
        image-medium.jpg 600w,
        image-large.jpg 1200w
      "
      sizes="(max-width: 640px) 300px,
             (max-width: 1024px) 600px,
             1200px"
    />
  </div>
  
  <!-- Overlay responsive -->
  <div class="absolute inset-0 bg-black bg-opacity-40 flex items-center justify-center">
    <h2 class="text-white text-2xl sm:text-3xl md:text-4xl font-bold">
      Titre sur l'image
    </h2>
  </div>
</div>
```

### Vidéo Responsive

```html
<div class="relative aspect-w-16 aspect-h-9">
  <iframe
    class="absolute inset-0 w-full h-full"
    src="https://www.youtube.com/embed/..."
    title="Video"
    allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
    allowfullscreen
  ></iframe>
</div>
```

## 7. Exercices Pratiques Supplémentaires

### Exercice 4 : Page d'Accueil Magazine

Créez une page d'accueil de magazine avec :

- Grille complexe pour les articles
- Typographie responsive
- Images adaptatives
- Sections variées

### Exercice 5 : Galerie d'Images Responsive

Réalisez une galerie avec :

- Grille adaptative
- Images optimisées
- Lightbox responsive
- Filtres adaptatifs

### Exercice 6 : Page de Produit E-commerce

Créez une page produit avec :

- Galerie d'images responsive
- Informations produit adaptatives
- Options de personnalisation
- Recommandations responsives

## 8. Projet final du TP2

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
