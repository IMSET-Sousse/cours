# TP2 : Structures de contrôle et fonctions en Python

## Objectifs du TP

- Maîtriser les opérations logiques en Python
- Comprendre et utiliser les structures conditionnelles
- Apprendre à créer et utiliser des fonctions
- Gérer les exceptions et les erreurs

## 1. Opérations logiques

### Opérateurs logiques de base

```python
# Opérateurs AND, OR, NOT
a = True
b = False

# AND (et)
print(a and b)  # False
print(a and True)  # True

# OR (ou)
print(a or b)  # True
print(False or b)  # False

# NOT (non)
print(not a)  # False
print(not b)  # True

# Combinaisons
print((a and b) or (not a))  # False
print(not (a or b))  # False
```

### Comparaisons et opérations logiques

```python
# Opérateurs de comparaison
x = 5
y = 10

print(x < y)   # True
print(x > y)   # False
print(x <= y)  # True
print(x >= y)  # False
print(x == y)  # False
print(x != y)  # True

# Combinaison avec opérations logiques
print((x < y) and (y > 0))  # True
print((x > y) or (y > 0))   # True
print(not (x == y))         # True
```

## 2. Structures conditionnelles

### if, elif, else

```python
# Structure de base
age = 18
if age < 18:
    print("Mineur")
elif age >= 18 and age < 65:
    print("Adulte")
else:
    print("Senior")

# Conditions imbriquées
note = 85
if note >= 90:
    print("Excellent")
elif note >= 80:
    print("Très bien")
elif note >= 70:
    print("Bien")
else:
    print("À améliorer")

# Conditions avec opérations logiques
temperature = 25
pluie = True

if temperature > 30 and not pluie:
    print("Il fait très chaud et il ne pleut pas")
elif temperature > 20 and not pluie:
    print("Il fait bon et il ne pleut pas")
elif temperature > 20 and pluie:
    print("Il fait bon mais il pleut")
else:
    print("Il fait froid")
```

### Expressions conditionnelles (ternaire)

```python
# Syntaxe: valeur_si_vrai if condition else valeur_si_faux
age = 20
statut = "Majeur" if age >= 18 else "Mineur"
print(statut)  # Majeur

# Utilisation dans des calculs
x = 10
y = 20
maximum = x if x > y else y
print(maximum)  # 20
```

## 3. Boucles

### Boucle for

```python
# Boucle for avec range
for i in range(5):  # 0 à 4
    print(i)

# Boucle for avec liste
fruits = ["pomme", "banane", "orange"]
for fruit in fruits:
    print(fruit)

# Boucle for avec dictionnaire
personne = {"nom": "Alice", "age": 25, "ville": "Paris"}
for cle, valeur in personne.items():
    print(f"{cle}: {valeur}")

# Boucle for avec enumerate
for index, fruit in enumerate(fruits):
    print(f"{index + 1}. {fruit}")
```

### Boucle while

```python
# Boucle while simple
compteur = 0
while compteur < 5:
    print(compteur)
    compteur += 1

# Boucle while avec condition complexe
nombre = 0
while nombre < 100 and nombre % 2 == 0:
    print(nombre)
    nombre += 2

# Boucle infinie avec break
while True:
    reponse = input("Entrez 'q' pour quitter: ")
    if reponse.lower() == 'q':
        break
    print("Continuer...")
```

### Instructions de contrôle

```python
# break
for i in range(10):
    if i == 5:
        break
    print(i)  # 0, 1, 2, 3, 4

# continue
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)  # 1, 3, 5, 7, 9

# pass
for i in range(5):
    if i == 3:
        pass  # À implémenter plus tard
    print(i)
```

## 4. Fonctions

### Définition et appel de fonctions

```python
# Fonction simple
def dire_bonjour():
    print("Bonjour !")

# Fonction avec paramètres
def addition(a, b):
    return a + b

# Fonction avec paramètres par défaut
def saluer(nom="Utilisateur"):
    print(f"Bonjour, {nom}!")

# Fonction avec arguments variables
def somme(*nombres):
    return sum(nombres)

# Appel des fonctions
dire_bonjour()
resultat = addition(5, 3)
saluer("Alice")
saluer()  # Utilise la valeur par défaut
print(somme(1, 2, 3, 4, 5))  # 15
```

### Portée des variables

```python
# Variable globale
x = 10

def modifier_x():
    global x
    x = 20

def fonction_locale():
    y = 30  # Variable locale
    print(y)

modifier_x()
print(x)  # Affiche 20
fonction_locale()
# print(y)  # Erreur : y n'est pas définie globalement
```

### Fonctions récursives

```python
def factorielle(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorielle(n - 1)

print(factorielle(5))  # Affiche 120

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(10))  # Affiche 55
```

## 5. Gestion des exceptions

### Try, except, finally

```python
# Gestion d'erreur simple
try:
    resultat = 10 / 0
except ZeroDivisionError:
    print("Division par zéro impossible")

# Gestion de plusieurs types d'erreurs
try:
    nombre = int(input("Entrez un nombre : "))
    resultat = 10 / nombre
except ValueError:
    print("Veuillez entrer un nombre valide")
except ZeroDivisionError:
    print("Division par zéro impossible")
finally:
    print("Fin du programme")

# Gestion d'erreurs avec else
try:
    fichier = open("test.txt", "r")
except FileNotFoundError:
    print("Fichier non trouvé")
else:
    contenu = fichier.read()
    print(contenu)
    fichier.close()
```

### Lever des exceptions

```python
def verifier_age(age):
    if age < 0:
        raise ValueError("L'âge ne peut pas être négatif")
    elif age < 18:
        raise ValueError("Vous devez être majeur")
    return True

try:
    verifier_age(-5)
except ValueError as e:
    print(f"Erreur : {e}")

# Création d'exceptions personnalisées
class AgeInvalideError(Exception):
    pass

def verifier_age_personnalise(age):
    if age < 0:
        raise AgeInvalideError("Âge invalide")
    return True
```

## 6. Exercices pratiques

### Exercice 1 : Calculatrice améliorée

1. Créez une calculatrice qui :
   - Accepte une liste d'opérations
   - Gère les erreurs de saisie
   - Permet de quitter proprement
   - Affiche l'historique des calculs

### Exercice 2 : Jeu de devinette

1. Développez un jeu où :
   - L'ordinateur choisit un nombre aléatoire
   - Le joueur doit deviner le nombre
   - Le programme donne des indices
   - Le score est enregistré

### Exercice 3 : Gestion de liste

1. Créez un programme qui :
   - Permet d'ajouter/supprimer des éléments
   - Trie la liste
   - Recherche des éléments
   - Sauvegarde la liste dans un fichier

## Ressources supplémentaires

- [Documentation Python - Structures de contrôle](https://docs.python.org/fr/3/tutorial/controlflow.html)
- [Documentation Python - Fonctions](https://docs.python.org/fr/3/tutorial/controlflow.html#defining-functions)
- [W3Schools - Python Functions](https://www.w3schools.com/python/python_functions.asp)
