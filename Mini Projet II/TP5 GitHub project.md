# TP5: Gestion de Projet Agile avec GitHub Projects et Scrum

## Objectif

Apprendre à mettre en place et gérer un projet agile en utilisant GitHub Projects avec la méthodologie Scrum.

## Prérequis

- Compte GitHub avec accès à l'organisation IMSET-Sousse
- Connaissances de base en Git et GitHub
- Compréhension des principes Scrum
- Lecture préalable du Guide Scrum 2020

## Partie 1: Configuration du Projet

### 1.1 Mise en place de l'environnement

1. Création du projet dans l'organisation IMSET:
   a. Dans le coin supérieur droit de GitHub, cliquer sur votre photo de profil
   b. Sélectionner "Your organizations"
   c. Cliquer sur "IMSET-Sousse"
   d. Sous le nom de l'organisation, cliquer sur "Projects"
   e. Cliquer sur "New project"
   f. Sous "Start from scratch", sélectionner "Table"
   g. Donner un nom au projet
   h. Cliquer sur "Create project"

2. Configuration de la vue Table:
   a. Ajouter les colonnes essentielles:
      - Title (par défaut)
      - Status (single select)
        * New
        * Backlog
        * In Progress
        * In Review
        * Done
      - Priority (single select)
        * 🔥 High
        * 📌 Medium
        * 🔽 Low
      - Sprint (iteration)
      - Labels
      - Assignees
      - Repository

   b. Pour ajouter une colonne:
      - Cliquer sur "+" à droite du tableau
      - Sélectionner "New field"
      - Choisir le type de champ approprié
      - Configurer les options si nécessaire

3. Configuration des filtres et groupements:
   a. Cliquer sur le menu déroulant "Group"
      - Grouper par Status pour une vue Kanban
      - Grouper par Sprint pour la planification
      - Grouper par Priority pour la priorisation

   b. Utiliser les filtres pour:
      - Afficher les items du sprint en cours
      - Filtrer par assignee
      - Filtrer par label

4. Configuration initiale du projet:
   a. Ajouter une description du projet:
      - Cliquer sur le menu (⋯) en haut à droite
      - Sélectionner "Settings"
      - Sous "Add a description", ajouter une description claire
      - Cliquer sur "Save"

   b. Configurer le README du projet:
      - Dans les paramètres du projet
      - Sous "README", ajouter:
        * Objectifs du projet
        * Instructions d'utilisation
        * Liens importants
      - Cliquer sur "Save"

5. Configuration des vues:
   - Table (pour le Product Backlog)
   - Board (pour le Sprint en cours)
   - Roadmap (pour la planification)

6. Configuration des colonnes de travail:
   - New (nouvelles issues)
   - Backlog (à faire)
   - Ready (prêt à démarrer)
   - In Progress (en cours)
   - In Review (en révision)
   - Done (terminé)

### 1.2 Configuration des étiquettes

1. Familiarisation avec les étiquettes par défaut:
   - `bug` - Indique un problème inattendu ou un comportement non désiré
   - `documentation` - Améliorations ou ajouts à la documentation
   - `duplicate` - Issues, pull requests ou discussions similaires
   - `enhancement` - Demandes de nouvelles fonctionnalités
   - `good first issue` - Issues adaptées aux nouveaux contributeurs
   - `help wanted` - Le mainteneur demande de l'aide
   - `invalid` - Issue, pull request ou discussion non pertinente
   - `question` - Besoin d'informations supplémentaires
   - `wontfix` - Travail qui ne sera pas poursuivi

2. Création des étiquettes personnalisées:
   a. Naviguer vers le repository
   b. Cliquer sur "Issues"
   c. Cliquer sur "Labels"
   d. Cliquer sur "New label"
   e. Pour chaque étiquette:
      - Définir un nom explicite
      - Ajouter une description claire
      - Choisir une couleur distinctive (utiliser le sélecteur ou entrer un code hexadécimal)
      - Cliquer sur "Create label"

