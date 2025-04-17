# TP5 : Advanced Styling and Customization with Tailwind CSS

## Objectifs du TP

- Maîtriser la personnalisation avancée de Tailwind CSS
- Créer des thèmes personnalisés
- Développer des styles personnalisés
- Utiliser des animations et transitions avancées

## Note sur l'Utilisation du CDN

Tous les exemples de ce TP fonctionnent avec l'installation via CDN. Pour la personnalisation avancée, utilisez la configuration via CDN :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Projet Personnalisé</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              primary: {
                50: '#f0f9ff',
                100: '#e0f2fe',
                // ... jusqu'à 900
              },
              secondary: {
                light: '#f6f7f9',
                DEFAULT: '#e5e7eb',
                dark: '#d1d5db',
              },
            },
            spacing: {
              '128': '32rem',
              '144': '36rem',
            },
            borderRadius: {
              '4xl': '2rem',
            },
          }
        }
      }
    </script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

## 1. Configuration Avancée via CDN

### Personnalisation du Thème

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          brand: {
            light: '#f0f9ff',
            DEFAULT: '#3b82f6',
            dark: '#1d4ed8',
          }
        },
        fontFamily: {
          sans: ['Inter var', 'sans-serif'],
        },
      }
    }
  }
</script>

<div class="bg-brand-light text-brand-dark font-sans">
  Contenu avec thème personnalisé
</div>
```

### Styles Personnalisés

```html
<style type="text/tailwindcss">
  @layer utilities {
    .rotate-y-180 {
      transform: rotateY(180deg);
    }
    .preserve-3d {
      transform-style: preserve-3d;
    }
  }
</style>

<div class="rotate-y-180 preserve-3d">
  Élément avec transformation 3D
</div>
```

## 2. Création de Styles Personnalisés

### Styles de Base

```html
<style type="text/tailwindcss">
  @layer components {
    .btn {
      @apply px-4 py-2 rounded-lg font-semibold;
    }
    .btn-primary {
      @apply bg-blue-600 text-white hover:bg-blue-700;
    }
    .btn-secondary {
      @apply bg-gray-200 text-gray-800 hover:bg-gray-300;
    }
  }
</style>

<button class="btn btn-primary">Bouton Primaire</button>
<button class="btn btn-secondary">Bouton Secondaire</button>
```

### Styles Avancés

```html
<style type="text/tailwindcss">
  @layer components {
    .card {
      @apply bg-white rounded-lg shadow-md p-6
             hover:shadow-lg transition-shadow duration-300;
    }
    .card-header {
      @apply text-xl font-bold mb-4;
    }
    .card-body {
      @apply text-gray-600;
    }
  }
</style>

<div class="card">
  <h3 class="card-header">Titre de la carte</h3>
  <p class="card-body">Contenu de la carte...</p>
</div>
```

## 3. Animations et Transitions Avancées

### Animations Personnalisées

```html
<style type="text/tailwindcss">
  @layer utilities {
    .animate-slide-in {
      animation: slideIn 0.5s ease-out;
    }
    .animate-fade-in {
      animation: fadeIn 0.5s ease-in;
    }
  }
  
  @keyframes slideIn {
    from {
      transform: translateX(-100%);
      opacity: 0;
    }
    to {
      transform: translateX(0);
      opacity: 1;
    }
  }
  
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
</style>

<div class="animate-slide-in">Contenu avec animation</div>
```

### Transitions Complexes

```html
<div class="group relative">
  <div class="absolute inset-0 bg-black opacity-0 group-hover:opacity-50 transition-opacity duration-300"></div>
  <div class="relative z-10 transform group-hover:scale-110 transition-transform duration-300">
    <!-- Contenu -->
  </div>
</div>
```

## 4. Thèmes Dynamiques

### Toggle de Thème

```html
<script>
  tailwind.config = {
    darkMode: 'class',
    theme: {
      extend: {
        colors: {
          dark: {
            100: '#1a1a1a',
            200: '#2a2a2a',
          }
        }
      }
    }
  }
</script>

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

<div class="bg-white dark:bg-dark-100 text-gray-900 dark:text-white">
  Contenu avec thème dynamique
</div>
```

## 5. Exercices Pratiques

### Exercice 1 : Création d'un Thème Personnalisé

1. Créez un thème personnalisé avec :
   - Une palette de couleurs unique
   - Des espacements personnalisés
   - Des polices personnalisées
   - Des bordures et ombres personnalisées

### Exercice 2 : Styles Personnalisés

1. Développez des styles personnalisés pour :
   - Des animations de chargement
   - Des effets de survol
   - Des transitions de page

### Exercice 3 : Système de Design

1. Créez un système de design complet avec :
   - Des composants réutilisables
   - Des variantes de thème
   - Une documentation

## Ressources supplémentaires

- [Documentation officielle Tailwind CSS](https://tailwindcss.com/docs)
- [Tailwind UI](https://tailwindui.com/)
- [Tailwind Components](https://tailwindcomponents.com/)