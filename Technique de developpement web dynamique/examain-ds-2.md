# Examen DS Technique de développement web dynamique

## Exercice 1 : Types de données Python

Créez un programme qui :

- Demande à l'utilisateur de saisir deux nombres (entiers ou décimaux)
- Stocke ces nombres dans des variables appropriées
- Effectue les opérations suivantes :
  - Addition
  - Multiplication
  - Puissance
- Affiche les résultats avec le bon type de données

Exemple de sortie avec nombre1 = 5.2 et nombre2 = 3.0:

```python
5.2 + 3.0 = 8.2
5.2 * 3.0 = 15.6
5.2 ** 3.0 = 140.608
```

## Exercice 2 : Structures conditionnelles

Créez un programme qui :

- Demande à l'utilisateur de saisir un nombre
- Vérifie si ce nombre est positif, négatif ou nul
- Vérifie si ce nombre est pair ou impair
- Affiche tous les résultats avec des messages appropriés

Exemple de sortie avec nombre = 5:

```python
5 est positif et impair
```

## Exercice 3 : Structures répétitives

Créez un programme qui :
Demande à l'utilisateur de saisir un nombre N:

- Calculer la somme des nombres de 1 a N
- Calculer la factorielle de N (le produit de tous les entiers de 1 à N)

Exemple de sortie avec nombre = 5:

```python
La somme des nombres de 1 à 5 est 15
La factorielle de 5 est 120
```

## Projet : Gestionnaire de Budget Personnel

### Interface utilisateur

- Le programme doit demander à l'utilisateur de saisir :
  - Le revenu mensuel (float) : Entrez votre salaire ou autres revenus mensuels
  - Le loyer (float) : Montant mensuel de votre loyer ou crédit immobilier
  - Les factures (float) : Total des factures mensuelles (électricité, eau, internet, etc.)
  - Les courses (float) : Budget mensuel pour l'alimentation et produits courants
  - Les loisirs (float) : Dépenses de loisirs, sorties, activités
  - L'épargne souhaitée (float) : Montant que vous souhaitez mettre de côté chaque mois

- L'utilisateur doit ensuite choisir une opération parmi :
  - Calculer le budget total disponible (B) : Affiche l'argent disponible après toutes les dépenses
  - Calculer le total des dépenses (D) : Fait la somme de toutes vos dépenses mensuelles
  - Calculer l'épargne réalisable (E) : Vérifie si votre objectif d'épargne est atteignable
  - Vérifier l'équilibre budgétaire (V) : Compare vos revenus et dépenses pour déterminer si :
    - Le budget est équilibré (revenus = dépenses)
    - Il y a un excédent (revenus > dépenses)
    - Il y a un déficit (revenus < dépenses)
    - Affiche le pourcentage des dépenses par rapport aux revenus
  - Afficher le rapport budgétaire détaillé (F) : Montre un résumé complet de votre situation financière avec :
    - Le détail de toutes les dépenses mensuelles (loyer, factures, courses, loisirs)
    - Le pourcentage que représente chaque dépense par rapport au revenu total
    - Le montant disponible après dépenses
    - L'épargne possible et son pourcentage par rapport au revenu
    - Un indicateur visuel de l'équilibre budgétaire (+ ou - selon excédent/déficit)
  - Taper '/q' pour quitter le programme : Permet de sortir du programme

### Test des calculs

1. Calcul du budget disponible (B)

```python
Revenu mensuel: 2500
Loyer: 800
Factures: 200
Courses: 400
Loisirs: 300
Épargne souhaitée: 300
Opération (B, D, E, V, F, /q): B
Budget disponible = 500.0 TND
```

2. Calcul du total des dépenses (D)

```python
Revenu mensuel: 2500
Loyer: 800
Factures: 200
Courses: 400
Loisirs: 300
Épargne souhaitée: 300
Opération (B, D, E, V, F, /q): D
Total des dépenses = 2000.0 TND
```

3. Calcul de l'épargne réalisable (E)

```python
Revenu mensuel: 2500
Loyer: 800
Factures: 200
Courses: 400
Loisirs: 300
Épargne souhaitée: 300
Opération (B, D, E, V, F, /q): E
Épargne est réalisable
```

4. Vérification de l'équilibre budgétaire (V)

```python
Revenu mensuel: 2500
Loyer: 800
Factures: 200
Courses: 400
Loisirs: 300
Épargne souhaitée: 300
Opération (B, D, E, V, F, /q): V
État du budget: + EXCÉDENT
```

5. Rapport budgétaire détaillé (F)

```python
=== RAPPORT BUDGÉTAIRE DÉTAILLÉ ===
Revenu mensuel:        2500.00 TND
---------------------------
Dépenses mensuelles:
Loyer:                  800.00 TND (32.0%)
Factures:               200.00 TND (8.0%)
Courses:                400.00 TND (16.0%)
Loisirs:                300.00 TND (12.0%)
Épargne souhaitée:      300.00 TND (12.0%)
---------------------------
Total des dépenses:    2000.00 TND (80.0%)
Budget disponible:      500.00 TND (20.0%)
---------------------------
État du budget: + EXCÉDENT
=============================
```

### Formules de calcul

- Budget disponible = Revenu mensuel - (Loyer + Factures + Courses + Loisirs + Épargne)
- Total des dépenses = Loyer + Factures + Courses + Loisirs + Épargne
- Pourcentage par poste = (Montant du poste / Revenu mensuel) × 100
- Épargne réalisable = Budget disponible ≥ Épargne souhaitée
- État du budget:
  - Équilibré si Revenu = Dépenses totales
  - Excédent si Revenu > Dépenses totales
  - Déficit si Revenu < Dépenses totales
