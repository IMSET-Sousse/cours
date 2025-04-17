# TP3 : Composants et Interactivité avec Tailwind CSS

## Objectifs du TP

- Créer des composants réutilisables
- Implémenter des interactions utilisateur
- Maîtriser les états et les transitions
- Créer des animations et des effets

## 1. Composants de Base

### Boutons

```html
<button class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-offset-2">
  Bouton primaire
</button>

<button class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-gray-500 focus:ring-offset-2">
  Bouton secondaire
</button>
```

### Cartes

```html
<div class="max-w-sm rounded-lg overflow-hidden shadow-lg">
  <img class="w-full" src="image.jpg" alt="Image">
  <div class="px-6 py-4">
    <div class="font-bold text-xl mb-2">Titre de la carte</div>
    <p class="text-gray-700 text-base">
      Description de la carte avec du texte.
    </p>
  </div>
  <div class="px-6 pt-4 pb-2">
    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag1</span>
    <span class="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">#tag2</span>
  </div>
</div>
```

## 2. Interactions et États

### Hover et Focus

```html
<div class="group">
  <div class="bg-gray-100 p-4 rounded-lg group-hover:bg-blue-100 transition-colors duration-300">
    <h3 class="text-lg font-semibold group-hover:text-blue-600">Titre</h3>
    <p class="text-gray-600 group-hover:text-gray-800">Description</p>
  </div>
</div>
```

### Transitions

```html
<button class="px-4 py-2 bg-green-600 text-white rounded-lg 
                hover:bg-green-700 transform hover:scale-105 
                transition-all duration-300">
  Bouton avec transition
</button>
```

## 3. Animations

### Animations de base

```html
<div class="animate-bounce">
  Élément qui rebondit
</div>

<div class="animate-pulse">
  Élément qui pulse
</div>
```

### Transitions personnalisées

```html
<div class="group">
  <div class="transform transition-all duration-300 group-hover:scale-110">
    <img src="image.jpg" alt="Image" class="rounded-lg">
  </div>
  <div class="opacity-0 group-hover:opacity-100 transition-opacity duration-300">
    <p class="text-center mt-2">Description visible au survol</p>
  </div>
</div>
```

## 4. Exercices Pratiques

### Exercice 1 : Menu déroulant

Créez un menu déroulant avec :

- Animation d'ouverture/fermeture
- Transitions fluides
- États de survol et focus

## 5. Exercices Pratiques

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
