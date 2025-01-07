# TP 1 Introduction à Next.js

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
- Connaissances de base en HTML, CSS, JavaScript et React([1](https://nextjs.org/docs))

## Étapes

### 1. Installation de Node.js et npm

1. Téléchargez et installez Node.js depuis [nodejs.org](https://nodejs.org/)
   - Version 18.18 ou ultérieure requise([2](https://nextjs.org/docs/app/getting-started/installation))
   - Choisissez la version LTS (Long Term Support)

2. Vérifiez l'installation en ouvrant un terminal :

   Pour vérifier Node.js :

   ```bash
   node --version
   ```

   Cette commande affiche la version de Node.js installée, confirmant que l'installation s'est bien déroulée.

   Pour vérifier npm :

   ```bash
   npm --version
   ```

   npm (Node Package Manager) est le gestionnaire de paquets de Node.js. Il permet d'installer, de gérer et de partager des packages JavaScript. C'est l'outil principal pour installer les dépendances de votre projet Next.js.

   Pour vérifier npx :

   ```bash
   npx --version
   ```

   npx est un exécuteur de paquets npm qui permet d'exécuter des packages sans avoir à les installer globalement. Il est particulièrement utile pour exécuter des commandes ponctuelles comme create-next-app, qui ne nécessitent pas une installation permanente sur votre système.

### 2. Configuration de l'environnement de développement

1. Installez VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/)
2. Installez les extensions recommandées :
   - ESLint (validation du code)([3](https://nextjs.org/docs/app/building-your-application/configuring/eslint))
   - ES7+ React/Redux/React-Native snippets
   - Prettier (formatage du code)
   - Next.js extension (support TypeScript et auto-complétion)([4](https://nextjs.org/docs/app/getting-started/installation))

### 3. Création d'une nouvelle application Next.js

1. Ouvrez un terminal et naviguez vers le dossier souhaité :

   ```bash
   cd chemin/vers/votre/dossier
   ```

2. Créez une nouvelle application Next.js([2](https://nextjs.org/docs/app/getting-started/installation)) :

   ```bash
   npx create-next-app@latest
   ```

3. Répondez aux questions de configuration :

   ```bash
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

```bash
mon-app/
  ├── app/             # Dossier principal de l'application
  │   ├── layout.js    # Layout racine
  │   └── page.js      # Page d'accueil
  ├── public/          # Fichiers statiques (images, fonts, etc.)
  ├── node_modules/    # Dépendances du projet
  ├── package.json     # Configuration du projet
  ├── next.config.js   # Configuration Next.js
  └── README.md        # Documentation
```

### 5. Premiers pas avec Next.js

1. Modifiez `src/app/page.js` :

   ```jsx
   export default function HomePage() {
     return (
       <main className="container">
         <h1>Bienvenue sur mon application Next.js</h1>
         <p>Cette page est rendue côté serveur par défaut!</p>
       </main>
     );
   }
   ```

2. Modifiez `src/app/layout.js` :

   ```jsx
   export const metadata = {
     title: 'Mon Application Next.js',
     description: 'Créée avec create-next-app',
   }

   export default function RootLayout({ children }) {
     return (
       <html lang="fr">
         <body>{children}</body>
       </html>
     );
   }
   ```

### 6. Lancement et développement

1. Démarrez le serveur de développement :

   ```bash
   npm run dev
   ```

2. Accédez à [http://localhost:3000](http://localhost:3000)

3. Scripts disponibles :

   ```json
   {
     "scripts": {
       "dev": "next dev",     // Mode développement
       "build": "next build", // Build de production
       "start": "next start", // Démarrage en production
       "lint": "next lint"    // Vérification du code
     }
   }
   ```

## Fonctionnalités principales de Next.js([5](https://nextjs.org/docs))

- **Server Components** : Composants React rendus côté serveur par défaut
- **Client Components** : Composants interactifs avec le marqueur 'use client'
- **Routing** : Système de routage basé sur le système de fichiers
- **Data Fetching** : Récupération des données simplifiée avec async/await
- **Optimizations** : Optimisations automatiques (images, polices, scripts)

## Exercices pratiques

1. Créez une nouvelle page "À propos" dans `src/app/about/page.js`
2. Ajoutez un composant de navigation entre les pages
3. Créez un composant client interactif avec le marqueur 'use client'
4. Utilisez le composant Image de Next.js pour optimiser une image
5. Implémentez un formulaire de contact simple

## Ressources supplémentaires

- [Documentation officielle Next.js](https://nextjs.org/docs)
- [Learn Next.js](https://nextjs.org/learn)
- [Examples](https://github.com/vercel/next.js/tree/canary/examples)
