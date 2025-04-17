# TP1 : Types de données Python et leurs manipulations

## Objectifs du TP

- Maîtriser les types de données fondamentaux en Python
- Comprendre et appliquer les opérations arithmétiques
- Utiliser les méthodes spécifiques à chaque type
- Gérer les conversions entre types
- Manipuler efficacement les collections de données

## 1. Types numériques

### Entiers (int)

Les entiers en Python sont des nombres entiers de taille arbitraire (limitée uniquement par la mémoire disponible).

```python
# Opérations de base
a = 10
b = 3
print(a + b)  # Addition: 13
print(a - b)  # Soustraction: 7
print(a * b)  # Multiplication: 30
print(a / b)  # Division: 3.333... (retourne un float)
print(a // b) # Division entière: 3 (retourne un int)
print(a % b)  # Modulo: 1 (reste de la division)
print(a ** b) # Puissance: 1000

# Méthodes utiles
nombre = 42
print(bin(nombre))  # Conversion en binaire: '0b101010'
print(hex(nombre))  # Conversion en hexadécimal: '0x2a'
print(abs(-42))     # Valeur absolue: 42
print(pow(2, 3))    # Puissance (équivalent à **): 8

# Opérations sur les bits
x = 5  # 101 en binaire
y = 3  # 011 en binaire
print(x & y)   # ET bit à bit: 1 (001)
print(x | y)   # OU bit à bit: 7 (111)
print(x ^ y)   # OU exclusif: 6 (110)
print(~x)      # Complément à 1: -6
print(x << 1)  # Décalage à gauche: 10 (1010)
print(x >> 1)  # Décalage à droite: 2 (10)
```

### Flottants (float)

Les nombres flottants en Python sont des nombres à virgule flottante de double précision (64 bits).

```python
# Opérations de base
x = 3.14
y = 2.71
print(x + y)  # Addition
print(x - y)  # Soustraction
print(x * y)  # Multiplication
print(x / y)  # Division

# Méthodes utiles
print(int(3.7))  # Arrondi inférieur: 3
print(int(3.2) + 1)   # Arrondi supérieur: 4
print(round(3.14159, 2)) # Arrondi à 2 décimales: 3.14

# Comparaison de flottants
def est_proche(a, b, tolerance=1e-9):
    return abs(a - b) < tolerance

print(est_proche(0.1 + 0.2, 0.3))  # True

# Valeurs spéciales
print(float('inf'))  # Infini positif
print(float('-inf')) # Infini négatif
print(float('nan'))  # Not a Number
```

## 2. Chaînes de caractères (str)

Les chaînes de caractères en Python sont des séquences immuables d'Unicode.

```python
# Création et manipulation
s1 = "Bonjour"
s2 = "monde"
print(s1 + " " + s2)  # Concaténation: "Bonjour monde"
print(f"{s1} {s2}")   # Formatage f-string (Python 3.6+)
print("{} {}".format(s1, s2))  # Formatage avec format()

# Indexation et slicing
s = "Python"
print(s[0])      # Premier caractère: 'P'
print(s[-1])     # Dernier caractère: 'n'
print(s[1:4])    # Sous-chaîne: 'yth'
print(s[::2])    # Un caractère sur deux: 'Pto'
print(s[::-1])   # Inversion: 'nohtyP'

# Méthodes importantes
s = "  Python est génial!  "

# Manipulation de casse
print(s.upper())      # Majuscules: "  PYTHON EST GÉNIAL!  "
print(s.lower())      # Minuscules: "  python est génial!  "
print(s.title())      # Première lettre en majuscule: "  Python Est Génial!  "
print(s.capitalize()) # Première lettre en majuscule: "  python est génial!  "

# Recherche et remplacement
print(s.find("est"))     # Position de "est": 8
print(s.rfind("est"))    # Dernière position de "est"
print(s.replace("est", "est très"))  # Remplacement
print("est" in s)        # Vérification d'appartenance: True

# Nettoyage et séparation
print(s.strip())         # Suppression des espaces
print(s.lstrip())        # Suppression des espaces à gauche
print(s.rstrip())        # Suppression des espaces à droite
print(s.split())         # Découpage en mots: ['Python', 'est', 'génial!']
print("-".join(["a", "b", "c"]))  # Concaténation avec séparateur: "a-b-c"

# Vérification
print(s.isalpha())      # Vérifie si tous les caractères sont alphabétiques
print(s.isdigit())      # Vérifie si tous les caractères sont des chiffres
print(s.isalnum())      # Vérifie si tous les caractères sont alphanumériques
print(s.startswith("Py"))  # Vérifie le début
print(s.endswith("!"))     # Vérifie la fin
```

