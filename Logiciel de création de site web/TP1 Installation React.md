# TP 1 Installation et Configuration de React

## Objectifs

- Installer Node.js et npm
- Créer une nouvelle application React
- Comprendre la structure d'un projet React
- Lancer et tester l'application
- Effectuer des modifications basiques
- Comprendre les composants essentiels

## Prérequis

- Un éditeur de code (VS Code recommandé)
- Un terminal de commande
- Une connexion internet
- Connaissances de base en HTML et JavaScript

## Étapes

### 1. Installation de Node.js et npm

1. Téléchargez et installez Node.js depuis [nodejs.org](https://nodejs.org/)
   - Choisissez la version LTS (Long Term Support)
   - Suivez les étapes d'installation standard

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

   npm (Node Package Manager) est le gestionnaire de paquets de Node.js. Il permet d'installer, de gérer et de partager des packages JavaScript. C'est l'outil principal pour installer les dépendances de votre projet React.

   Pour vérifier npx :

   ```bash
   npx --version
   ```

   npx est un exécuteur de paquets npm qui permet d'exécuter des packages sans avoir à les installer globalement. Il est particulièrement utile pour exécuter des commandes ponctuelles comme create-react-app, qui ne nécessitent pas une installation permanente sur votre système.

### 2. Configuration de l'environnement de développement

Installation de VS Code (si ce n'est pas déjà fait)

- Téléchargez VS Code depuis [code.visualstudio.com](https://code.visualstudio.com/)
- Installez les extensions recommandées pour React :
  - ES7+ React/Redux/React-Native snippets
  - ESLint
  - Prettier
  - Simple React Snippets
  - Auto Rename Tag

### 3. Création d'une nouvelle application React

1. Ouvrez un terminal et naviguez vers le dossier où vous souhaitez créer votre projet

   ```bash
   cd chemin/vers/votre/dossier
   ```

2. Créez une nouvelle application React avec Create React App :

   ```bash
   npx create-react-app mon-app
   ```

   > Note : Remplacez "mon-app" par le nom souhaité pour votre projet

3. Une fois l'installation terminée, accédez au dossier du projet :

   ```bash
   cd mon-app
   ```

### 4. Structure du projet React

Explorez la structure de base de votre projet :

```bash
mon-app/
  ├── node_modules/    # Dépendances du projet
  ├── public/          # Fichiers statiques
  │   ├── index.html   # Page HTML principale
  │   ├── favicon.ico  # Icône du site
  │   └── manifest.json
  ├── src/             # Code source
  │   ├── App.js       # Composant principal
  │   ├── App.css      # Styles du composant App
  │   ├── index.js     # Point d'entrée
  │   └── index.css    # Styles globaux
  ├── package.json     # Configuration du projet
  └── README.md        # Documentation
```

### 5. Lancement de l'application

1. Dans le terminal, à partir du dossier du projet, lancez l'application :

   ```bash
   npm start
   ```

2. Votre navigateur devrait s'ouvrir automatiquement à l'adresse : http://localhost:3000

3. En cas d'erreur :
   - Vérifiez que vous êtes bien dans le dossier du projet
   - Essayez `npm install` pour réinstaller les dépendances
   - Vérifiez qu'aucune autre application n'utilise le port 3000

### 6. Premières modifications

1. Ouvrez `src/App.js` et modifiez le contenu :

   ```jsx
   import './App.css';

   function App() {
     return (
       <div className="App">
         <header className="App-header">
           <h1>Ma première application React</h1>
           <p>Bienvenue dans le monde de React!</p>
         </header>
       </div>
     );
   }

   export default App;
   ```

2. Observez les changements en temps réel dans votre navigateur

### 7. Commandes utiles

```bash
npm start    # Démarre le serveur de développement
npm test     # Lance les tests
npm run build # Crée une version de production
npm run eject # Éjecte la configuration (irréversible)
```

## Points importants à retenir

- React utilise JSX, une syntaxe qui mélange JavaScript et HTML
- Les modifications sont visibles en temps réel grâce au "hot reload"
- Chaque composant React doit commencer par une majuscule
- Les fichiers CSS peuvent être importés directement dans les composants
- Node_modules ne doit jamais être commité dans le gestionnaire de versions
- La commande `npm start` doit toujours être exécutée depuis le dossier du projet

## Ressources supplémentaires

- [Documentation officielle de React](https://react.dev/)
- [Create React App documentation](https://create-react-app.dev/)

## Conclusion

Vous avez maintenant une application React fonctionnelle et vous comprenez sa structure de base. Vous pouvez commencer à développer vos propres composants et à explorer les fonctionnalités de React.

## Exercice final

Pour valider vos acquis, essayez de :

1. Créer un nouveau projet React
2. Le lancer correctement
3. Modifier le texte d'accueil
4. Arrêter le serveur (Ctrl+C dans le terminal)
5. Le relancer
