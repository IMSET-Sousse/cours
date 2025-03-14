# TP4 : Fonctionnalités Avancées avec Tailwind CSS

## Objectifs du TP

- Personnaliser l'apparence avec Tailwind
- Créer des composants réutilisables
- Gérer les thèmes et le mode sombre
- Optimiser le code pour de meilleures performances

## 1. Personnalisation avec Tailwind

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
              brand: "#3b82f6",
              "brand-dark": "#2563eb",
            },
            spacing: {
              128: "32rem",
              144: "36rem",
            },
          },
        },
      };
    </script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

### Variables CSS Personnalisées

```html
<style>
  :root {
    --color-primary: #3b82f6;
    --color-secondary: #6b7280;
  }
</style>
```

## 2. Mode Sombre

### Configuration du Mode Sombre

```html
<!DOCTYPE html>
<html class="dark">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mode Sombre</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

### Classes Conditionnelles

```html
<div
  class="bg-white dark:bg-gray-800 
            text-gray-900 dark:text-white"
>
  Contenu adaptatif
</div>
```

### Toggle du Mode Sombre

```html
<button
  class="p-2 rounded-lg bg-gray-200 dark:bg-gray-700"
  onclick="document.documentElement.classList.toggle('dark')"
>
  <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
    <path
      stroke-linecap="round"
      stroke-linejoin="round"
      stroke-width="2"
      d="M20.354 15.354A9 9 0 018.646 3.646 9.003 9.003 0 0012 21a9.003 9.003 0 008.354-5.646z"
    />
  </svg>
</button>
```

## 3. Composants Réutilisables

### Classes Personnalisées

```html
<style>
  .btn-primary {
    @apply px-4 py-2 bg-blue-600 text-white rounded-lg 
               hover:bg-blue-700 focus:outline-none focus:ring-2 
               focus:ring-blue-500 focus:ring-offset-2 
               transition-colors duration-200;
  }

  .card {
    @apply bg-white rounded-lg shadow-md p-6 
               hover:shadow-lg transition-shadow duration-300;
  }
</style>
```

### Utilisation

```html
<button class="btn-primary">Cliquez-moi</button>
<div class="card">
  <h3>Titre de la carte</h3>
  <p>Contenu...</p>
</div>
```

## 4. Optimisation des Performances

### Optimisation des Images

```html
<picture>
  <source media="(min-width: 768px)" srcset="image-large.jpg" />
  <img src="image-small.jpg" alt="Image responsive" class="w-full h-auto" />
</picture>
```

### Lazy Loading

```html
<img src="image.jpg" alt="Image" loading="lazy" class="w-full h-auto" />
```

## 5. Bonnes Pratiques

### Organisation des Classes

```html
<!-- À éviter -->
<div
  class="p-4 bg-white rounded-lg shadow-md hover:shadow-lg 
            transition-shadow duration-300 flex items-center 
            justify-between space-x-4"
>
  <!-- À privilégier -->
  <div class="card flex items-center justify-between space-x-4"></div>
</div>
```

### Extensions de Thème

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        fontFamily: {
          sans: ["Inter var", "sans-serif"],
        },
        animation: {
          "bounce-slow": "bounce 3s infinite",
        },
      },
    },
  };
</script>
```

## 6. Exercices Pratiques

1. Créez un système de thème complet avec :

   - Mode clair/sombre
   - Variables CSS personnalisées
   - Composants réutilisables
   - Transitions fluides

2. Optimisez une page web avec :

   - Images responsives
   - Lazy loading
   - Classes optimisées
   - Transitions performantes

3. Créez une bibliothèque de composants avec :
   - Classes personnalisées
   - Variantes
   - Documentation
   - Exemples d'utilisation

## Ressources supplémentaires

- [Documentation officielle Tailwind CSS](https://tailwindcss.com/docs)
- [Tailwind UI](https://tailwindui.com/)
- [Tailwind Components](https://tailwindcomponents.com/)
