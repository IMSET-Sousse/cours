# TP 3 Styling in React

## Objectifs

- Comprendre les différentes approches de styling dans React
- Maîtriser l'utilisation des CSS Modules
- Apprendre à utiliser le styling inline de manière appropriée
- Comprendre l'utilisation des bibliothèques CSS-in-JS
- Implémenter des styles conditionnels
- Appliquer les bonnes pratiques de performance

## Prérequis

- TP1 et TP2 complétés
- Connaissances de base en CSS
- Projet React fonctionnel

## Les Approches de Styling dans React

### 1. CSS Traditionnel

#### a. CSS Global

```css
/* src/styles/global.css */
.button {
  padding: 10px 20px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.button-primary {
  background-color: #007bff;
  color: white;
}
```

```jsx
import './styles/global.css';

function Button() {
  return (
    <button className="button button-primary">
      Cliquer
    </button>
  );
}
```

#### b. CSS Modules (Recommandé)

```css
/* src/components/Button/Button.module.css */
.button {
  padding: 10px 20px;
  border-radius: 4px;
  border: none;
  cursor: pointer;
}

.primary {
  background-color: #007bff;
  color: white;
}
```

```jsx
import styles from './Button.module.css';
import classNames from 'classnames';

function Button({ variant = 'primary', isDisabled }) {
  return (
    <button 
      className={classNames(styles.button, {
        [styles.primary]: variant === 'primary',
        [styles.disabled]: isDisabled
      })}
    >
      Cliquer
    </button>
  );
}
```

### 2. Inline Styling (Pour les styles dynamiques)

```jsx
function DynamicCard({ height, backgroundColor }) {
  // ⚠️ Utilisez le style inline uniquement pour les valeurs dynamiques
  const cardStyle = {
    height,
    backgroundColor,
    padding: '20px',
    borderRadius: '8px',
  };

  return (
    <div style={cardStyle}>
      Contenu dynamique
    </div>
  );
}
```

### 3. Système de Thème

```jsx
// src/styles/theme.js
export const theme = {
  colors: {
    primary: '#007bff',
    secondary: '#6c757d',
    success: '#28a745',
    error: '#dc3545'
  },
  spacing: {
    sm: '8px',
    md: '16px',
    lg: '24px'
  },
  typography: {
    h1: '2rem',
    h2: '1.5rem',
    body: '1rem'
  }
};

// Utilisation avec CSS Modules
/* src/components/Button/Button.module.css */
.button {
  padding: var(--spacing-md);
  font-size: var(--typography-body);
  background-color: var(--color-primary);
}
```

### 4. Exercices Pratiques

#### a. Créez un composant Card avec CSS Modules

```jsx
// src/components/Card/Card.module.css
.card {
  padding: var(--spacing-md);
  border-radius: 8px;
  background-color: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.title {
  font-size: var(--typography-h2);
  color: var(--color-primary);
  margin-bottom: var(--spacing-sm);
}

// src/components/Card/index.jsx
import styles from './Card.module.css';

function Card({ title, children }) {
  return (
    <div className={styles.card}>
      <h2 className={styles.title}>{title}</h2>
      <div>{children}</div>
    </div>
  );
}
```

### 5. Bonnes Pratiques

1. **Performance**
   - Préférez les CSS Modules aux styles inline
   - Évitez de créer des objets de style à chaque rendu
   - Utilisez `memo` pour les composants avec styles complexes

2. **Organisation**
   - Un fichier CSS Module par composant
   - Variables CSS pour les valeurs réutilisables
   - Séparation des styles globaux et locaux

3. **Accessibilité**
   - Utilisez des contrastes suffisants
   - Maintenez une hiérarchie visuelle claire
   - Testez avec différents zooms

4. **Responsive Design**

   ```css
   .container {
     --columns: 1;
     display: grid;
     grid-template-columns: repeat(var(--columns), 1fr);
   }

   @media (min-width: 768px) {
     .container {
       --columns: 2;
     }
   }
   ```

## Points Importants à Retenir

1. **Choix de l'approche**
   - CSS Modules pour l'isolation et la maintenabilité
   - Styles inline uniquement pour les valeurs dynamiques
   - Variables CSS pour la cohérence

2. **Performance**
   - Évitez la génération de styles à chaque rendu
   - Utilisez les CSS Modules pour une meilleure performance
   - Optimisez les re-renders avec `memo` si nécessaire

3. **Maintenance**
   - Organisation claire des fichiers CSS
   - Utilisation de variables pour la cohérence
   - Documentation des styles complexes

## Ressources

- [Documentation React sur le styling](https://react.dev/reference/react-dom/components/common#applying-css-styles)([1](https://react.dev/reference/react-dom/components/common))
- [Guide CSS Modules](https://github.com/css-modules/css-modules)

## Conclusion

La maîtrise des différentes approches de styling dans React est essentielle pour créer des interfaces utilisateur performantes et maintenables. Les CSS Modules offrent un excellent compromis entre isolation, performance et maintenabilité.
