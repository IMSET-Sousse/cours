# TP7 : Mises en Page Avancées et Animations avec Tailwind CSS

## Objectifs du TP

- Maîtriser les mises en page complexes avec Tailwind
- Créer des animations avancées
- Implémenter des transitions fluides
- Optimiser les performances des animations

## Note sur l'Utilisation du CDN

Tous les exemples de ce TP fonctionnent avec l'installation via CDN. Assurez-vous d'avoir inclus le script Tailwind dans votre fichier HTML :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Projet avec Animations</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

## 1. Mises en Page Avancées

### Grilles Complexes

```html
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
  <div class="col-span-1 md:col-span-2 lg:col-span-3 bg-gray-100 p-6 rounded-lg">
    <h2 class="text-2xl font-bold mb-4">Article Principal</h2>
    <p>Contenu de l'article principal...</p>
  </div>
  
  <div class="bg-white p-4 rounded-lg shadow-md">
    <h3 class="text-xl font-semibold mb-2">Article Secondaire 1</h3>
    <p>Contenu secondaire...</p>
  </div>
  
  <div class="bg-white p-4 rounded-lg shadow-md">
    <h3 class="text-xl font-semibold mb-2">Article Secondaire 2</h3>
    <p>Contenu secondaire...</p>
  </div>
</div>
```

### Mise en Page Magazine

```html
<div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
  <div class="grid grid-cols-1 lg:grid-cols-12 gap-8">
    <!-- Colonne principale -->
    <main class="lg:col-span-8">
      <article class="bg-white rounded-lg shadow-lg p-6 mb-8">
        <h1 class="text-3xl font-bold mb-4">Titre de l'article</h1>
        <div class="prose max-w-none">
          <!-- Contenu de l'article -->
        </div>
      </article>
    </main>
    
    <!-- Barre latérale -->
    <aside class="lg:col-span-4">
      <div class="bg-gray-50 rounded-lg p-6">
        <h2 class="text-xl font-bold mb-4">Articles Récents</h2>
        <!-- Liste des articles récents -->
      </div>
    </aside>
  </div>
</div>
```

## 2. Animations Avancées

### Keyframes Personnalisés

```html
<style type="text/tailwindcss">
  @layer utilities {
    .animate-float {
      animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
      0%, 100% { transform: translateY(0); }
      50% { transform: translateY(-20px); }
    }
  }
</style>

<div class="animate-float bg-blue-500 text-white p-4 rounded-lg">
  Élément flottant
</div>
```

### Transitions Complexes

```html
<div class="group relative overflow-hidden rounded-lg">
  <img 
    src="image.jpg" 
    alt="Description" 
    class="w-full h-64 object-cover transform transition-transform duration-500 group-hover:scale-110"
  />
  <div class="absolute inset-0 bg-black bg-opacity-50 opacity-0 group-hover:opacity-100 transition-opacity duration-300 flex items-center justify-center">
    <p class="text-white text-xl">Texte de survol</p>
  </div>
</div>
```

## 3. Animations au Défilement

```html
<div class="space-y-8">
  <div class="transform transition-all duration-1000 opacity-0 translate-y-10" 
       data-scroll="fade-in">
    <h2 class="text-2xl font-bold mb-4">Section 1</h2>
    <p>Contenu de la section...</p>
  </div>
  
  <div class="transform transition-all duration-1000 opacity-0 translate-y-10" 
       data-scroll="fade-in">
    <h2 class="text-2xl font-bold mb-4">Section 2</h2>
    <p>Contenu de la section...</p>
  </div>
</div>

<script>
  document.addEventListener('DOMContentLoaded', () => {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.remove('opacity-0', 'translate-y-10');
        }
      });
    }, { threshold: 0.1 });

    document.querySelectorAll('[data-scroll="fade-in"]').forEach(el => {
      observer.observe(el);
    });
  });
</script>
```

## 4. Performance et Optimisation

### Optimisation des Animations

```html
<div class="transform transition-transform duration-300 hover:scale-105 will-change-transform">
  Élément avec animation optimisée
</div>

<!-- Utilisation de transform et opacity pour de meilleures performances -->
<div class="transform transition-all duration-300 hover:scale-105 hover:opacity-90">
  Élément optimisé
</div>
```

### Chargement Différé

```html
<img 
  src="image.jpg" 
  alt="Description" 
  class="w-full h-full object-cover"
  loading="lazy"
  decoding="async"
/>
```

## 5. Exercices Pratiques

### Exercice 1 : Mise en Page Magazine

1. Créez une mise en page de magazine avec :
   - Grille responsive
   - Articles principaux et secondaires
   - Barre latérale
   - Espacement approprié

### Exercice 2 : Galerie d'Images Animée

1. Développez une galerie d'images avec :
   - Effets de survol
   - Transitions fluides
   - Overlays animés
   - Chargement optimisé

### Exercice 3 : Page d'Accueil Interactive

1. Concevez une page d'accueil avec :
   - Animations au défilement
   - Sections interactives
   - Transitions fluides
   - Optimisation des performances

## Ressources supplémentaires

- [Tailwind CSS Documentation](https://tailwindcss.com/docs)
- [MDN Web Animations API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API)
- [CSS Tricks Animation Guide](https://css-tricks.com/almanac/properties/a/animation/) 