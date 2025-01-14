# TP3 Data Fetching & Server Components

## Objectifs

- Comprendre la différence entre Server et Client Components
- Maîtriser les différentes méthodes de récupération de données
- Implémenter le rendu statique et dynamique
- Utiliser les stratégies de mise en cache
- Gérer les états de chargement et d'erreur

## Prérequis

- Avoir complété le TP2
- Comprendre les bases du routage Next.js
- Connaissances de base des API REST

## 1. Server Components vs Client Components

### 1.1 Server Components (Par défaut)

```jsx
// app/users/page.js
async function getUsers() {
  const res = await fetch('https://api.example.com/users');
  return res.json();
}

export default async function UsersPage() {
  const users = await getUsers();
  
  return (
    <div>
      <h1>Utilisateurs</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>{user.name}</li>
        ))}
      </ul>
    </div>
  );
}
```

### 1.2 Client Components

```jsx
// app/components/Counter.js
'use client';

import { useState } from 'react';

export default function Counter() {
  const [count, setCount] = useState(0);
  
  return (
    <div>
      <p>Compteur: {count}</p>
      <button onClick={() => setCount(count + 1)}>
        Incrémenter
      </button>
    </div>
  );
}
```

## 2. Méthodes de Récupération de Données

### 2.1 fetch avec Server Components

```jsx
// app/posts/page.js
async function getPosts() {
  const res = await fetch('https://api.example.com/posts', {
    next: {
      revalidate: 3600 // Revalidation toutes les heures
    }
  });
  
  if (!res.ok) {
    throw new Error('Erreur lors de la récupération des articles');
  }
  
  return res.json();
}

export default async function PostsPage() {
  const posts = await getPosts();
  
  return (
    <div>
      <h1>Articles</h1>
      {posts.map(post => (
        <article key={post.id}>
          <h2>{post.title}</h2>
          <p>{post.excerpt}</p>
        </article>
      ))}
    </div>
  );
}
```

### 2.2 SWR pour les Client Components

```jsx
// app/components/LiveData.js
'use client';

import useSWR from 'swr';

const fetcher = (...args) => fetch(...args).then(res => res.json());

export default function LiveData() {
  const { data, error, isLoading } = useSWR(
    'https://api.example.com/live-data',
    fetcher,
    { refreshInterval: 1000 }
  );
  
  if (error) return <div>Erreur de chargement</div>;
  if (isLoading) return <div>Chargement...</div>;
  
  return (
    <div>
      <h2>Données en temps réel</h2>
      <pre>{JSON.stringify(data, null, 2)}</pre>
    </div>
  );
}
```

## 3. Rendu Statique vs Dynamique

### 3.1 Rendu Statique (par défaut)

```jsx
// app/static/page.js
export default async function StaticPage() {
  const data = await fetch('https://api.example.com/static-data', {
    cache: 'force-cache'
  }).then(res => res.json());
  
  return (
    <div>
      <h1>Page Statique</h1>
      <p>{data.content}</p>
    </div>
  );
}
```

### 3.2 Rendu Dynamique

```jsx
// app/dynamic/page.js
export const dynamic = 'force-dynamic';

export default async function DynamicPage() {
  const data = await fetch('https://api.example.com/dynamic-data', {
    cache: 'no-store'
  }).then(res => res.json());
  
  return (
    <div>
      <h1>Page Dynamique</h1>
      <p>Timestamp: {data.timestamp}</p>
    </div>
  );
}
```

## 4. Stratégies de Cache

### 4.1 Revalidation à la Demande

```jsx
// app/api/revalidate/route.js
import { revalidatePath } from 'next/cache';

export async function POST(request) {
  const { path, token } = await request.json();
  
  if (token !== process.env.REVALIDATE_TOKEN) {
    return Response.json({ error: 'Token invalide' }, { status: 401 });
  }
  
  revalidatePath(path);
  return Response.json({ revalidated: true });
}
```

### 4.2 Mise en Cache Sélective

```jsx
// app/products/[id]/page.js
async function getProduct(id) {
  const res = await fetch(`https://api.example.com/products/${id}`, {
    next: {
      tags: [`product-${id}`]
    }
  });
  return res.json();
}

export default async function ProductPage({ params }) {
  const product = await getProduct(params.id);
  
  return (
    <div>
      <h1>{product.name}</h1>
      <p>{product.description}</p>
      <p>Prix: {product.price}€</p>
    </div>
  );
}
```

## 5. Gestion des États

### 5.1 Loading UI

```jsx
// app/products/loading.js
export default function Loading() {
  return (
    <div className="loading-spinner">
      <div>Chargement des produits...</div>
    </div>
  );
}
```

### 5.2 Error Handling

```jsx
// app/products/error.js
'use client';

export default function Error({ error, reset }) {
  return (
    <div>
      <h2>Une erreur est survenue!</h2>
      <p>{error.message}</p>
      <button onClick={() => reset()}>Réessayer</button>
    </div>
  );
}
```

## Exercices Pratiques

1. Créez une page de blog avec :
   - Liste des articles (Server Component)
   - Compteur de vues (Client Component)
   - Mise en cache des articles
   - Revalidation périodique

2. Implémentez un tableau de bord avec :
   - Données en temps réel
   - État de chargement
   - Gestion des erreurs
   - Mise à jour automatique

3. Développez une page produit avec :
   - Données statiques (description, caractéristiques)
   - Données dynamiques (stock, prix)
   - Cache sélectif
   - UI de chargement

4. Créez une API avec :
   - Points de terminaison REST
   - Validation des données
   - Gestion du cache
   - Revalidation à la demande

## Ressources Supplémentaires

- [Documentation Data Fetching](https://nextjs.org/docs/app/building-your-application/data-fetching)
- [Guide des Server Components](https://nextjs.org/docs/app/building-your-application/rendering/server-components)
- [Documentation du Caching](https://nextjs.org/docs/app/building-your-application/caching) 