## 3. Listes et tuples

### Listes (list)

Les listes sont des séquences mutables d'éléments hétérogènes.

```python
# Création et manipulation
ma_liste = [1, 2, 3, 4, 5]
print(ma_liste[0])      # Accès par index: 1
print(ma_liste[-1])     # Dernier élément: 5
print(ma_liste[1:3])    # Slicing: [2, 3]
print(ma_liste[::2])    # Un élément sur deux: [1, 3, 5]

# Méthodes importantes
ma_liste.append(6)      # Ajout en fin
ma_liste.insert(0, 0)   # Insertion à une position
ma_liste.extend([7, 8]) # Extension avec une autre liste
ma_liste.remove(3)      # Suppression d'un élément
ma_liste.pop()          # Suppression du dernier élément
ma_liste.sort()         # Tri
ma_liste.reverse()      # Inversion

# List comprehension
nombres_pairs = [x for x in range(10) if x % 2 == 0]
nombres_carres = [x**2 for x in range(5)]
paires = [(x, y) for x in range(3) for y in range(3)]

# Opérations sur les listes
print(len(ma_liste))    # Longueur
print(min(ma_liste))    # Minimum
print(max(ma_liste))    # Maximum
print(sum(ma_liste))    # Somme
```

### Tuples (tuple)

Les tuples sont des séquences immuables d'éléments hétérogènes.

```python
# Création et manipulation
mon_tuple = (1, 2, 3, 4, 5)
print(mon_tuple[0])     # Accès par index: 1
print(mon_tuple[1:3])   # Slicing: (2, 3)
print(mon_tuple[::2])   # Un élément sur deux: (1, 3, 5)

# Méthodes disponibles
print(mon_tuple.count(2))  # Compte les occurrences
print(mon_tuple.index(3))  # Trouve l'index d'un élément

# Déballage de tuple
a, b, c = (1, 2, 3)
x, *y = (1, 2, 3, 4)  # x = 1, y = [2, 3, 4]

# Utilisation de tuples
point = (1, 2)  # Coordonnées x, y
print(point[0])  # x: 1
print(point[1])  # y: 2

# Tuples imbriqués
points = ((1, 2), (3, 4), (5, 6))
print(points[0])     # (1, 2)
print(points[0][0])  # 1
print(points[0][1])  # 2
```

## 4. Dictionnaires (dict)

Les dictionnaires sont des collections non ordonnées de paires clé-valeur.

```python
# Création et manipulation
mon_dict = {"nom": "Alice", "age": 25, "ville": "Paris"}
print(mon_dict["nom"])  # Accès par clé: "Alice"
mon_dict["age"] = 26    # Modification
mon_dict["pays"] = "France"  # Ajout

# Méthodes importantes
print(mon_dict.keys())    # Liste des clés
print(mon_dict.values())  # Liste des valeurs
print(mon_dict.items())   # Liste des paires clé-valeur

# Manipulation
mon_dict.update({"profession": "Ingénieur"})  # Mise à jour
del mon_dict["ville"]     # Suppression
print(mon_dict.get("nom", "Inconnu"))  # Accès sécurisé
print(mon_dict.setdefault("langue", "Français"))  # Ajout si absent

# Dictionary comprehension
carrés = {x: x**2 for x in range(5)}
filtre = {k: v for k, v in mon_dict.items() if len(k) > 3}
```

