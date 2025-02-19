# TP 1 : Introduction à Next.js (Version 15)

## Introduction

Next.js est un framework React innovant qui permet de construire des applications web modernes, rapides et performantes tout en simplifiant la configuration grâce à son approche "batteries incluses". La version 15 apporte des améliorations importantes en termes de performance (grâce à Turbopack Dev, Fast Refresh optimisé, etc.) et de stabilité pour des projets en production.
Ce TP a pour objectif de vous initier aux bases de Next.js, de vous guider dans la création d'une application simple et de vous préparer à explorer ses fonctionnalités avancées par la suite.

## Objectifs

- Installer Node.js et npm
- Créer une nouvelle application Next.js
- Comprendre la structure d'un projet Next.js
- Lancer et tester l'application
- Effectuer des modifications basiques
- Comprendre les composants essentiels

## Prérequis

- Un éditeur de code (VS Code recommandé)
- Un terminal de commande
- Une connexion internet
- Connaissances de base en HTML, CSS, JavaScript et React ([1](https://nextjs.org/docs))

> **Ressources recommandées** :
>
> - [HTML & CSS](https://www.w3schools.com/html/)
> - [JavaScript](https://www.javascript.com/)
> - [React](https://reactjs.org/)

## Étapes

### 1. Installation de Node.js et npm

1. Téléchargez et installez Node.js depuis [nodejs.org](https://nodejs.org/)
   - Version 15.x ou ultérieure requise ([2](https://nextjs.org/docs/app/getting-started/installation))
   - Choisissez la version LTS (Long Term Support)

2. Vérifiez l'installation en ouvrant un terminal :

   Pour vérifier Node.js :

   ```powershell
   node --version
   ```

   Cette commande affiche la version de Node.js installée, confirmant que l'installation s'est bien déroulée.

   Pour vérifier npm :

   ```powershell
   npm --version
   ```

   npm (Node Package Manager) est le gestionnaire de paquets de Node.js. Il permet d'installer, de gérer et de partager des packages JavaScript. C'est l'outil principal pour installer les dépendances de votre projet Next.js.

   Pour vérifier npx :

   ```powershell
   npx --version
   ```

   npx est un exécuteur de paquets npm qui permet d'exécuter des packages sans avoir à les installer globalement. Il est particulièrement utile pour exécuter des commandes ponctuelles comme create-next-app, qui ne nécessitent pas une installation permanente sur votre système.

### 2. Configuration de l'environnement de développement

1. Installez VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/)
2. Installez les extensions recommandées :
   - ESLint (validation du code) ([3](https://nextjs.org/docs/app/building-your-application/configuring/eslint))
   - ES7+ React/Redux/React-Native snippets
   - Prettier (formatage du code)
   - Next.js extension (support TypeScript et auto-complétion) ([4](https://nextjs.org/docs/app/getting-started/installation))

### 3. Création d'une nouvelle application Next.js

1. Ouvrez un terminal et naviguez vers le dossier où vous souhaitez créer votre projet

   Par exemple, si vous voulez créer votre projet sur le Bureau :

   ```powershell
   cd C:\Users\VotreNom\Desktop
   ```

   > **Note** : Ne copiez pas exactement ces commandes ! Remplacez "VotreNom" par votre nom d'utilisateur Windows, ou naviguez vers le dossier de votre choix.

2. Créez une nouvelle application Next.js ([2](https://nextjs.org/docs/app/getting-started/installation)) :

   ```powershell
   npx create-next-app@latest
   ```

3. Répondez aux questions de configuration :

   ```powershell
   What is your project named? mon-app
   Would you like to use TypeScript? No
   Would you like to use ESLint? Yes
   Would you like to use Tailwind CSS? No
   Would you like your code inside a `src/` directory? No
   Would you like to use App Router? (recommended) Yes
   Would you like to use Turbopack for `next dev`? Yes
   Would you like to customize the import alias (@/* by default)? No
   ```

### 4. Structure du projet Next.js

Explorez la structure de base de votre projet :

```text
mon-app/
  ├── app/                    # Dossier principal de l'application
  │   ├── components/        # Dossier pour les composants réutilisables
  │   │   ├── Navigation.jsx # Composant de navigation
  │   │   └── Counter.jsx    # Composant de compteur
  │   ├── layout.jsx         # Layout racine (structure globale HTML)
  │   ├── page.jsx          # Page d'accueil
  │   └── globals.css       # Styles globaux
  ├── public/               # Fichiers statiques (images, fonts, etc.)
  ├── node_modules/         # Dépendances du projet
  ├── package.json          # Dépendances et scripts du projet
  ├── next.config.js        # Configuration propre à Next.js
  └── README.md             # Documentation du projet
```

### 5. Premiers Pas avec Next.js

#### Lancement du Serveur de Développement

1. Dans le terminal, lancez le serveur de développement :

   ```powershell
   npm run dev
   ```

   *Cette commande démarre le serveur de développement. Vous pouvez visiter [http://localhost:3000](http://localhost:3000) pour voir votre application en action.*

2. Ouvrez votre projet dans VS Code et modifiez le code pour observer l'effet des changements en temps réel grâce à la fonctionnalité Fast Refresh de Next.js 15.

#### Modification de la Page d'Accueil

1. **Fichier `app/page.jsx`**
   Modifiez ce fichier pour afficher un message de bienvenue :

   ```jsx
   // app/page.jsx
   export default function HomePage() {
     return (
       <main className="container">
         <h1>Bienvenue sur mon application Next.js</h1>
         <p>Cette page est rendue côté serveur par défaut grâce à Next.js.</p>
       </main>
     );
   }
   ```

2. **Fichier `app/layout.jsx`**
   Ajustez votre layout racine pour définir les métadonnées et la structure HTML :

   ```jsx
   // app/layout.jsx
   export const metadata = {
     title: 'Mon Application Next.js',
     description: 'Créée avec create-next-app dans Next.js version 15',
   };

   export default function RootLayout({ children }) {
     return (
       <html lang="fr">
         <body>
           {children}
         </body>
       </html>
     );
   }
   ```

### 6. Comprendre les Composants Server et Client

Next.js 15 introduit une distinction importante entre les composants Server et Client :

```jsx:app/components/ServerComponent.jsx
// app/components/ServerComponent.jsx
// Composant Serveur (par défaut)
export default function ServerComponent() {
  return <h1>Rendu côté serveur</h1>;
}
```

```jsx:app/components/ClientComponent.jsx
// Composant Client
// app/components/ClientComponent.jsx
"use client";

export default function ClientComponent() {
  return <h1>Rendu côté client</h1>;
}
```

> **Important** :
>
> - Les composants sont Server Components par défaut
> - Utilisez "use client" uniquement lorsque vous avez besoin d'interactivité

### 7. Introduction au Styling Global

Next.js permet d'ajouter facilement des styles globaux à votre application. Commençons par quelques styles de base :

1. Ouvrez le fichier `app/globals.css`
2. Ajoutez ces styles simples :

  ```css:app/globals.css
  /* Styles de base */
  body {
    font-family: system-ui, sans-serif;
    margin: 0;
    padding: 20px;
    max-width: 1200px;
    margin: 0 auto;
  }

  /* Style simple pour la navigation */
  nav {
    margin-bottom: 20px;
  }

  nav ul {
    list-style: none;
    padding: 0;
    display: flex;
    gap: 20px;
  }

  nav a {
    color: #0070f3;
    text-decoration: none;
  }

  nav a:hover {
    text-decoration: underline;
  }

  /* Style de base pour les conteneurs */
  main {
    padding: 20px;
  }
  ```

3. Ces styles sont automatiquement appliqués grâce à l'import dans `app/layout.jsx` :

```jsx:app/layout.jsx
import './globals.css'
// ... reste du code ...
```

## Exercices Pratiques

### Exercice 1 : Créer une Page "À Propos"

**Objectif :** Créer une nouvelle page qui présente des informations sur vous ou sur votre projet.

1. Dans le dossier `app`, créez un dossier nommé `about`.
2. Dans ce dossier, créez un fichier `page.jsx` avec le contenu suivant :

   ```jsx:app/about/page.jsx
   // app/about/page.jsx
   export default function AboutPage() {
     return (
       <main className="container">
         <h1>À Propos</h1>
         <p>Bienvenue sur la page À Propos de mon application Next.js. Ici, vous trouverez des informations sur le projet et son développement.</p>
       </main>
     );
   }
   ```

3. **Vérification :** Accédez à [http://localhost:3000/about](http://localhost:3000/about) pour voir votre nouvelle page.

### Exercice 2 : Ajouter une Navigation Interne

**Objectif :** Faciliter la navigation entre pages en ajoutant un composant de lien au layout racine.

1. Créez un composant de navigation dans `app/components/Navigation.jsx` :

   ```jsx:app/components/Navigation.jsx
   // app/components/Navigation.jsx
   import Link from 'next/link';

   export default function Navigation() {
     return (
       <nav>
         <ul>
           <li><Link href="/">Accueil</Link></li>
           <li><Link href="/about">À Propos</Link></li>
         </ul>
       </nav>
     );
   }
   ```

2. Importez et utilisez ce composant dans `app/layout.jsx` :

   ```jsx:app/layout.jsx
   // app/layout.jsx
   import Navigation from './components/Navigation';
   import './globals.css';

   export const metadata = {
     title: 'Mon Application Next.js',
     description: 'Créée avec create-next-app dans Next.js version 15',
   };

   export default function RootLayout({ children }) {
     return (
       <html lang="fr">
         <body>
           {/* Insertion de la navigation */}
           <Navigation />
           {children}
         </body>
       </html>
     );
   }
   ```

3. **Vérification :** Assurez-vous que les liens permettent de naviguer entre les pages sans recharger la page (client-side routing).

### Exercice 3 : Créer un Composant Client Interactif

**Objectif :** Créer un composant interactif qui gère un état local grâce au marqueur "use client".

1. Créez un composant `Counter` dans `app/components/Counter.jsx` :

   ```jsxjsx:app/layout.jsx
   // app/components/Counter.jsx
   "use client";

   import { useState } from 'react';

   export default function Counter() {
     const [count, setCount] = useState(0);

     return (
       <div>
         <p>Valeur du compteur: {count}</p>
         <button onClick={() => setCount(count + 1)}>
           Incrémenter
         </button>
       </div>
     );
   }
   ```

2. Intégrez ce composant dans la page d'accueil :

   ```jsx:app/page.jsx
   // app/page.jsx
   import Counter from './components/Counter';

   export default function HomePage() {
     return (
       <main className="container">
         <h1>Bienvenue sur mon application Next.js</h1>
         <p>Cette page est rendue côté serveur par défaut grâce à Next.js.</p>
         {/* Insertion du composant interactif */}
         <Counter />
       </main>
     );
   }
   ```

3. **Vérification :** Assurez-vous que le compteur s'incrémente à chaque clic sans rechargement complet de la page.

### Exercice 4 : Utiliser le Composant Optimisé pour les Images

**Objectif :** Afficher une image optimisée en utilisant le composant `Image` de Next.js.

1. Modifiez la page d'accueil pour y inclure une image :

   ```jsx:app/page.jsx
   // app/page.jsx
   import Image from 'next/image';
   import Counter from './components/Counter';

   export default function HomePage() {
     return (
       <main className="container">
         <h1>Bienvenue sur mon application Next.js</h1>
         <p>Cette page est rendue côté serveur par défaut grâce à Next.js.</p>
         {/* Utilisation de Next/Image pour une image optimisée */}
         <Image
           src="/images/next-app.png"
           alt="Illustration Next.js"
           width={600}
           height={400}
           priority
         />
         <Counter />
       </main>
     );
   }
   ```

2. **Vérification :** L'image doit s'afficher correctement et profiter des optimisations automatiques de Next.js pour les images. Pour plus de détails, consultez la [documentation du composant Image](https://nextjs.org/docs/api-reference/next/image).

## Ressources Supplémentaires

- [Documentation officielle de Next.js](https://nextjs.org/docs)
- [Les nouveautés de Next.js 15](https://nextjs.org/blog/next-15)
- [Tutoriels et exemples sur GitHub](https://github.com/vercel/next.js/tree/canary/examples)
