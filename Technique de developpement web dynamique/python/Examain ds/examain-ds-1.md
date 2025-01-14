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
Entrez le premier nombre: 5.2
Entrez le deuxième nombre: 3
5.2  +  3.0  =  8.2
5.2  *  3.0  =  15.600000000000001
5.2  **  3.0  =  140.608
```

## Exercice 2 : Structures conditionnelles

Créez un programme qui :

- Demande à l'utilisateur de saisir un nombre
- Vérifie si ce nombre est positif, négatif ou nul
- Vérifie si ce nombre est pair ou impair
- Affiche tous les résultats avec des messages appropriés

Exemple de sortie avec nombre = 5:

```python
Entrez un nombre: 5
5 est positif et impair
```

## Exercice 3 : Structures répétitives

Créez un programme qui :
Demande à l'utilisateur de saisir un nombre N:

- Calculer la somme des nombres de 1 a N
- Calculer la factorielle de N (le produit de tous les entiers de 1 à N)

Exemple de sortie avec nombre = 5:

```python
Entrez un nombre: 5
La somme des nombres de 1 à 5 est 15
La factorielle de 5 est 120
```

## Projet RH : Calculateur de Paie

### Interface utilisateur

- Le programme doit demander à l'utilisateur de saisir :
  - Le salaire brut de base
  - Le nombre d'heures supplémentaires
  - Le taux des heures supplémentaires (75% pour jours ouvrables, 100% pour jours de repos)
  - Les primes éventuelles
- L'utilisateur doit ensuite choisir une opération parmi :
  - Calculer le salaire brut total (B)
  - Calculer les cotisations sociales (C)
  - Calculer le salaire net (N)
  - Calculer le coût employeur (E)
  - Afficher la fiche de paie complète (F)
  - Taper '/q' pour quitter le programme

### Test des calculs

1. Calcul du salaire brut

```python
Salaire de base: 1000
Heures supplémentaires: 10
Taux majoré (1.75 ou 2.00): 1.75
Primes: 100
Opération (B, C, N, E, F, /q): B
Salaire brut total = 1300.0
```

1. Calcul des cotisations

```python
Salaire de base: 1000
Heures supplémentaires: 10
Taux majoré (1.75 ou 2.00): 1.75
Primes: 100
Opération (B, C, N, E, F, /q): C
Cotisations sociales = 143.00  # 9.18% salarié + 1.82% assurance maladie
```

1. Fiche de paie complète

```python
=== FICHE DE PAIE TUNISIENNE ===
Salaire de base:         1000.00 TND
Heures supplémentaires:   200.00 TND
Primes:                   100.00 TND
---------------------------
Salaire brut:           1300.00 TND
Cotisations CNSS (9.18%): 119.34 TND
Assurance maladie (1.82%): 23.66 TND
---------------------------
Salaire net:            1157.00 TND
Charges patronales:      447.20 TND
Coût employeur:         1747.20 TND
=============================
```

### Formules de calcul

- Salaire brut = Salaire de base + (Heures sup × Taux horaire × Taux majoré) + Primes
- Taux horaire = Salaire de base / 173.33 (heures mensuelles en Tunisie)
- Cotisations salariales = Salaire brut × 11% (9.18% CNSS + 1.82% assurance maladie)
- Cotisations patronales = Salaire brut × 16.57% (CNSS)
- Coût employeur = Salaire brut + Cotisations patronales