## 5. Ensembles (set)

Les ensembles sont des collections non ordonnées d'éléments uniques.

```python
# Création et manipulation
mon_set = {1, 2, 3, 4, 5}
autre_set = {4, 5, 6, 7, 8}

# Opérations ensemblistes
print(mon_set.union(autre_set))        # Union: {1, 2, 3, 4, 5, 6, 7, 8}
print(mon_set.intersection(autre_set)) # Intersection: {4, 5}
print(mon_set.difference(autre_set))   # Différence: {1, 2, 3}
print(mon_set.symmetric_difference(autre_set))  # Différence symétrique: {1, 2, 3, 6, 7, 8}

# Méthodes importantes
mon_set.add(6)          # Ajout d'un élément
mon_set.remove(1)       # Suppression d'un élément (lève une erreur si absent)
mon_set.discard(10)     # Suppression sécurisée (ne lève pas d'erreur)
mon_set.pop()           # Suppression d'un élément aléatoire
mon_set.clear()         # Vidage de l'ensemble

# Set comprehension
nombres_pairs = {x for x in range(10) if x % 2 == 0}
```

## 6. Opérateurs Logiques et Booléens

### Introduction aux Opérateurs Logiques

Les opérateurs logiques en Python permettent de combiner des expressions booléennes pour former des conditions plus complexes. Ils sont essentiels pour le contrôle de flux et la prise de décision dans les programmes.

### Opérateurs Booléens de Base

#### AND (et)

L'opérateur `and` retourne `True` uniquement si les deux opérandes sont `True`. Si le premier opérande est `False`, Python n'évalue même pas le second (court-circuit).

```python
# Exemples d'opérateur AND
print(True and True)    # True
print(True and False)   # False
print(False and True)   # False
print(False and False)  # False

# Exemple pratique
age = 25
permis = True
peut_conduire = age >= 18 and permis  # True
```

#### OR (ou)

L'opérateur `or` retourne `True` si au moins un des opérandes est `True`. Si le premier opérande est `True`, Python n'évalue pas le second (court-circuit).

```python
# Exemples d'opérateur OR
print(True or True)     # True
print(True or False)    # True
print(False or True)    # True
print(False or False)   # False

# Exemple pratique
pluie = False
parapluie = True
peut_sortir = not pluie or parapluie  # True
```

#### NOT (non)

L'opérateur `not` inverse la valeur booléenne de son opérande.

```python
# Exemples d'opérateur NOT
print(not True)   # False
print(not False)  # True

# Exemple pratique
est_ferme = False
est_ouvert = not est_ferme  # True
```

### Priorité des Opérateurs Logiques

La priorité des opérateurs logiques est la suivante (du plus prioritaire au moins prioritaire) :

1. `not`
2. `and`
3. `or`

```python
# Exemple de priorité
resultat = not True and False or True  # Équivaut à ((not True) and False) or True
print(resultat)  # True
```

### Opérateurs de Comparaison

Les opérateurs de comparaison retournent des valeurs booléennes (`True` ou `False`).

```python
# Opérateurs de comparaison
x = 5
y = 10

# Égalité et différence
print(x == y)  # False (égalité)
print(x != y)  # True (différence)

# Comparaisons numériques
print(x < y)   # True (inférieur)
print(x > y)   # False (supérieur)
print(x <= y)  # True (inférieur ou égal)
print(x >= y)  # False (supérieur ou égal)

# Comparaisons de chaînes (ordre lexicographique)
s1 = "abc"
s2 = "def"
print(s1 < s2)  # True
```

### Opérateurs d'Identité

Les opérateurs `is` et `is not` vérifient si deux objets sont le même objet en mémoire.

```python
# Opérateurs d'identité
a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is b)     # False (objets différents)
print(a is c)     # True (même objet)
print(a is not b) # True
```

