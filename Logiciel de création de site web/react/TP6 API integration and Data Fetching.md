# TP6 - API Integration & Data Fetching

## Introduction

L'intégration d'API REST est cruciale pour récupérer et envoyer des données dans les applications modernes. Ce TP vous montrera comment intégrer des API, gérer les états de chargement et les erreurs.

## 1. Intégration d'API REST

### Utilisation de `fetch`

Utilisez `fetch` pour récupérer des données depuis une API.

```jsx
import React, { useState, useEffect } from 'react';

function DonneesAPI() {
  const [donnees, setDonnees] = useState([]);
  const [erreur, setErreur] = useState(null);
  const [chargement, setChargement] = useState(true);

  useEffect(() => {
    fetch('https://api.example.com/data')
      .then((response) => response.json())
      .then((data) => {
        setDonnees(data);
        setChargement(false);
      })
      .catch((error) => {
        setErreur(error);
        setChargement(false);
      });
  }, []);

  if (chargement) return <p>Chargement...</p>;
  if (erreur) return <p>Erreur: {erreur.message}</p>;

  return (
    <ul>
      {donnees.map((item) => (
        <li key={item.id}>{item.name}</li>
      ))}
    </ul>
  );
}
```

## 2. Hooks pour la Récupération de Données

Utilisez `useEffect` pour effectuer des appels API et `useState` pour gérer les données et les états de chargement.

### Gestion des Erreurs

Affichez des messages d'erreur lorsque la récupération des données échoue.

### Exercice

Intégrez une API publique et affichez les données récupérées avec gestion des erreurs et des états de chargement.
