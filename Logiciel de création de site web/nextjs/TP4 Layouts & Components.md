# TP4 Layouts & Components

## Objectifs

- Maîtriser les layouts racine et imbriqués
- Implémenter des interfaces de chargement (Loading UI)
- Gérer les erreurs efficacement
- Configurer les métadonnées
- Créer des composants réutilisables

## Prérequis

- Avoir complété le TP3
- Comprendre les Server et Client Components
- Connaissances de base en React

## 1. Root Layout

### 1.1 Configuration du Layout Racine

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
  description: 'Description de mon site',
  keywords: ['Next.js', 'React', 'JavaScript'],
};

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body className={inter.className}>
        <Header />
        <main className="container mx-auto px-4">
          {children}
        </main>
        <Footer />
      </body>
    </html>
  );
}
```

### 1.2 Composants de Base

```jsx
// app/components/Header.js
import Link from 'next/link';

export default function Header() {
  return (
    <header className="bg-white shadow">
      <nav className="container mx-auto px-4 py-6">
        <ul className="flex space-x-4">
          <li><Link href="/">Accueil</Link></li>
          <li><Link href="/blog">Blog</Link></li>
          <li><Link href="/contact">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
}

// app/components/Footer.js
export default function Footer() {
  return (
    <footer className="bg-gray-100 mt-8">
      <div className="container mx-auto px-4 py-6">
        <p>&copy; {new Date().getFullYear()} Mon Site</p>
      </div>
    </footer>
  );
}
```

## 2. Layouts Imbriqués

### 2.1 Layout pour Section Blog

```jsx
// app/blog/layout.js
import Sidebar from './components/Sidebar';

export const metadata = {
  title: 'Blog',
};

export default function BlogLayout({ children }) {
  return (
    <div className="flex gap-6">
      <div className="w-3/4">
        {children}
      </div>
      <Sidebar className="w-1/4" />
    </div>
  );
}

// app/blog/components/Sidebar.js
export default function Sidebar() {
  return (
    <aside>
      <h2>Catégories</h2>
      <ul>
        <li>Technologie</li>
        <li>Design</li>
        <li>Business</li>
      </ul>
    </aside>
  );
}
```

## 3. Loading UI

### 3.1 Loading Global

```jsx
// app/loading.js
export default function Loading() {
  return (
    <div className="flex justify-center items-center min-h-screen">
      <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-blue-500"></div>
    </div>
  );
}
```

### 3.2 Loading Spécifique

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

### 4.1 Error Boundary Global

```jsx
// app/error.js
'use client';

import { useEffect } from 'react';

export default function Error({ error, reset }) {
  useEffect(() => {
    console.error(error);
  }, [error]);

  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h2 className="text-2xl font-bold mb-4">
          Une erreur est survenue
        </h2>
        <button
          onClick={reset}
          className="bg-blue-500 text-white px-4 py-2 rounded"
        >
          Réessayer
        </button>
      </div>
    </div>
  );
}
```

### 4.2 Not Found Page

```jsx
// app/not-found.js
import Link from 'next/link';

export default function NotFound() {
  return (
    <div className="min-h-screen flex items-center justify-center">
      <div className="text-center">
        <h2 className="text-4xl font-bold mb-4">404</h2>
        <p className="mb-4">Page non trouvée</p>
        <Link
          href="/"
          className="text-blue-500 hover:underline"
        >
          Retour à l'accueil
        </Link>
      </div>
    </div>
  );
}
```

## 5. Métadonnées

### 5.1 Configuration Dynamique

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

### 5.2 Composants Réutilisables

```jsx
// app/components/MetadataImage.js
import Image from 'next/image';

export default function MetadataImage({ src, alt, width, height }) {
  return (
    <div className="relative aspect-video">
      <Image
        src={src}
        alt={alt}
        fill
        className="object-cover"
        sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 33vw"
        priority
      />
    </div>
  );
}
```

## Exercices Pratiques

1. Créez un layout pour une section admin avec :
   - Barre latérale de navigation
   - En-tête avec informations utilisateur
   - Zone de contenu principale
   - Gestion des erreurs spécifique

2. Implémentez des composants réutilisables :
   - Card pour afficher des articles/produits
   - Pagination
   - Formulaire de recherche
   - Boutons d'action

3. Configurez les métadonnées pour :
   - Pages statiques
   - Pages dynamiques
   - Images OpenGraph
   - Twitter Cards

4. Créez des interfaces de chargement pour :
   - Liste de produits
   - Détails d'article
   - Formulaires
   - Tableaux de données

## Ressources Supplémentaires

- [Documentation des Layouts](https://nextjs.org/docs/app/building-your-application/routing/pages-and-layouts)
- [Guide des Métadonnées](https://nextjs.org/docs/app/building-your-application/optimizing/metadata)
- [Documentation sur la Gestion des Erreurs](https://nextjs.org/docs/app/building-your-application/routing/error-handling) 