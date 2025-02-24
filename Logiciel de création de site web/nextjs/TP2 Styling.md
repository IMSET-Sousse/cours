# TP2 Styling

## Objectifs

- Comprendre les différentes approches de styling dans Next.js
- Maîtriser les méthodes de styling CSS
- Implémenter des styles globaux et des modules CSS
- Utiliser Tailwind CSS avec Next.js

## Introduction

Next.js offre plusieurs approches pour styler vos applications. Ce TP se concentre sur les méthodes de styling CSS, notamment les CSS Modules et les styles globaux. Nous verrons également l'intégration de Tailwind CSS, un framework CSS utilitaire populaire.

## Prérequis

- Avoir complété le TP1 Introduction à Next.js
- Connaissances de base en CSS
- Une application Next.js fonctionnelle

## Étapes

### 1. Les Différentes Approches de Styling

Next.js prend en charge plusieurs méthodes de styling :

1. **CSS Modules** : Pour des styles scopés aux composants
2. **Global CSS** : Pour des styles appliqués à toute l'application
3. **Tailwind CSS** : Pour un styling utilitaire rapide

### 2. CSS Modules

Les CSS Modules permettent de créer des styles scopés à un composant spécifique, évitant les conflits de nommage.

1. Créez un nouveau composant avec son module CSS :

```jsx:app/components/Card.jsx
export default function Card({ title, children }) {
  return (
    <div className={styles.card}>
      <h2 className={styles.title}>{title}</h2>
      <div className={styles.content}>{children}</div>
    </div>
  );
}
```

2. Créez le fichier de style correspondant :

```css:app/components/Card.module.css
.card {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.title {
  margin: 0 0 8px 0;
  color: #333;
}

.content {
  color: #666;
}
```

3. Importez et utilisez le composant :

```jsx:app/page.jsx
import Card from './components/Card';

export default function HomePage() {
  return (
    <main>
      <Card title="Mon Premier Card">
        <p>Contenu de la carte avec des styles scopés.</p>
      </Card>
    </main>
  );
}
```

### 3. Styles Globaux

Les styles globaux s'appliquent à toute l'application. Ils sont parfaits pour définir des styles de base.

1. Modifiez le fichier `app/globals.css` :

```css:app/globals.css
/* Reset CSS de base */
* {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

/* Variables CSS globales */
:root {
  --primary-color: #0070f3;
  --secondary-color: #ff4081;
  --background-color: #ffffff;
  --text-color: #333333;
}

/* Styles de base */
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', sans-serif;
  line-height: 1.6;
  color: var(--text-color);
  background-color: var(--background-color);
}

/* Styles de typographie */
h1 {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  color: var(--primary-color);
}

h2 {
  font-size: 2rem;
  margin-bottom: 0.8rem;
}

p {
  margin-bottom: 1rem;
}

/* Styles de mise en page */
.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 1rem;
}

/* Styles de boutons */
.button {
  display: inline-block;
  padding: 0.5rem 1rem;
  background-color: var(--primary-color);
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  text-decoration: none;
  transition: background-color 0.3s ease;
}

.button:hover {
  background-color: #0056b3;
}
```

2. Assurez-vous que le fichier est importé dans `app/layout.jsx` :

```jsx:app/layout.jsx
import './globals.css';

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>{children}</body>
    </html>
  );
}
```

### 4. Installation et Configuration de Tailwind CSS

1. Installez Tailwind CSS et ses dépendances :

```bash
npm install -D tailwindcss postcss autoprefixer
```

2. Initialisez la configuration Tailwind :

```bash
npx tailwindcss init -p
```

3. Configurez les chemins dans `tailwind.config.js` :

```js:tailwind.config.js
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./app/**/*.{js,ts,jsx,tsx,mdx}",
    "./components/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

4. Ajoutez les directives Tailwind dans `globals.css` :

```css:app/globals.css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

## Exercices Pratiques

### Exercice 1 : Création d'un Composant Card avec CSS Modules

