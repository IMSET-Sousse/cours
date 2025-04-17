# Types de données Python et leurs manipulations

## Types de données fondamentaux

Python possède plusieurs types de données natifs qui permettent de représenter différentes sortes d'informations :

### Types numériques

#### Entiers (int)

Les entiers sont des nombres sans partie décimale. Ils peuvent être positifs ou négatifs. Par exemple, 3, -1, 42 et 0 sont tous des entiers. Les entiers sont utilisés pour représenter des quantités discrètes, comme le nombre d'éléments dans une liste ou le score d'un jeu.

Voici quelques exemples d'utilisation des entiers en Python :

```python
age = 25
nombre_etudiants = 30

print(age)
print(nombre_etudiants)
```

#### Flottants (float)

Les flottants sont des nombres à virgule flottante, c'est-à-dire des nombres avec une partie décimale. Ils peuvent représenter des valeurs continues, comme des mesures ou des pourcentages. Par exemple, 3.14, -0.001 et 2.0 sont des flottants.

Voici quelques exemples d'utilisation des flottants en Python :

```python
prix = 19.99
temperature = -2.5

print(prix)
print(temperature)
```

### Chaînes de caractères (str)

Les chaînes de caractères sont des séquences de caractères utilisées pour représenter du texte.

Voici quelques exemples d'utilisation des chaînes de caractères en Python :

```python
nom = "Alice"
message = "Bonjour, comment ça va ?"

print(nom)
print(message)
```

### Listes (list)

Les listes sont des collections ordonnées et modifiables d'éléments. Elles peuvent contenir des éléments de types différents.

Voici quelques exemples d'utilisation des listes en Python :

```python
ma_liste = [1, "deux", 3.0]
```

### Tuples (tuple)

Les tuples sont des collections ordonnées mais immuables d'éléments. Comme les listes, ils peuvent contenir des éléments de types différents.

### Dictionnaires (dict)

Les dictionnaires sont des collections non ordonnées de paires clé-valeur. Chaque clé doit être unique.

### Ensembles (set)

Les ensembles sont des collections non ordonnées d'éléments uniques.

### Booléens (bool)

Les booléens représentent des valeurs de vérité et peuvent être soit True soit False.

## Conversion entre types (type casting)

Python permet de convertir des valeurs d'un type à un autre :

- `int()`
- `float()`
- `str()`
- `list()`
- `tuple()`
- `dict()`
- `set()`

## Opérations arithmétiques

Python permet d'effectuer des opérations arithmétiques sur les types numériques :

- Addition (+)
- Soustraction (-)
- Multiplication (*)
- Division (/)
- Division entière (//)
- Modulo (%)
- Exponentiation (**)

## Méthodes spécifiques à chaque type de données

### Méthodes pour les chaînes de caractères (str)

- `split()`
- `join()`
- `replace()`
- `upper()`
- `lower()`

### Méthodes pour les listes (list)

- `append()`
- `extend()`
- `pop()`
- `remove()`
- `sort()`

### Méthodes pour les dictionnaires (dict)

- `keys()`
- `values()`
- `items()`
- `get()`
- `update()`
