# TP 3 Data Fetching & Server Components

## Objectifs

- Comprendre la différence entre Server et Client Components
- Maîtriser les méthodes de récupération de données
- Implémenter le rendu statique et dynamique
- Utiliser les stratégies de mise en cache
- Optimiser les performances de l'application

## Prérequis

- Avoir complété le TP2
- Comprendre les bases du routage Next.js
- Connaître les concepts de base des API REST

## 1. Server Components vs Client Components

### Exercice 1.1 : Comprendre les Server Components

1. Créez un composant serveur de base :

```jsx
// app/components/ServerComponent.js
async function getData() {
  const res = await fetch('https://api.example.com/data');
  return res.json();
}

export default async function ServerComponent() {
  const data = await getData();
  
  return (
    <div>
      <h1>Server Component</h1>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

### Exercice 1.2 : Créer un Client Component

1. Créez un composant client interactif :

```jsx
// app/components/ClientComponent.js
'use client';

import { useState } from 'react';

export default function ClientComponent() {
  const [count, setCount] = useState(0);

  return (
    <div>
      <h2>Client Component</h2>
      <p>Count: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Increment
      </button>
    </div>
  );
}
```

## 2. Méthodes de Récupération de Données

### Exercice 2.1 : Fetch avec Server Components

1. Implémentez différentes méthodes de fetch :

```jsx
// app/products/page.js
async function getProducts() {
  // Cette fonction s'exécute côté serveur
  const res = await fetch('https://api.example.com/products', {
    next: {
      revalidate: 3600 // Revalidation toutes les heures
    }
  });
  
  if (!res.ok) {
    throw new Error('Failed to fetch products');
  }
  
  return res.json();
}

export default async function ProductsPage() {
  const products = await getProducts();
  
  return (
    <div>
      <h1>Nos Produits</h1>
      <div className="products-grid">
        {products.map((product) => (
          <div key={product.id} className="product-card">
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <p>Prix: {product.price}€</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## 3. Rendu Statique vs Dynamique

### Exercice 3.1 : Configuration du Rendu

1. Implémentez une page avec rendu statique :

```jsx
// app/blog/[slug]/page.js
export async function generateStaticParams() {
  const posts = await fetch('https://api.example.com/posts').then(r => r.json());
  
  return posts.map((post) => ({
    slug: post.slug,
  }));
}

export default async function BlogPost({ params }) {
  const post = await fetch(`https://api.example.com/posts/${params.slug}`).then(r => r.json());
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div dangerouslySetInnerHTML={{ __html: post.content }} />
    </article>
  );
}
```

2. Créez une page avec rendu dynamique :

```jsx
// app/dashboard/page.js
export const dynamic = 'force-dynamic';

export default async function DashboardPage() {
  const data = await fetch('https://api.example.com/stats', { cache: 'no-store' });
  const stats = await data.json();
  
  return (
    <div>
      <h1>Tableau de Bord</h1>
      <div className="stats-grid">
        {Object.entries(stats).map(([key, value]) => (
          <div key={key} className="stat-card">
            <h3>{key}</h3>
            <p>{value}</p>
          </div>
        ))}
      </div>
    </div>
  );
}
```

## 4. Stratégies de Mise en Cache

### Exercice 4.1 : Implémentation du Cache

1. Configurez différentes stratégies de cache :

```jsx
// app/utils/data.js
export async function getData(type) {
  // Données mises en cache pendant 1 heure
  const cached = await fetch(`https://api.example.com/${type}`, {
    next: { revalidate: 3600 }
  });

  // Données jamais mises en cache
  const fresh = await fetch(`https://api.example.com/${type}`, {
    cache: 'no-store'
  });

  // Données mises en cache indéfiniment (ISR)
  const static = await fetch(`https://api.example.com/${type}`, {
    cache: 'force-cache'
  });

  return {
    cached: await cached.json(),
    fresh: await fresh.json(),
    static: await static.json()
  };
}
```

## Exercices Pratiques

1. Créez une page de blog avec :
   - Rendu statique des articles
   - Commentaires dynamiques
   - Mise en cache optimisée

2. Implémentez un tableau de bord avec :
   - Données en temps réel
   - Graphiques interactifs
   - Mise à jour automatique

3. Développez un système de recherche avec :
   - Autocomplétion côté client
   - Résultats côté serveur
   - Cache des résultats fréquents

## Ressources Supplémentaires

- [Documentation Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
- [Guide Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)
- [Stratégies de Cache](https://nextjs.org/docs/app/building-your-application/caching) 