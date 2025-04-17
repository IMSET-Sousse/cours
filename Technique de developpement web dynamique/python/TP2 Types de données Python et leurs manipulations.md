# TP2 : Types de données Python et leurs manipulations

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

### Exercices Pratiques - Types Numériques

1. **Calculatrice Simple**

```python
# Créez une calculatrice qui effectue les opérations de base
# et gère la division par zéro
operation = '+'
a, b = 10, 5

if operation == '+':
    resultat = a + b
elif operation == '-':
    resultat = a - b
elif operation == '*':
    resultat = a * b
elif operation == '/':
    if b == 0:
        resultat = "Division par zéro impossible"
    else:
        resultat = a / b

print(resultat)  # Affiche le résultat
```

2. **Conversion de Température**

```python
# Convertissez entre Celsius et Fahrenheit
celsius = 0
fahrenheit = (celsius * 9/5) + 32
print(fahrenheit)  # 32.0

fahrenheit = 98.6
celsius = (fahrenheit - 32) * 5/9
print(celsius)  # 37.0
```

3. **Manipulation de Bits**

```python
# Vérifiez si un nombre est une puissance de 2
n = 16
est_puissance_de_2 = (n > 0) and (n & (n - 1)) == 0
print(est_puissance_de_2)  # True
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

### Exercices Pratiques - Chaînes de caractères

1. **Analyseur de Texte**

```python
texte = "Python 3.9 est SUPER!"
longueur = len(texte)
mots = len(texte.split())
majuscules = sum(1 for c in texte if c.isupper())
minuscules = sum(1 for c in texte if c.islower())
chiffres = sum(1 for c in texte if c.isdigit())

print({'longueur': longueur, 'mots': mots, 'majuscules': majuscules, 'minuscules': minuscules, 'chiffres': chiffres})
```

2. **Validateur d'Email**

```python
email = "user@example.com"
if '@' in email:
    nom, domaine = email.split('@')
    email_valide = (
        len(nom) > 0 and
        len(domaine) > 3 and
        '.' in domaine and
        not any(c in ' ,;:' for c in email)
    )
else:
    email_valide = False

print(email_valide)  # True
```

3. **Formateur de Texte**

```python
texte = "Python est un langage de programmation puissant et facile à apprendre"
largeur = 20
mots = texte.split()
lignes = []
ligne_courante = []

for mot in mots:
    if sum(len(m) for m in ligne_courante) + len(ligne_courante) + len(mot) <= largeur:
        ligne_courante.append(mot)
    else:
        lignes.append(' '.join(ligne_courante))
        ligne_courante = [mot]

if ligne_courante:
    lignes.append(' '.join(ligne_courante))

print('\n'.join(lignes))
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

### Exercices Pratiques - Listes et Tuples

1. **Gestionnaire de Notes**

```python
notes = []

while True:
    note = float(input("Entrez une note (ou -1 pour terminer): "))
    if note == -1:
        break
    if 0 <= note <= 20:
        notes.append(note)
        print("Note ajoutée")
    else:
        print("Note invalide")

if notes:
    moyenne = sum(notes) / len(notes)
    stats = {
        'moyenne': moyenne,
        'min': min(notes),
        'max': max(notes),
        'nombre_notes': len(notes)
    }
else:
    stats = None

print(stats)
```

2. **Manipulation de Matrices**

```python
lignes, colonnes = 2, 2
valeur_defaut = 0
matrice1 = [[valeur_defaut for _ in range(colonnes)] for _ in range(lignes)]
matrice2 = [[valeur_defaut + 1 for _ in range(colonnes)] for _ in range(lignes)]

matrice3 = [[matrice1[i][j] + matrice2[i][j] for j in range(colonnes)] for i in range(lignes)]

for ligne in matrice3:
    print(' '.join(str(x) for x in ligne))
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

### Exercices Pratiques - Dictionnaires

1. **Gestionnaire de Contacts**

```python
contacts = {}

contacts["Alice"] = {'telephone': "0123456789", 'email': "alice@email.com"}
contacts["Bob"] = {'telephone': "9876543210", 'email': "bob@email.com"}

contact_recherche = contacts.get("Alice", "Contact non trouvé")
print(contact_recherche)

contacts.pop("Bob", None)
print(contacts)
```

2. **Analyseur de Fréquence**

```python
texte = "le chat le chien le chat chat"
texte = texte.lower()
mots = texte.split()

frequence = {}
for mot in mots:
    frequence[mot] = frequence.get(mot, 0) + 1

frequence_triee = dict(sorted(frequence.items(), key=lambda x: x[1], reverse=True))
print(frequence_triee)
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

### Exercices Pratiques - Ensembles

1. **Gestionnaire de Bibliothèque**

```python
livres_disponibles = set()
livres_empruntes = set()

livres_disponibles.add("Python pour les débutants")
livres_disponibles.add("Algorithmes avancés")

if "Python pour les débutants" in livres_disponibles:
    livres_disponibles.remove("Python pour les débutants")
    livres_empruntes.add("Python pour les débutants")

status_bibliotheque = {
    'disponibles': livres_disponibles,
    'empruntes': livres_empruntes
}

print(status_bibliotheque)
```

2. **Analyseur de Texte avec Ensembles**

```python
t1 = "Python est un langage génial"
t2 = "Python est facile à apprendre"

mots1 = set(t1.lower().split())
mots2 = set(t2.lower().split())

resultat = {
    'mots_communs': mots1 & mots2,
    'mots_uniques_texte1': mots1 - mots2,
    'mots_uniques_texte2': mots2 - mots1,
    'vocabulaire_total': mots1 | mots2
}

print(resultat)
```

## Projet Final

### Mini-Système de Gestion d'Étudiants

# Créez un système qui combine tous les types de données vus dans ce TP pour gérer des informations sur les étudiants

etudiants = {}
cours = set()
notes = {}

# Ajout d'étudiants

etudiants[1] = {'nom': "Alice Dupont", 'age': 20, 'cours': set()}
notes[1] = {}
etudiants[2] = {'nom': "Bob Martin", 'age': 22, 'cours': set()}
notes[2] = {}

# Inscription aux cours

etudiants[1]['cours'].add("Python")
cours.add("Python")
notes[1]["Python"] = []
etudiants[1]['cours'].add("Java")
cours.add("Java")
notes[1]["Java"] = []
etudiants[2]['cours'].add("Python")
notes[2]["Python"] = []

# Ajout de notes

notes[1]["Python"].extend([15, 18])
notes[1]["Java"].append(12)
notes[2]["Python"].append(14)

# Calcul des moyennes

moyenne1 = sum(notes[1]["Python"]) / len(notes[1]["Python"]) if notes[1]["Python"] else 0
moyenne2 = sum(notes[2]["Python"]) / len(notes[2]["Python"]) if notes[2]["Python"] else 0

# Affichage des rapports

rapport1 = {
'informations': {'nom': etudiants[1]['nom'], 'age': etudiants[1]['age']},
'cours': list(etudiants[1]['cours']),
'notes': notes[1],
'moyenne_generale': moyenne1
}

rapport2 = {
'informations': {'nom': etudiants[2]['nom'], 'age': etudiants[2]['age']},
'cours': list(etudiants[2]['cours']),
'notes': notes[2],
'moyenne_generale': moyenne2
}

print(rapport1)
print(rapport2)

## Ressources supplémentaires

- [Documentation Python - Types de données](https://docs.python.org/fr/3/library/stdtypes.html)
- [W3Schools - Python Data Types](https://www.w3schools.com/python/python_datatypes.asp)
- [Python Tutor - Visualisation des types](http://www.pythontutor.com/)
