# TP 5 Layouts & Components

## Objectifs

- Maîtriser les layouts racine et imbriqués
- Implémenter des interfaces de chargement
- Gérer les erreurs efficacement
- Configurer les métadonnées
- Créer des composants réutilisables

## Prérequis

- Avoir complété le TP3
- Comprendre les Server et Client Components
- Connaître les bases du routage Next.js

## 1. Root Layout

### Exercice 1.1 : Configuration du Layout Racine

1. Créez un layout racine personnalisé :

```jsx
// app/layout.js
import { Inter } from 'next/font/google';
import Header from './components/Header';
import Footer from './components/Footer';
import './globals.css';

const inter = Inter({ subsets: ['latin'] });

export const metadata = {
  title: {
    template: '%s | Mon Site',
    default: 'Mon Site',
  },
  description: 'Un site créé avec Next.js',
  keywords: ['Next.js', 'React', 'JavaScript'],
};

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body className={inter.className}>
        <Header />
        <main className="min-h-screen p-4">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
```

## 2. Layouts Imbriqués

### Exercice 2.1 : Création de Layouts Spécifiques

1. Créez un layout pour la section blog :

```jsx
// app/blog/layout.js
import Sidebar from '../components/blog/Sidebar';

export default function BlogLayout({ children }) {
  return (
    <div className="grid grid-cols-12 gap-4">
      <aside className="col-span-3">
        <Sidebar />
      </aside>
      <div className="col-span-9">
        {children}
      </div>
    </div>
  );
}
```

## 3. Loading UI

### Exercice 3.1 : Implémentation des États de Chargement

1. Créez un composant de chargement global :

```jsx
// app/loading.js
export default function Loading() {
  return (
    <div className="flex items-center justify-center min-h-screen">
      <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-gray-900"></div>
    </div>
  );
}
```

2. Créez un composant de chargement spécifique :

```jsx
// app/blog/loading.js
export default function BlogLoading() {
  return (
    <div className="space-y-4">
      {[1, 2, 3].map((i) => (
        <div key={i} className="animate-pulse">
          <div className="h-4 bg-gray-200 rounded w-3/4"></div>
          <div className="space-y-3 mt-4">
            <div className="h-4 bg-gray-200 rounded"></div>
            <div className="h-4 bg-gray-200 rounded w-5/6"></div>
          </div>
        </div>
      ))}
    </div>
  );
}
```

## 4. Gestion des Erreurs

### Exercice 4.1 : Configuration de la Gestion d'Erreurs

1. Créez un composant d'erreur global :

```jsx
// app/error.js
'use client';

export default function Error({ error, reset }) {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h2 className="text-2xl font-bold mb-4">Une erreur est survenue</h2>
        <p className="text-gray-600 mb-4">{error.message}</p>
        <button
          onClick={reset}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600"
        >
          Réessayer
        </button>
      </div>
    </div>
  );
}
```

2. Créez un gestionnaire d'erreurs spécifique :

```jsx
// app/blog/error.js
'use client';

export default function BlogError({ error, reset }) {
  return (
    <div className="p-4 border border-red-200 rounded bg-red-50">
      <h2 className="text-red-800 font-semibold">Erreur de chargement du blog</h2>
      <p className="text-red-600">{error.message}</p>
      <button
        onClick={reset}
        className="mt-2 text-red-600 hover:text-red-800"
      >
        Réessayer
      </button>
    </div>
  );
}
```

## 5. Métadonnées

### Exercice 5.1 : Configuration des Métadonnées

1. Configurez les métadonnées dynamiques :

```jsx
// app/blog/[slug]/page.js
export async function generateMetadata({ params }) {
  const post = await getPost(params.slug);
  
  return {
    title: post.title,
    description: post.excerpt,
    openGraph: {
      title: post.title,
      description: post.excerpt,
      images: [post.image],
    },
  };
}
```

## Exercices Pratiques

1. Créez une mise en page complexe avec :
   - En-tête fixe
   - Barre latérale responsive
   - Pied de page collant
   - Navigation imbriquée

2. Implémentez un système de chargement avec :
   - Skeleton loading
   - Suspense boundaries
   - Indicateurs de progression

3. Développez un système de gestion d'erreurs avec :
   - Erreurs personnalisées
   - Journalisation des erreurs
   - Récupération gracieuse

4. Configurez les métadonnées pour :
   - SEO optimisé
   - Partage social
   - Données structurées

## Ressources Supplémentaires

- [Documentation des Layouts](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts)
- [Guide Loading UI](https://nextjs.org/docs/app/building-your-application/routing/loading-ui)
- [Documentation Error Handling](https://nextjs.org/docs/app/building-your-application/routing/error-handling)
- [Guide Metadata](https://nextjs.org/docs/app/building-your-application/optimizing/metadata) 