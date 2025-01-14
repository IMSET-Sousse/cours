# TP2 Routing in Next.js

## Objectifs

- Comprendre le système de routage basé sur les fichiers
- Implémenter des routes dynamiques
- Créer des routes imbriquées
- Utiliser les liens entre pages
- Maîtriser les groupes de routes et les routes parallèles

## Prérequis

- Avoir complété le TP1
- Connaissances de base de Next.js
- Projet Next.js fonctionnel

## 1. Structure de Base du Routage

Le routage dans Next.js est basé sur le système de fichiers dans le dossier `app`. Chaque dossier représente un segment de route.

### 1.1 Pages Statiques

Créez les fichiers suivants :

```jsx
// app/about/page.js
export default function About() {
  return (
    <div>
      <h1>À propos</h1>
      <p>Bienvenue sur la page À propos</p>
    </div>
  );
}

// app/contact/page.js
export default function Contact() {
  return (
    <div>
      <h1>Contact</h1>
      <p>Contactez-nous</p>
    </div>
  );
}
```

## 2. Navigation Entre Pages

### 2.1 Utilisation du Composant Link

Créez un composant de navigation :

```jsx
// app/components/Navigation.js
import Link from 'next/link';

export default function Navigation() {
  return (
    <nav>
      <ul>
        <li><Link href="/">Accueil</Link></li>
        <li><Link href="/about">À propos</Link></li>
        <li><Link href="/contact">Contact</Link></li>
      </ul>
    </nav>
  );
}
```

### 2.2 Intégration dans le Layout

```jsx
// app/layout.js
import Navigation from './components/Navigation';

export default function RootLayout({ children }) {
  return (
    <html lang="fr">
      <body>
        <Navigation />
        {children}
      </body>
    </html>
  );
}
```

## 3. Routes Dynamiques

### 3.1 Création d'une Route Dynamique

```jsx
// app/posts/[id]/page.js
export default function Post({ params }) {
  return (
    <div>
      <h1>Article {params.id}</h1>
      <p>Contenu de l'article {params.id}</p>
    </div>
  );
}
```

### 3.2 Génération des Paramètres

```jsx
// app/posts/[id]/page.js
export async function generateStaticParams() {
  // Simuler des données d'articles
  const posts = [1, 2, 3, 4, 5];
  
  return posts.map((id) => ({
    id: id.toString(),
  }));
}
```

## 4. Routes Imbriquées

Créez une structure de routes imbriquées :

```plaintext
app/
  ├── blog/
  │   ├── page.js           # /blog
  │   ├── [category]/
  │   │   ├── page.js       # /blog/[category]
  │   │   └── [post]/
  │   │       └── page.js   # /blog/[category]/[post]
```

```jsx
// app/blog/[category]/[post]/page.js
export default function BlogPost({ params }) {
  return (
    <div>
      <h1>Article: {params.post}</h1>
      <p>Catégorie: {params.category}</p>
    </div>
  );
}
```

## 5. Groupes de Routes

### 5.1 Création d'un Groupe de Routes

```plaintext
app/
  ├── (shop)/
  │   ├── products/
  │   │   └── page.js
  │   └── categories/
  │       └── page.js
```

### 5.2 Routes Parallèles

```plaintext
app/
  ├── @modal/
  │   └── login/
  │       └── page.js
  └── page.js
```

## Exercices Pratiques

1. Créez une structure de blog avec :
   - Liste des articles
   - Pages d'articles individuels
   - Catégories

2. Implémentez une navigation dynamique :
   - Menu principal
   - Fil d'Ariane (Breadcrumb)
   - Navigation entre articles

3. Créez un groupe de routes pour une section "admin" :
   - Dashboard
   - Gestion des articles
   - Gestion des utilisateurs

4. Ajoutez des routes parallèles pour :
   - Modal de connexion
   - Panier d'achat
   - Notifications

## Ressources Supplémentaires

- [Documentation officielle du routage Next.js](https://nextjs.org/docs/app/building-your-application/routing)
- [Exemples de routes dynamiques](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes)
- [Guide des routes parallèles](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes) 