**Objectif :** Créer un composant Card réutilisable avec des styles scopés.

1. Créez un nouveau composant `ProductCard` :

```jsx:app/components/ProductCard.jsx
import styles from './ProductCard.module.css';

export default function ProductCard({ title, price, description, imageUrl }) {
  return (
    <div className={styles.card}>
      <img src={imageUrl} alt={title} className={styles.image} />
      <div className={styles.content}>
        <h3 className={styles.title}>{title}</h3>
        <p className={styles.price}>{price}€</p>
        <p className={styles.description}>{description}</p>
      </div>
    </div>
  );
}
```

2. Créez les styles correspondants :

```css:app/components/ProductCard.module.css
.card {
  border: 1px solid #eaeaea;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.2s ease;
}

.card:hover {
  transform: translateY(-5px);
}

.image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.content {
  padding: 1rem;
}

.title {
  font-size: 1.25rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.price {
  color: #0070f3;
  font-weight: bold;
  font-size: 1.2rem;
}

.description {
  color: #666;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}
```

### Exercice 2 : Page de Produits avec Tailwind CSS

**Objectif :** Créer une page de produits utilisant Tailwind CSS.

1. Créez une nouvelle page produits :

```jsx:app/products/page.jsx
export default function ProductsPage() {
  const products = [
    {
      id: 1,
      name: "Produit 1",
      price: 99.99,
      description: "Description du produit 1"
    },
    {
      id: 2,
      name: "Produit 2",
      price: 149.99,
      description: "Description du produit 2"
    }
  ];

  return (
    <div className="container mx-auto px-4 py-8">
      <h1 className="text-3xl font-bold mb-6">Nos Produits</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        {products.map(product => (
          <div key={product.id} className="bg-white rounded-lg shadow-md p-6">
            <h2 className="text-xl font-semibold mb-2">{product.name}</h2>
            <p className="text-blue-600 font-bold">{product.price}€</p>
            <p className="text-gray-600 mt-2">{product.description}</p>
            <button className="mt-4 bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 transition-colors">
              Ajouter au panier
            </button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

### Exercice 3 : Création d'un Thème avec Variables CSS

**Objectif :** Implémenter un système de thème utilisant les variables CSS.

1. Ajoutez des variables de thème dans `globals.css` :

```css:app/globals.css
:root {
  /* Couleurs principales */
  --color-primary: #0070f3;
  --color-secondary: #ff4081;
  --color-success: #28a745;
  --color-danger: #dc3545;
  
  /* Couleurs de fond */
  --bg-primary: #ffffff;
  --bg-secondary: #f8f9fa;
  
  /* Typographie */
  --font-size-sm: 0.875rem;
  --font-size-base: 1rem;
  --font-size-lg: 1.125rem;
  --font-size-xl: 1.25rem;
  
  /* Espacement */
  --spacing-xs: 0.25rem;
  --spacing-sm: 0.5rem;
  --spacing-md: 1rem;
  --spacing-lg: 1.5rem;
  --spacing-xl: 2rem;
}

/* Classe utilitaire pour le thème sombre */
[data-theme="dark"] {
  --color-primary: #66b3ff;
  --bg-primary: #1a1a1a;
  --bg-secondary: #2d2d2d;
}
```

## Ressources Supplémentaires

- [Documentation CSS Modules Next.js](https://nextjs.org/docs/basic-features/built-in-css-support#adding-component-level-css)
- [Documentation Tailwind CSS](https://tailwindcss.com/docs)
- [Guide des bonnes pratiques CSS](https://developer.mozilla.org/fr/docs/Web/CSS)

## Conclusion

Ce TP vous a permis d'explorer les différentes approches de styling dans Next.js. Vous avez appris à :
- Utiliser les CSS Modules pour des styles scopés
- Gérer les styles globaux
- Intégrer Tailwind CSS
- Créer des composants réutilisables avec leur propre style

La prochaine étape consistera à explorer des fonctionnalités plus avancées de Next.js comme le routing et la gestion des données.
