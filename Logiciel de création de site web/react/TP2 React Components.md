# TP 2 Les Composants React

## Objectifs

- Comprendre les différents types d'exports dans React
- Maîtriser l'organisation des composants
- Apprendre à structurer une application React
- Utiliser les bonnes pratiques d'import/export

## Prérequis

- TP1 complété
- Node.js et npm installés
- Projet React fonctionnel

## Les Exports dans React

### 1. Types d'exports

#### a. Export par défaut (Default Export)

```jsx
// Un seul export par défaut par fichier
function Welcome() {
  return <h1>Bienvenue</h1>;
}
export default Welcome;

// Import
import Welcome from './components/Welcome';
```

#### b. Export nommé (Named Export)

```jsx
// Plusieurs exports possibles
export function Button() {
  return <button>Cliquer</button>;
}
export function Input() {
  return <input type="text" />;
}

// Import
import { Button, Input } from './components/Controls';
```

### 2. Passage de Props

Les props sont un concept fondamental de React pour la communication entre composants.

```jsx
// Exemple de composant avec props
function WelcomeUser(props) {
  return (
    <div>
      <h2>Bienvenue {props.name}</h2>
      <p>Votre rôle : {props.role}</p>
    </div>
  );
}

// Utilisation
<WelcomeUser name="John" role="Admin" />
```

### 3. Organisation des composants

La bonne organisation des composants est cruciale pour maintenir un code propre et maintenable. Voici la structure recommandée :

```bash
src/
  ├── components/        # Dossier principal des composants
  │   ├── Buttons/
  │   │   ├── EqualButton.js
  │   │   ├── NumberButton.js
  │   │   ├── OperatorButton.js
  │   └── Header/
  │       ├── Navigation.js
  │       └── Logo.js

```

### 4. Exercices pratiques

#### a. Créez un composant Welcome modulaire

```jsx
// src/components/Welcome/WelcomeHeader.js
export function WelcomeHeader() {
  return <h2>Bienvenue sur notre site</h2>;
}

export function WelcomeMessage() {
  return <p>Nous sommes ravis de vous accueillir</p>;
}

// src/components/Welcome/index.js
import { WelcomeHeader, WelcomeMessage } from './WelcomeHeader';

function Welcome() {
  return (
    <div>
      <WelcomeHeader />
      <WelcomeMessage />
    </div>
  );
}

export default Welcome;
```

#### b. Créez un composant Header avec sous-composants

```jsx
// src/components/Header/Navigation.js
export function Navigation() {
  return (
    <nav>
      <ul style={{ listStyle: 'none', display: 'flex', gap: '20px' }}>
        <li>Accueil</li>
        <li>À propos</li>
        <li>Contact</li>
      </ul>
    </nav>
  );
}

// src/components/Header/Logo.js
export function Logo() {
  return <h1>Mon Site React</h1>;
}

// src/components/Header/index.js
import { Navigation } from './Navigation';
import { Logo } from './Logo';

function Header() {
  return (
    <header style={{ backgroundColor: '#282c34', padding: '20px', color: 'white' }}>
      <Logo />
      <Navigation />
    </header>
  );
}

export default Header;
```

### 5. Bonnes pratiques

1. **Nommage des fichiers**
   - Utilisez PascalCase pour les composants (ex: `Welcome.js`)
   - Utilisez camelCase pour les utilitaires (ex: `utils.js`)

2. **Organisation des imports**

   ```jsx
   // 1. Imports de React et hooks
   import { useState, useEffect } from 'react';
   
   // 2. Imports de bibliothèques tierces
   import classNames from 'classnames';
   
   // 3. Imports de composants
   import { Header } from './components';
   
   // 4. Imports d'utilitaires et styles
   import { COLORS } from './utils/styles';
   import './App.css';
   ```

3. **Un composant par fichier**
   - Facilite la maintenance
   - Améliore la lisibilité
   - Permet une meilleure réutilisation

### 6. Exercice final

Créez une application complète avec :

1. Un composant `App` principal
2. Un `Header` avec navigation
3. Une section `Welcome`
4. Un `Footer`

```jsx
// src/App.js
import Header from './components/Header';
import Welcome from './components/Welcome';
import Footer from './components/Footer';
import { COLORS } from './utils/styles';
import './App.css';

function App() {
  return (
    <div className="App" style={{ 
      minHeight: '100vh', 
      display: 'flex', 
      flexDirection: 'column',
      backgroundColor: COLORS.secondary 
    }}>
      <Header />
      <main style={{ padding: '20px' }}>
        <Welcome />
      </main>
      <Footer />
    </div>
  );
}

export default App;
```

## Points importants à retenir

1. **Exports**
   - Un seul export par défaut par fichier
   - Plusieurs exports nommés possibles
   - Les exports nommés nécessitent des accolades à l'import

2. **Organisation**
   - Structure de dossiers cohérente
   - Séparation des responsabilités
   - Composants réutilisables

3. **Bonnes pratiques**
   - Nommage clair et cohérent
   - Organisation des imports
   - Documentation du code
   - Découpage en petits composants réutilisables

## Ressources

- [Documentation officielle React](https://react.dev/)([1](https://react.dev/reference/react/Component))
- [Guide des bonnes pratiques React](https://react.dev/reference/react/apis)([2](https://react.dev/reference/react/apis))

## Conclusion

La bonne organisation des composants et la maîtrise des exports sont essentielles pour développer des applications React maintenables et évolutives.
