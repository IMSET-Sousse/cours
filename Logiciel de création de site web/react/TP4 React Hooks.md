# TP4 React Hooks

## Introduction

Les Hooks de React sont des fonctions qui permettent d'utiliser l'état et d'autres fonctionnalités de React dans les composants fonctionnels. Ils simplifient la gestion de l'état et des effets secondaires, rendant le code plus lisible et maintenable, surtout pour les débutants.

## 1. useState - Gestion de l'État

### Présentation de useState

Le Hook `useState` permet d'ajouter l'état local à des composants fonctionnels. Il renvoie un tableau avec deux éléments : la valeur actuelle et une fonction pour la modifier. L'état est une manière de "mémoriser" des informations entre les rendus. C'est similaire à la gestion de l'état dans les composants de classe, mais plus simple et plus intuitif.

### Exemple de Base

```jsx
import React, { useState } from 'react';

function Counter() {
  // Déclare une nouvelle variable d'état, que nous appellerons "count"
  const [count, setCount] = useState(0);

  return (
    <div>
      <p>Compteur : {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Incrémenter
      </button>
    </div>
  );
}
```

Dans cet exemple, `useState(0)` initialise l'état avec la valeur 0. `count` est la valeur actuelle de l'état, et `setCount` est la fonction utilisée pour mettre à jour cet état.

### Exercice 1

Créez un composant TodoList qui permet d'ajouter et de supprimer des tâches en utilisant `useState`. Voici quelques étapes pour vous aider :

- **Étape 1**: Initialisez l'état avec un tableau vide pour stocker les tâches.
- **Étape 2**: Créez une fonction pour ajouter une nouvelle tâche au tableau.
- **Étape 3**: Créez une fonction pour supprimer une tâche du tableau.
- **Étape 4**: Affichez la liste des tâches dans le rendu du composant.

## 2. useEffect - Gestion des Effets Secondaires

### Présentation de useEffect

`useEffect` permet d'effectuer des effets secondaires dans les composants fonctionnels. Il est utilisé pour les opérations comme les appels API, les abonnements, ou les modifications manuelles du DOM. Il remplace les méthodes de cycle de vie des composants de classe comme `componentDidMount`, `componentDidUpdate`, et `componentWillUnmount`. Assurez-vous de bien comprendre le tableau de dépendances pour contrôler quand l'effet doit être exécuté.

### Exemple

```jsx
import React, { useState, useEffect } from 'react';

function WindowWidth() {
  const [width, setWidth] = useState(window.innerWidth);

  useEffect(() => {
    const handleResize = () => setWidth(window.innerWidth);
    window.addEventListener('resize', handleResize);
    
    // Fonction de nettoyage
    return () => {
      window.removeEventListener('resize', handleResize);
    };
  }, []); // Tableau de dépendances vide = exécution uniquement au montage

  return <p>Largeur de la fenêtre : {width}px</p>;
}
```

Dans cet exemple, `useEffect` est utilisé pour ajouter un écouteur d'événements lors du montage du composant et le supprimer lors du démontage.

### Exercice 2

Créez un composant qui utilise `useEffect` pour charger des données depuis une API au montage du composant. Voici quelques étapes pour vous aider :

- **Étape 1**: Utilisez `fetch` pour récupérer des données depuis une API.
- **Étape 2**: Stockez les données dans l'état avec `useState`.
- **Étape 3**: Affichez les données dans le rendu du composant.

## 3. useContext - Partage de Données

### Présentation de useContext

`useContext` permet de s'abonner à un contexte React et de lire sa valeur. Il est utile pour partager des données qui peuvent être considérées comme "globales" pour un arbre de composants, comme le thème ou l'utilisateur connecté. Cela simplifie le passage de données à travers l'arbre de composants sans avoir à passer explicitement des props à chaque niveau.

### Exemple de useContext

```jsx
import React, { createContext, useContext } from 'react';

const ThemeContext = createContext('light');

function ThemedButton() {
  const theme = useContext(ThemeContext);
  return (
    <button style={{ background: theme === 'dark' ? '#000' : '#fff' }}>
      Je suis stylé par le thème {theme}
    </button>
  );
}
```

Dans cet exemple, `useContext` est utilisé pour accéder à la valeur du contexte `ThemeContext`.

### Exercice 3

Implémentez un système de thème (clair/sombre) en utilisant `useContext`. Voici quelques étapes pour vous aider :

- **Étape 1**: Créez un contexte pour le thème.
- **Étape 2**: Utilisez `useContext` pour accéder au thème dans un composant.
- **Étape 3**: Changez le thème en fonction de l'état.

## Conseils Pratiques pour les Hooks

- **useState**: Assurez-vous de ne pas modifier directement l'état. Utilisez toujours la fonction de mise à jour fournie.
- **useEffect**: Faites attention aux dépendances pour éviter les boucles infinies.
- **useContext**: Utilisez-le pour éviter le "prop drilling" et simplifier le partage de données globales.

## Projet Final

Créez une application de gestion de tâches complète utilisant tous les hooks vus précédemment :

- `useState` pour la gestion des tâches
- `useEffect` pour la persistance locale
- `useContext` pour le thème

Voici quelques étapes pour vous aider :

- Commencez par créer le composant principal avec `useState` pour gérer les tâches.
- Ajoutez `useEffect` pour sauvegarder et charger les tâches depuis le stockage local.
- Implémentez un système de thème avec `useContext`.

## Ressources Supplémentaires

- [Documentation officielle React Hooks](https://react.dev/reference/react/hooks)
- [Guide des règles des Hooks](https://react.dev/warnings/invalid-hook-call-warning)
- [Tutoriel vidéo complet sur les Hooks React](https://www.youtube.com/watch?v=TNhaISOUy6Q)