### Opérateurs d'Appartenance

Les opérateurs `in` et `not in` vérifient si un élément est présent dans une séquence.

```python
# Opérateurs d'appartenance
liste = [1, 2, 3, 4, 5]
chaine = "Bonjour"

print(3 in liste)        # True
print(6 not in liste)    # True
print("jour" in chaine)  # True
print("soir" not in chaine)  # True
```

### Combinaison d'Opérateurs

Les opérateurs logiques peuvent être combinés pour former des conditions complexes.

```python
# Exemples de combinaisons
age = 25
permis = True
experience = 2

# Conditions complexes
peut_conduire = age >= 18 and permis
peut_location = age >= 21 and permis and experience >= 1
peut_voiture_sport = age >= 25 and permis and experience >= 3

# Utilisation de parenthèses pour clarifier
condition = (age >= 18 and permis) or (age >= 16 and not permis)
```

### Exercices Pratiques

1. Vérification d'âge et de permis

```python
age = 20
permis = True
experience = 1

# Vérifie si la personne peut conduire une voiture de location
peut_location = age >= 21 and permis and experience >= 1
print(peut_location)  # False
```

2. Validation de mot de passe

```python
mot_de_passe = "Python123"
longueur_ok = len(mot_de_passe) >= 8
contient_maj = any(c.isupper() for c in mot_de_passe)
contient_chiffre = any(c.isdigit() for c in mot_de_passe)

mot_de_passe_valide = longueur_ok and contient_maj and contient_chiffre
print(mot_de_passe_valide)  # True
```

3. Vérification de température

```python
temperature = 25
humidite = 60
vent = 15

# Conditions météorologiques
trop_chaud = temperature > 30
trop_humide = humidite > 70
trop_vent = vent > 20

# Vérifie si les conditions sont favorables
conditions_favorables = not (trop_chaud or trop_humide or trop_vent)
print(conditions_favorables)  # True
```

### Bonnes Pratiques

1. Utilisez des parenthèses pour clarifier l'ordre des opérations
2. Évitez les conditions trop complexes - décomposez-les en plusieurs étapes
3. Utilisez des variables intermédiaires pour améliorer la lisibilité
4. Privilégiez les conditions positives plutôt que négatives
5. Utilisez des noms de variables descriptifs pour les conditions

## 7. Conversion entre types

```python
# Conversion explicite
nombre = 42
chaine = str(nombre)      # Vers chaîne: "42"
entier = int("123")       # Vers entier: 123
flottant = float("3.14")  # Vers flottant: 3.14
liste = list("abc")       # Vers liste: ['a', 'b', 'c']
tuple = tuple([1, 2, 3])  # Vers tuple: (1, 2, 3)
ensemble = set([1, 2, 3]) # Vers ensemble: {1, 2, 3}

# Conversion implicite
resultat = 3 + 4.5  # int + float = float
resultat = "abc" * 3  # str * int = str: "abcabcabc"
```

## 8. Exercices pratiques

### Exercice 1 : Formateur de texte

1. Créez un programme qui :
   - Accepte un texte en entrée
   - Compte le nombre de mots
   - Trouve les mots les plus fréquents
   - Formate le texte selon des règles spécifiques

### Exercice 2 : Calculatrice multi-types

1. Développez une calculatrice qui :
   - Gère les entiers et les flottants
   - Convertit automatiquement les types
   - Gère les erreurs de division par zéro
   - Affiche les résultats formatés

### Exercice 3 : Gestion de collection

1. Créez un programme qui :
   - Stocke des données dans différentes structures
   - Permet d'ajouter/supprimer des éléments
   - Effectue des recherches efficaces
   - Sauvegarde les données dans un fichier

## Ressources supplémentaires

- [Documentation Python - Types de données](https://docs.python.org/fr/3/library/stdtypes.html)
- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [Python Tutor - Visualisation des types](http://www.pythontutor.com/)
