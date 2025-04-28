# TP 5 Data Fetching & Server Components

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
import Image from 'next/image';

async function getData() {
  const res = await fetch('https://fakestoreapi.com/products/1');
  return res.json();
}

export default async function ServerComponent() {
  const data = await getData();
  
  return (
    <div>
      <h1>Server Component</h1>
      <div className="product">
        <Image 
          src={data.image} 
          alt={data.title} 
          width={200}
          height={200}
          style={{ objectFit: 'contain' }}
        />
        <h2>{data.title}</h2>
        <p>{data.description}</p>
        <p>Prix: {data.price}€</p>
        <p>Catégorie: {data.category}</p>
      </div>
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
import Image from 'next/image';
import Link from 'next/link';

async function getProducts() {
  // Cette fonction s'exécute côté serveur
  const res = await fetch('https://fakestoreapi.com/products', {
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
            <Link href={`/blog/${product.id}`}>
              <Image 
                src={product.image} 
                alt={product.title}
                width={150}
                height={150}
                style={{ objectFit: 'contain' }}
              />
              <h2>{product.title}</h2>
            </Link>
            <p>{product.description.substring(0, 100)}...</p>
            <p>Prix: {product.price}€</p>
            <p>Catégorie: {product.category}</p>
            <Link href={`/blog/${product.id}`} className="view-details">
              Voir détails
            </Link>
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
import Image from 'next/image';
import Link from 'next/link';

export async function generateStaticParams() {
  const posts = await fetch('https://fakestoreapi.com/products').then(r => r.json());
  
  return posts.map((post) => ({
    slug: post.id.toString(),
  }));
}

export default async function BlogPost({ params }) {
  const post = await fetch(`https://fakestoreapi.com/products/${params.slug}`).then(r => r.json());
  
  return (
    <article>
      <h1>{post.title}</h1>
      <div className="product-details">
        <Image 
          src={post.image} 
          alt={post.title} 
          width={300}
          height={300}
          style={{ objectFit: 'contain' }}
          priority
        />
        <p>{post.description}</p>
        <p>Prix: {post.price}€</p>
        <p>Catégorie: {post.category}</p>
        <p>Note: {post.rating.rate}/5 ({post.rating.count} avis)</p>
        <Link href="/products" className="back-button">
          Retour aux produits
        </Link>
      </div>
    </article>
  );
}
```

2. Créez une page avec rendu dynamique :

```jsx
// app/dashboard/page.js
import Link from 'next/link';

export const dynamic = 'force-dynamic';

export default async function DashboardPage() {
  const data = await fetch('https://fakestoreapi.com/products/categories', { cache: 'no-store' });
  const categories = await data.json();
  
  return (
    <div>
      <h1>Tableau de Bord</h1>
      <div className="stats-grid">
        {categories.map((category) => (
          <div key={category} className="stat-card">
            <h3>{category}</h3>
            <p>Catégorie de produits</p>
            <Link href={`/category/${encodeURIComponent(category)}`}>
              Voir les produits
            </Link>
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
  const cached = await fetch(`https://fakestoreapi.com/${type}`, {
    next: { revalidate: 3600 }
  });

  // Données jamais mises en cache
  const fresh = await fetch(`https://fakestoreapi.com/${type}`, {
    cache: 'no-store'
  });

  // Données mises en cache indéfiniment (ISR)
  const static = await fetch(`https://fakestoreapi.com/${type}`, {
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
- [Fake Store API Documentation](https://fakestoreapi.com/docs)
