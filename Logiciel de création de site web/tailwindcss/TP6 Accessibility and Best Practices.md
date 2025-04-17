# TP6 : Accessibilité et Bonnes Pratiques avec Tailwind CSS

## Objectifs du TP

- Comprendre les principes d'accessibilité web
- Implémenter des composants accessibles avec Tailwind
- Appliquer les bonnes pratiques de développement
- Optimiser l'expérience utilisateur

## Note sur l'Utilisation du CDN

Tous les exemples de ce TP fonctionnent avec l'installation via CDN. Assurez-vous d'avoir inclus le script Tailwind dans votre fichier HTML :

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Mon Projet Accessible</title>
    <script src="https://cdn.tailwindcss.com"></script>
  </head>
  <body>
    <!-- Votre contenu ici -->
  </body>
</html>
```

## 1. Principes d'Accessibilité

### ARIA et Rôles

```html
<!-- Navigation -->
<nav aria-label="Navigation principale">
  <ul role="menubar">
    <li role="menuitem">
      <a href="/" class="text-gray-700 hover:text-blue-600">Accueil</a>
    </li>
    <li role="menuitem">
      <a href="/about" class="text-gray-700 hover:text-blue-600">À propos</a>
    </li>
  </ul>
</nav>

<!-- Formulaire -->
<form aria-labelledby="form-title" class="space-y-4">
  <h2 id="form-title" class="text-xl font-bold">Contactez-nous</h2>
  <div role="group" aria-labelledby="name-label">
    <label id="name-label" for="name" class="block text-sm font-medium text-gray-700">Nom</label>
    <input type="text" id="name" aria-required="true" class="mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500" />
  </div>
</form>
```

### Navigation au Clavier

```html
<button
  class="px-4 py-2 bg-blue-600 text-white rounded-lg 
           hover:bg-blue-700 focus:outline-none focus:ring-2 
           focus:ring-blue-500 focus:ring-offset-2"
  tabindex="0"
>
  Bouton accessible
</button>

<div class="group" tabindex="0">
  <div class="group-focus:ring-2 group-focus:ring-blue-500">
    Contenu focusable
  </div>
</div>
```

## 2. Composants Accessibles

### Boutons

```html
<button
  class="px-4 py-2 bg-blue-600 text-white rounded-lg 
           hover:bg-blue-700 focus:outline-none focus:ring-2 
           focus:ring-blue-500 focus:ring-offset-2"
  aria-label="Action principale"
>
  <span class="sr-only">Description pour lecteurs d'écran</span>
  <span aria-hidden="true">Texte visible</span>
</button>
```

### Formulaires

```html
<form class="space-y-4">
  <div>
    <label for="email" class="block text-sm font-medium text-gray-700">
      Email
    </label>
    <input
      type="email"
      id="email"
      class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
               focus:border-blue-500 focus:ring-blue-500"
      aria-describedby="email-description"
      required
    />
    <p id="email-description" class="mt-1 text-sm text-gray-500">
      Nous ne partagerons jamais votre email.
    </p>
  </div>
</form>
```

### Alertes et Messages

```html
<div
  role="alert"
  class="p-4 mb-4 text-sm text-red-700 bg-red-100 rounded-lg"
  aria-live="assertive"
>
  <span class="font-medium">Erreur !</span> Veuillez corriger les erreurs suivantes.
</div>
```

## 3. Bonnes Pratiques de Développement

### Organisation du Code

```html
<!-- Utilisation de @apply pour les styles réutilisables -->
<style type="text/tailwindcss">
  @layer components {
    .card {
      @apply p-4 bg-white rounded-lg shadow-md hover:shadow-lg 
             transition-shadow duration-300;
    }
  }
</style>

<div class="card">
  <!-- Contenu -->
</div>
```

### Performance

```html
<!-- Optimisation des images -->
<img 
  src="image.jpg" 
  alt="Description" 
  class="w-full h-full object-cover"
  loading="lazy"
/>

<!-- Optimisation des animations -->
<div class="transform transition-transform duration-300 hover:scale-105 will-change-transform">
  Élément avec animation optimisée
</div>
```

## 4. Optimisation UX

### États de Focus

```html
<button
  class="px-4 py-2 bg-blue-600 text-white rounded-lg 
           hover:bg-blue-700 focus:outline-none focus:ring-2 
           focus:ring-blue-500 focus:ring-offset-2 
           active:bg-blue-800 disabled:opacity-50 
           disabled:cursor-not-allowed"
>
  Bouton avec états
</button>
```

### Transitions et Animations

```html
<div
  class="transition-all duration-300 ease-in-out 
           hover:scale-105 focus:scale-105"
  role="button"
  tabindex="0"
>
  Élément interactif
</div>
```

## 5. Exercices Pratiques

### Exercice 1 : Formulaire Accessible

1. Créez un formulaire de contact avec :
   - Labels appropriés
   - Messages d'erreur
   - Navigation au clavier
   - États de focus

### Exercice 2 : Navigation Accessible

1. Développez une barre de navigation avec :
   - Rôles ARIA appropriés
   - Navigation au clavier
   - Indicateurs de focus
   - Support des lecteurs d'écran

### Exercice 3 : Composants Accessibles

1. Créez une série de composants avec :
   - Support ARIA
   - États interactifs
   - Messages d'état
   - Navigation au clavier

## Ressources supplémentaires

- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [ARIA Authoring Practices](https://www.w3.org/WAI/ARIA/apg/)
- [Tailwind Accessibility](https://tailwindcss.com/docs/accessibility) 