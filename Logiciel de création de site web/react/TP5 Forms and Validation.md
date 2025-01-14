# TP5 - Forms & Validation

## Introduction

Les formulaires sont essentiels pour interagir avec les utilisateurs dans les applications web. React offre plusieurs façons de gérer les formulaires, notamment à travers les composants contrôlés. Ce TP vous guidera à travers la création de formulaires, la validation et la gestion des erreurs.

## 1. Composants Contrôlés

### Présentation

Dans un composant contrôlé, l'état du formulaire est géré par React. Chaque champ de formulaire a une valeur qui est stockée dans l'état du composant.

### Exemple

```jsx
import React, { useState } from 'react';

function FormulaireControle() {
  const [nom, setNom] = useState('');

  return (
    <form>
      <label>
        Nom:
        <input type="text" value={nom} onChange={(e) => setNom(e.target.value)} />
      </label>
    </form>
  );
}
```

## 2. Validation des Formulaires

### Validation de Base

Utilisez des fonctions pour valider les champs de formulaire avant de soumettre.

```jsx
function validerNom(nom) {
  return nom.length > 0;
}
```

### Gestion des Erreurs

Affichez des messages d'erreur lorsque la validation échoue.

```jsx
function FormulaireAvecValidation() {
  const [nom, setNom] = useState('');
  const [erreur, setErreur] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!validerNom(nom)) {
      setErreur('Le nom ne peut pas être vide.');
    } else {
      setErreur('');
      // Soumettre le formulaire
    }
  };

  return (
    <form onSubmit={handleSubmit}>
      <label>
        Nom:
        <input type="text" value={nom} onChange={(e) => setNom(e.target.value)} />
      </label>
      {erreur && <p style={{ color: 'red' }}>{erreur}</p>}
      <button type="submit">Soumettre</button>
    </form>
  );
}
```

## 3. Hooks pour les Formulaires

Utilisez des hooks comme `useState` pour gérer l'état des formulaires et `useEffect` pour valider les champs en temps réel.

### Exercice

Créez un formulaire de contact avec validation des champs et gestion des erreurs.