3. Créer les étiquettes Scrum suivantes:

   | Nom | Description | Couleur suggérée |
   |-----|-------------|------------------|
   | `epic` | Fonctionnalité majeure regroupant plusieurs stories | #3E4B9E |
   | `user story` | Story utilisateur suivant le format "En tant que... je veux... afin de..." | #006B75 |
   | `technical debt` | Refactoring et améliorations techniques nécessaires | #D93F0B |
   | `blocked` | Item bloqué par une dépendance | #D73A4A |

4. Gestion des étiquettes:
   - Pour modifier: utiliser le bouton "Edit" à côté de l'étiquette
   - Pour supprimer: utiliser le bouton "Delete" à côté de l'étiquette
   - Pour appliquer: dans la barre latérale droite d'une issue, cliquer sur "Labels"

5. Configurer les champs personnalisés dans GitHub Projects:
   - Priority (single select: 🔥 High, 📌 Medium, 🔽 Low)
   - Sprint (iteration)
   - Status (single select avec workflow)

6. Pour chaque étiquette créée:
   - Ajouter une description claire
   - Choisir une couleur distinctive
   - S'assurer que le nom est explicite

## Partie 2: Initialisation du Product Backlog

### 2.1 Création des User Stories

1. Dans la vue Table, ajouter des items pour chaque user story:
   a. Format: "En tant que [utilisateur], je veux [action] afin de [bénéfice]"
   b. Ajouter l'étiquette "user story"
   c. Définir la priorité
   d. Estimer les story points
   e. Ajouter les critères d'acceptation dans la description

2. Créer au moins 10 user stories couvrant:
   - Fonctionnalités essentielles
   - Améliorations potentielles
   - Corrections de bugs anticipées

### 2.2 Organisation du Backlog

1. Utiliser le groupement par Priority pour organiser les stories
2. Ajouter des epics pour regrouper les stories liées
3. Définir le Product Goal dans la description du projet

## Partie 3: Planification du Sprint

### 3.1 Sprint Planning

1. Créer une itération (Sprint):
   a. Dans la vue Table, cliquer sur le champ Sprint
   b. Sélectionner "Create iteration"
   c. Définir les dates (2 semaines recommandées)
   d. Nommer le sprint (ex: "Sprint 1")

2. Sélection des User Stories:
   a. Filtrer par Priority
   b. Assigner les stories au sprint créé
   c. Vérifier que le total des story points est réaliste

### 3.2 Décomposition en Tâches

1. Pour chaque User Story:
   a. Créer des sous-tâches dans la description
   b. Estimer chaque tâche
   c. Assigner les responsables

## Partie 4: Exécution du Sprint

### 4.1 Suivi Quotidien

1. Mettre à jour le statut des items:
   a. Utiliser les colonnes de statut appropriées
   b. Documenter les blocages avec l'étiquette "blocked"
   c. Mettre à jour les assignations si nécessaire

2. Utiliser les filtres pour les Daily Scrums:
   - Filtrer par Sprint actuel
   - Grouper par Assignee
   - Identifier les items "In Progress"

### 4.2 Gestion des Changements

1. Pour les nouvelles demandes:
   - Ajouter au Backlog (pas au Sprint en cours)
   - Prioriser appropriement
   - Étiqueter correctement

2. Pour les blocages:
   - Ajouter l'étiquette "blocked"
   - Documenter la raison dans les commentaires
   - Créer des issues liées si nécessaire

## Partie 5: Clôture du Sprint

### 5.1 Sprint Review

1. Préparer un rapport utilisant les vues GitHub:
   - Items complétés vs planifiés
   - Story points réalisés
   - Blocages rencontrés

2. Documenter les feedbacks:
   - Créer des nouvelles issues pour les améliorations
   - Mettre à jour les priorités du Backlog

### 5.2 Sprint Retrospective

1. Créer une issue de rétrospective contenant:
   - Ce qui a bien fonctionné
   - Ce qui peut être amélioré
   - Actions pour le prochain sprint

## Livrables

1. Projet GitHub Projects configuré avec:
   - Vue Table organisée
   - Backlog priorisé
   - Sprint planifié
2. Documentation des cérémonies Scrum
3. Rapport de rétrospective

## Critères d'évaluation

- Configuration correcte de GitHub Projects
- Qualité et organisation des User Stories
- Utilisation appropriée des étiquettes et champs
- Suivi régulier du sprint
- Documentation claire des cérémonies
