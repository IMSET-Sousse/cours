# TP3 : Composants et Interactivité avec Tailwind CSS

## Objectifs du TP

- Créer des composants réutilisables
- Implémenter des interactions utilisateur
- Maîtriser les états (hover, focus, active)
- Créer des animations et transitions

## 1. Composants de Base

### Boutons

```html
<!-- Bouton Primaire -->
<button
  class="px-4 py-2 bg-blue-600 text-white rounded-lg 
               hover:bg-blue-700 focus:outline-none focus:ring-2 
               focus:ring-blue-500 focus:ring-offset-2 
               transition-colors duration-200"
>
  Cliquez-moi
</button>

<!-- Bouton Secondaire -->
<button
  class="px-4 py-2 bg-gray-200 text-gray-800 rounded-lg 
               hover:bg-gray-300 focus:outline-none focus:ring-2 
               focus:ring-gray-500 focus:ring-offset-2 
               transition-colors duration-200"
>
  Annuler
</button>
```

### Cartes

```html
<!-- Carte Simple -->
<div
  class="bg-white rounded-lg shadow-md p-6 
            hover:shadow-lg transition-shadow duration-300"
>
  <h3 class="text-xl font-semibold mb-4">Titre de la carte</h3>
  <p class="text-gray-600">Contenu de la carte avec effet de survol.</p>
</div>

<!-- Carte avec Image -->
<div
  class="bg-white rounded-lg shadow-md overflow-hidden 
            hover:shadow-lg transition-shadow duration-300"
>
  <img src="image.jpg" alt="Image" class="w-full h-48 object-cover" />
  <div class="p-6">
    <h3 class="text-xl font-semibold mb-2">Titre</h3>
    <p class="text-gray-600">Description</p>
  </div>
</div>
```

## 2. Formulaires

### Champs de Formulaire

```html
<form class="max-w-md mx-auto space-y-4">
  <!-- Nom -->
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1"> Nom </label>
    <input
      type="text"
      class="w-full px-3 py-2 border border-gray-300 rounded-lg 
                      focus:outline-none focus:ring-2 focus:ring-blue-500 
                      focus:border-transparent"
    />
  </div>

  <!-- Email -->
  <div>
    <label class="block text-sm font-medium text-gray-700 mb-1"> Email </label>
    <input
      type="email"
      class="w-full px-3 py-2 border border-gray-300 rounded-lg 
                      focus:outline-none focus:ring-2 focus:ring-blue-500 
                      focus:border-transparent"
    />
  </div>

  <!-- Case à cocher -->
  <div class="flex items-center">
    <input
      type="checkbox"
      class="h-4 w-4 text-blue-600 focus:ring-blue-500 
                      border-gray-300 rounded"
    />
    <label class="ml-2 block text-sm text-gray-700">
      J'accepte les conditions
    </label>
  </div>

  <!-- Bouton Submit -->
  <button
    type="submit"
    class="w-full px-4 py-2 bg-blue-600 text-white rounded-lg 
                   hover:bg-blue-700 focus:outline-none focus:ring-2 
                   focus:ring-blue-500 focus:ring-offset-2"
  >
    Envoyer
  </button>
</form>
```

## 3. Composants Interactifs

### Menu Déroulant

```html
<div class="relative inline-block text-left">
  <button
    class="px-4 py-2 bg-white border border-gray-300 rounded-lg 
                   hover:bg-gray-50 focus:outline-none focus:ring-2 
                   focus:ring-blue-500"
  >
    Options
    <svg
      class="w-5 h-5 inline-block ml-1"
      fill="none"
      stroke="currentColor"
      viewBox="0 0 24 24"
    >
      <path
        stroke-linecap="round"
        stroke-linejoin="round"
        stroke-width="2"
        d="M19 9l-7 7-7-7"
      />
    </svg>
  </button>

  <div
    class="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg 
                ring-1 ring-black ring-opacity-5"
  >
    <div class="py-1">
      <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
        Option 1
      </a>
      <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
        Option 2
      </a>
      <a href="#" class="block px-4 py-2 text-gray-700 hover:bg-gray-100">
        Option 3
      </a>
    </div>
  </div>
</div>
```

### Modal

```html
<!-- Bouton pour ouvrir le modal -->
<button
  class="px-4 py-2 bg-blue-600 text-white rounded-lg 
               hover:bg-blue-700 focus:outline-none focus:ring-2 
               focus:ring-blue-500"
>
  Ouvrir Modal
</button>

<!-- Modal -->
<div
  class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center"
>
  <div class="bg-white rounded-lg p-6 max-w-md w-full mx-4">
    <div class="flex justify-between items-center mb-4">
      <h3 class="text-xl font-semibold">Titre du Modal</h3>
      <button class="text-gray-500 hover:text-gray-700">
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
            d="M6 18L18 6M6 6l12 12"
          />
        </svg>
      </button>
    </div>
    <p class="text-gray-600 mb-4">Contenu du modal...</p>
    <div class="flex justify-end space-x-4">
      <button class="px-4 py-2 text-gray-700 hover:text-gray-900">
        Annuler
      </button>
      <button
        class="px-4 py-2 bg-blue-600 text-white rounded-lg 
                          hover:bg-blue-700 focus:outline-none focus:ring-2 
                          focus:ring-blue-500"
      >
        Confirmer
      </button>
    </div>
  </div>
</div>
```

## 4. Animations et Transitions

### Fade In

```html
<style>
  @keyframes fadeIn {
    from {
      opacity: 0;
    }
    to {
      opacity: 1;
    }
  }
  .animate-fade-in {
    animation: fadeIn 0.5s ease-in;
  }
</style>

<div class="animate-fade-in">Contenu avec animation de fondu</div>
```

### Slide In

```html
<style>
  @keyframes slideIn {
    from {
      transform: translateY(20px);
      opacity: 0;
    }
    to {
      transform: translateY(0);
      opacity: 1;
    }
  }
  .animate-slide-in {
    animation: slideIn 0.5s ease-out;
  }
</style>

<div class="animate-slide-in">Contenu avec animation de glissement</div>
```

## 5. Exercices Pratiques

### Exercice 1 : Système de Navigation

Créez un système de navigation avec :

- Menu déroulant
- Sous-menus
- Indicateurs visuels
- Animations de transition

### Exercice 2 : Système de Cartes Interactif

Réalisez un système de cartes avec :

- Effet de survol
- Animation au clic
- Modal de détails
- Transitions fluides

### Exercice 3 : Formulaire de Contact

Créez un formulaire de contact avec :

- Validation visuelle
- Messages d'erreur
- Animation de soumission
- Confirmation de succès

## 6. Projet final du TP3

Créez un tableau de bord interactif avec :

- Cartes interactives
- Graphiques animés
- Filtres dynamiques
- Notifications toast
- Modals de confirmation

## Ressources supplémentaires

- [Documentation des Transitions](https://tailwindcss.com/docs/transition-property)
- [Documentation des Animations](https://tailwindcss.com/docs/animation)
- [Documentation des États](https://tailwindcss.com/docs/hover-focus-and-other-states)
