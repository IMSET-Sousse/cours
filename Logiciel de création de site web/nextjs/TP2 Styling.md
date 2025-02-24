# TP2 : Styling

## Introduction

Le styling (mise en forme) est un aspect fondamental du développement web. Next.js offre plusieurs approches pour styler vos applications, toutes intégrées nativement sans configuration supplémentaire. Dans ce TP, nous nous concentrerons sur les méthodes de styling utilisant uniquement CSS, sans Sass ni Tailwind CSS.

## Objectifs

- Comprendre les différentes approches de styling dans Next.js
- Maîtriser l'utilisation des CSS Modules pour des styles isolés
- Apprendre à utiliser le CSS global pour des styles d'application
- Créer des composants réutilisables avec des styles modulaires
- Implémenter des designs responsifs

## Prérequis

- Avoir complété le TP1 Introduction à Next.js
- Connaissances de base en CSS
- Un projet Next.js fonctionnel

## 1. Les Approches de Styling dans Next.js

Next.js propose plusieurs méthodes pour styler vos applications :

1. **CSS Global**
   - Styles appliqués à toute l'application
   - Idéal pour les styles de base et les réinitialisations CSS
   - Importé dans le fichier `layout.jsx`

2. **CSS Modules**
   - Styles scopés à un composant spécifique
   - Évite les conflits de noms de classes
   - Nommage automatique des classes

3. **CSS-in-JS** (non couvert dans ce TP)
   - Styles directement dans les composants
   - Utilisation de bibliothèques tierces

## 2. CSS Global

Le CSS global permet de définir des styles qui s'appliquent à l'ensemble de l'application.

### 2.1 Configuration

1. Créez ou modifiez le fichier `app/globals.css` :

```css
/* app/globals.css */
/* Variables CSS globales */
:root {
  --primary-color: #0070f3;
  --secondary-color: #ff4081;
  --background-color: #ffffff;
  --text-color: #333333;
  --spacing-unit: 8px;
  --border-radius: 4px;
}

/* Reset CSS basique */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Styles de base */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
}

/* Typographie */
h1 {
  font-size: 2.5rem;
  margin-bottom: calc(var(--spacing-unit) * 3);
}

h2 {
  font-size: 2rem;
  margin-bottom: calc(var(--spacing-unit) * 2);
}

p {
  margin-bottom: var(--spacing-unit);
}

/* Layout */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 calc(var(--spacing-unit) * 2);
}

/* Utilitaires */
.text-center {
  text-align: center;
}

.mt-1 { margin-top: var(--spacing-unit); }
.mt-2 { margin-top: calc(var(--spacing-unit) * 2); }
.mt-3 { margin-top: calc(var(--spacing-unit) * 3); }
```

2. Importez le CSS global dans votre `app/layout.jsx` :

```jsx
import './globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
```

## 3. CSS Modules

Les CSS Modules permettent de créer des styles scopés à un composant spécifique, évitant ainsi les conflits de noms de classes.

### 3.1 Création d'un Composant avec CSS Module

1. Créez un nouveau composant `Button` :

```jsx
// app/components/Button/Button.jsx
import styles from './Button.module.css';

export default function Button({ children, variant = 'primary' }) {
  return (
    <button className={`${styles.button} ${styles[variant]}`}>
      {children}
    </button>
  );
}
```

2. Créez le fichier CSS Module correspondant :

```css
/* app/components/Button/Button.module.css */
.button {
  padding: calc(var(--spacing-unit) * 1.5) calc(var(--spacing-unit) * 2);
  border: none;
  border-radius: var(--border-radius);
  font-size: 1rem;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.primary {
  background-color: var(--primary-color);
  color: white;
}

.primary:hover {
  background-color: #0051a8;
}

.secondary {
  background-color: var(--secondary-color);
  color: white;
}

.secondary:hover {
  background-color: #d1336a;
}
```

### 3.2 Création d'une Card Réutilisable

1. Créez un composant `Card` :

```jsx
// app/components/Card/Card.jsx
import styles from './Card.module.css';

export default function Card({ title, children }) {
  return (
    <div className={styles.card}>
      {title && <h2 className={styles.title}>{title}</h2>}
      <div className={styles.content}>
        {children}
      </div>
    </div>
  );
}
```

2. Ajoutez les styles correspondants :

