# TP4 : Fonctionnalités Avancées et Optimisation avec Tailwind CSS

## Objectifs du TP

- Personnaliser l'apparence de Tailwind
- Créer des composants réutilisables
- Gérer les thèmes
- Optimiser les performances

## Note sur l'Utilisation du CDN

Tous les exemples de ce TP fonctionnent avec l'installation via CDN. Pour la personnalisation avancée, vous pouvez utiliser la configuration via CDN :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Projet Avancé</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
      tailwind.config = {
        theme: {
          extend: {
            colors: {
              primary: '#3b82f6',
              secondary: '#6b7280',
            },
            spacing: {
              '128': '32rem',
              '144': '36rem',
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

## 1. Personnalisation via CDN

### Configuration des Couleurs

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
        }
      }
    }
  }
</script>

<div class="bg-brand-light text-brand-dark">
  Contenu avec couleurs personnalisées
</div>
```

### Configuration des Espacements

```html
<script>
  tailwind.config = {
    theme: {
      extend: {
        spacing: {
          '128': '32rem',
          '144': '36rem',
        }
      }
    }
  }
</script>

<div class="p-128">
  Contenu avec espacement personnalisé
</div>
```

## 2. Composants Réutilisables

### Création de Classes Personnalisées

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

## 3. Gestion des Thèmes

### Mode Sombre avec CDN

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

<div class="bg-white dark:bg-dark-100 text-gray-900 dark:text-white">
  Contenu avec support du mode sombre
</div>
```

## 4. Optimisation des Performances

### Optimisation des Images

```html
<div class="relative">
  <img 
    src="image.jpg" 
    alt="Description" 
    class="w-full h-full object-cover"
    loading="lazy"
  />
</div>
```

### Optimisation des Animations

```html
<div class="transform transition-transform duration-300 hover:scale-105 will-change-transform">
  Élément avec animation optimisée
</div>
```

## 5. Exercices Pratiques

### Exercice 1 : Système de Design

Créez un système de design avec :

- Palette de couleurs personnalisée
- Typographie personnalisée
- Composants réutilisables
- Support du mode sombre

## Ressources supplémentaires

- [Documentation officielle Tailwind CSS](https://tailwindcss.com/docs)
- [Tailwind UI](https://tailwindui.com/)
- [Tailwind Components](https://tailwindcomponents.com/)
