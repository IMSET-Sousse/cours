# TP 3 Routing in Next.js

## Objectifs

- Comprendre en profondeur le système de routage basé sur les fichiers (App Router)
- Maîtriser les différents types de routes (statiques, dynamiques, parallèles)
- Implémenter la navigation entre pages
- Comprendre les conventions de fichiers spéciaux
- Utiliser les groupes de routes et les routes parallèles

## Prérequis

- Avoir complété le TP1
- Comprendre les bases de React
- Avoir une application Next.js fonctionnelle

## 1. Fondamentaux du Routage Next.js

Next.js 13+ utilise l'App Router, un système de routage basé sur le système de fichiers où :

- Les dossiers définissent les routes
- Les fichiers définissent l'UI

### Conventions de Fichiers Spéciaux

- `page.js` : Crée une route accessible publiquement
- `layout.js` : Interface partagée entre plusieurs pages
- `loading.js` : UI de chargement pour la page
- `error.js` : UI d'erreur pour la page
- `not-found.js` : UI pour les pages 404

### Exercice 1.1 : Création de Routes Basiques

1. Créez la structure de base suivante :

   ```bash
   app/
   ├── page.js           # Route: / (page d'accueil)
   ├── about/
   │   └── page.js       # Route: /about
   └── contact/
       └── page.js       # Route: /contact
   ```

2. Implémentez la page d'accueil :

   ```jsx
   // app/page.js
   export default function HomePage() {
     return (
       <div className="container">
         <h1>Bienvenue sur notre site</h1>
         <p>Cette page est la page d'accueil.</p>
       </div>
     );
   }
   ```

3. Créez la page "À propos" :

   ```jsx
   // app/about/page.js
   export default function AboutPage() {
     return (
       <div>
         <h1>À propos de nous</h1>
         <p>Découvrez notre histoire et notre mission.</p>
       </div>
     );
   }
   ```

## 2. Routes Dynamiques

Les routes dynamiques permettent de créer des pages avec des paramètres variables dans l'URL.

### Types de Segments Dynamiques

1. **Segments Dynamiques** : `[id]` ou `[slug]`
2. **Segments Catch-all** : `[...slug]`
3. **Segments Catch-all Optionnels** : `[[...slug]]`

### Exercice 2.1 : Création de Routes Dynamiques

1. Créez une structure pour un blog :

   ```bash
   app/
   └── blog/
       ├── page.js                # Liste des articles
       ├── [slug]/
       │   └── page.js           # Article individuel
       └── categories/
           └── [...slug]/
               └── page.js       # Catégories imbriquées
   ```

2. Implémentez la page d'article dynamique :

   ```jsx
   // app/blog/[slug]/page.js
   export default function BlogPost({ params }) {
     return (
       <article>
         <h1>Article: {params.slug}</h1>
         <p>Contenu de l'article...</p>
       </article>
     );
   }
   ```

3. Implémentez les catégories imbriquées :

   ```jsx
   // app/blog/categories/[...slug]/page.js
   export default function Category({ params }) {
     // params.slug est un tableau : ['tech', 'javascript']
     const categories = params.slug.join(' > ');
     
     return (
       <div>
         <h1>Catégorie: {categories}</h1>
         <p>Articles dans cette catégorie...</p>
       </div>
     );
   }
   ```

## 3. Navigation

Next.js fournit plusieurs méthodes pour la navigation entre pages.

### Exercice 3.1 : Implémentation de la Navigation

1. Créez un composant de navigation :

   ```jsx
   // app/components/Navigation.js
   import Link from 'next/link';
   import { usePathname } from 'next/navigation';

   export default function Navigation() {
     const pathname = usePathname();

     return (
       <nav className="navigation">
         <ul>
           <li>
             <Link 
               href="/" 
               className={pathname === '/' ? 'active' : ''}
             >
               Accueil
             </Link>
           </li>
           <li>
             <Link 
               href="/blog"
               className={pathname === '/blog' ? 'active' : ''}
             >
               Blog
             </Link>
           </li>
           <li>
             <Link 
               href="/about"
               className={pathname === '/about' ? 'active' : ''}
             >
               À propos
             </Link>
           </li>
         </ul>
       </nav>
     );
   }
   ```

2. Ajoutez la navigation programmatique :

   ```jsx
   // Exemple de composant avec navigation programmatique
   'use client';
   
   import { useRouter } from 'next/navigation';

   export default function LoginButton() {
     const router = useRouter();

     const handleLogin = async (e) => {
       e.preventDefault();
       // Logique de connexion...
       router.push('/dashboard');
     };

     return (
       <button onClick={handleLogin}>
         Se connecter
       </button>
     );
   }
   ```

## 4. Groupes de Routes

Les groupes de routes permettent d'organiser les fichiers sans affecter l'URL.

### Exercice 4.1 : Organisation avec des Groupes de Routes

1. Créez une structure pour une zone admin :

   ```bash
   app/
   └── (admin)/           # Le parenthèses indiquent un groupe
       ├── layout.js      # Layout partagé pour l'admin
       ├── dashboard/
       │   └── page.js    # /dashboard
       └── settings/
           └── page.js    # /settings
   ```

2. Implémentez le layout admin :

   ```jsx
   // app/(admin)/layout.js
   import AdminNav from './components/AdminNav';

   export default function AdminLayout({ children }) {
     return (
       <div className="admin-layout">
         <AdminNav />
         <main>{children}</main>
       </div>
     );
   }
   ```

## 5. Routes Parallèles

Les routes parallèles permettent d'afficher plusieurs pages simultanément.

### Exercice 5.1 : Création de Routes Parallèles

1. Créez une structure pour un tableau de bord :

   ```bash
   app/
   ├── dashboard/
   │   ├── layout.js
   │   ├── page.js
   │   ├── @analytics/
   │   │   └── page.js
   │   └── @team/
   │       └── page.js
   ```

2. Implémentez le layout du tableau de bord :

   ```jsx
   // app/dashboard/layout.js
   export default function DashboardLayout({ children, analytics, team }) {
     return (
       <div className="dashboard-layout">
         <div className="main-content">{children}</div>
         <div className="side-panels">
           <div className="analytics-panel">{analytics}</div>
           <div className="team-panel">{team}</div>
         </div>
       </div>
     );
   }
   ```

## Exercices Pratiques

1. Créez un blog complet avec :
   - Liste d'articles paginée
   - Pages d'articles individuels
   - Système de catégories
   - Navigation entre articles

2. Implémentez un espace membre avec :
   - Pages protégées
   - Navigation conditionnelle
   - Redirections automatiques
   - Gestion des erreurs 404

3. Développez un tableau de bord avec :
   - Routes parallèles pour les widgets
   - Navigation entre sections
   - Groupes de routes pour l'organisation
   - Layouts imbriqués

## Ressources Supplémentaires

- [Documentation officielle du routage Next.js](https://nextjs.org/docs/app/building-your-application/routing)
- [Guide des routes dynamiques](https://nextjs.org/docs/app/building-your-application/routing/dynamic-routes)
- [Documentation des groupes de routes](https://nextjs.org/docs/app/building-your-application/routing/route-groups)
- [Guide des routes parallèles](https://nextjs.org/docs/app/building-your-application/routing/parallel-routes)