```css
/* app/components/Card/Card.module.css */
.card {
  background-color: white;
  border-radius: var(--border-radius);
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: calc(var(--spacing-unit) * 3);
  margin-bottom: calc(var(--spacing-unit) * 2);
}

.title {
  color: var(--primary-color);
  margin-bottom: calc(var(--spacing-unit) * 2);
}

.content {
  color: var(--text-color);
}
```

## 4. Design Responsif

### 4.1 Grille Responsive avec CSS Grid

Ajoutez ces styles à votre `globals.css` :

```css
/* Dans globals.css */
.grid {
  display: grid;
  gap: calc(var(--spacing-unit) * 2);
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
}

/* Media Queries pour différentes tailles d'écran */
@media (max-width: 768px) {
  .container {
    padding: 0 var(--spacing-unit);
  }
  
  h1 {
    font-size: 2rem;
  }
  
  h2 {
    font-size: 1.5rem;
  }
}
```

## 5. Exercices Pratiques

### Exercice 1 : Page d'Accueil Stylée

Créez une page d'accueil utilisant les composants et styles que nous avons créés :

```jsx
// app/page.jsx
import Button from './components/Button/Button';
import Card from './components/Card/Card';

export default function HomePage() {
  return (
    <div className="container">
      <h1 className="text-center">Bienvenue sur Notre Site</h1>
      
      <div className="grid mt-3">
        <Card title="Fonctionnalité 1">
          <p>Description de la première fonctionnalité</p>
          <Button>En savoir plus</Button>
        </Card>
        
        <Card title="Fonctionnalité 2">
          <p>Description de la deuxième fonctionnalité</p>
          <Button variant="secondary">Découvrir</Button>
        </Card>
        
        <Card title="Fonctionnalité 3">
          <p>Description de la troisième fonctionnalité</p>
          <Button>Explorer</Button>
        </Card>
      </div>
    </div>
  );
}
```

### Exercice 2 : Navigation Responsive

Créez un composant de navigation responsive :

```jsx
// app/components/Navigation/Navigation.jsx
import styles from './Navigation.module.css';
import Link from 'next/link';

export default function Navigation() {
  return (
    <nav className={styles.nav}>
      <div className="container">
        <div className={styles.navContent}>
          <Link href="/" className={styles.logo}>
            MonSite
          </Link>
          <ul className={styles.navLinks}>
            <li><Link href="/">Accueil</Link></li>
            <li><Link href="/about">À propos</Link></li>
            <li><Link href="/contact">Contact</Link></li>
          </ul>
        </div>
      </div>
    </nav>
  );
}
```

```css
/* app/components/Navigation/Navigation.module.css */
.nav {
  background-color: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: calc(var(--spacing-unit) * 2) 0;
}

.navContent {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  color: var(--primary-color);
  text-decoration: none;
}

.navLinks {
  display: flex;
  gap: calc(var(--spacing-unit) * 3);
  list-style: none;
}

.navLinks a {
  color: var(--text-color);
  text-decoration: none;
  transition: color 0.3s ease;
}

.navLinks a:hover {
  color: var(--primary-color);
}

@media (max-width: 768px) {
  .navContent {
    flex-direction: column;
    gap: var(--spacing-unit);
  }

  .navLinks {
    gap: var(--spacing-unit);
  }
}
```

## Points Clés à Retenir

1. **CSS Global vs CSS Modules**
   - CSS Global pour les styles d'application et utilitaires
   - CSS Modules pour les styles de composants isolés

2. **Variables CSS**
   - Définies une fois dans `:root`
   - Réutilisables dans toute l'application
   - Facilitent la maintenance et la cohérence

3. **Design Responsif**
   - Utilisation de CSS Grid pour les layouts
   - Media queries pour l'adaptation mobile
   - Unités relatives pour la flexibilité

4. **Bonnes Pratiques**
   - Organisation claire des fichiers CSS
   - Nommage explicite des classes
   - Réutilisation des composants
   - Utilisation des variables CSS

## Ressources

- [Documentation CSS Next.js](https://nextjs.org/docs/app/building-your-application/styling)
- [Guide CSS Modules](https://github.com/css-modules/css-modules)
- [MDN CSS Grid Guide](https://developer.mozilla.org/fr/docs/Web/CSS/CSS_Grid_Layout)

## Conclusion

Ce TP vous a permis de découvrir les différentes approches de styling dans Next.js, en se concentrant sur l'utilisation du CSS pur. Vous avez appris à :

- Utiliser le CSS Global pour les styles d'application
- Créer des composants isolés avec CSS Modules
- Implémenter un design responsif
- Appliquer les bonnes pratiques de styling
