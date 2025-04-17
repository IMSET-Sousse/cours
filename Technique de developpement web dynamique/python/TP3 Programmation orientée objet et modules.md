# TP3 : Programmation orientée objet et modules en Python

## Objectifs du TP

- Comprendre les concepts de la programmation orientée objet
- Maîtriser les classes et les objets
- Apprendre à créer et utiliser des modules
- Gérer l'héritage et le polymorphisme

## 1. Programmation orientée objet

### Classes et objets

```python
# Définition d'une classe simple
class Personne:
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def se_presenter(self):
        print(f"Je m'appelle {self.nom} et j'ai {self.age} ans.")

# Création d'objets
personne1 = Personne("Alice", 25)
personne2 = Personne("Bob", 30)

# Utilisation des méthodes
personne1.se_presenter()
personne2.se_presenter()
```

### Encapsulation

```python
class CompteBancaire:
    def __init__(self, titulaire, solde=0):
        self._titulaire = titulaire  # Attribut protégé
        self.__solde = solde        # Attribut privé
    
    def deposer(self, montant):
        if montant > 0:
            self.__solde += montant
            return True
        return False
    
    def retirer(self, montant):
        if 0 < montant <= self.__solde:
            self.__solde -= montant
            return True
        return False
    
    def get_solde(self):
        return self.__solde

# Utilisation
compte = CompteBancaire("Alice")
compte.deposer(1000)
print(compte.get_solde())  # Affiche 1000
```

### Héritage

```python
class Animal:
    def __init__(self, nom):
        self.nom = nom
    
    def parler(self):
        pass

class Chien(Animal):
    def parler(self):
        return "Woof!"

class Chat(Animal):
    def parler(self):
        return "Miaou!"

# Utilisation
chien = Chien("Rex")
chat = Chat("Mimi")

print(f"{chien.nom} dit {chien.parler()}")
print(f"{chat.nom} dit {chat.parler()}")
```

### Polymorphisme

```python
class Forme:
    def aire(self):
        pass

class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
    
    def aire(self):
        return self.largeur * self.hauteur

class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    
    def aire(self):
        return 3.14 * self.rayon ** 2

# Utilisation
formes = [Rectangle(4, 5), Cercle(3)]
for forme in formes:
    print(f"Aire : {forme.aire()}")
```

## 2. Modules et packages

### Création et utilisation de modules

```python
# fichier: geometrie.py
def aire_rectangle(largeur, hauteur):
    return largeur * hauteur

def aire_cercle(rayon):
    return 3.14 * rayon ** 2

# fichier: main.py
import geometrie

print(geometrie.aire_rectangle(4, 5))
print(geometrie.aire_cercle(3))
```

### Packages

```python
# Structure de dossiers:
# mon_package/
#     __init__.py
#     module1.py
#     module2.py
#     sous_package/
#         __init__.py
#         module3.py

# Utilisation
from mon_package import module1
from mon_package.sous_package import module3
```

### Modules standards

```python
import math
import random
import datetime
import json
import os

# Exemples d'utilisation
print(math.sqrt(16))  # 4.0
print(random.randint(1, 10))  # Nombre aléatoire entre 1 et 10
print(datetime.datetime.now())  # Date et heure actuelles
```

## 3. Gestion des fichiers

### Lecture et écriture

```python
# Écriture
with open("fichier.txt", "w") as f:
    f.write("Bonjour le monde!")

# Lecture
with open("fichier.txt", "r") as f:
    contenu = f.read()
    print(contenu)
```

### JSON

```python
import json

# Écriture
data = {"nom": "Alice", "age": 25}
with open("data.json", "w") as f:
    json.dump(data, f)

# Lecture
with open("data.json", "r") as f:
    data = json.load(f)
    print(data)
```

## 4. Exercices pratiques

### Exercice 1 : Système de gestion d'étudiants

1. Créez un système qui :
   - Gère les étudiants (nom, prénom, notes)
   - Calcule les moyennes
   - Sauvegarde les données dans un fichier
   - Permet de charger les données

### Exercice 2 : Jeu de cartes

1. Développez un jeu de cartes avec :
   - Une classe Carte
   - Une classe Jeu
   - Des méthodes pour mélanger et distribuer
   - Un système de points

### Exercice 3 : Gestionnaire de tâches

1. Créez une application qui :
   - Gère des tâches avec priorité
   - Permet d'ajouter/supprimer des tâches
   - Sauvegarde l'état dans un fichier
   - Affiche les tâches par priorité

## Ressources supplémentaires

- [Documentation Python - Classes](https://docs.python.org/fr/3/tutorial/classes.html)
- [Documentation Python - Modules](https://docs.python.org/fr/3/tutorial/modules.html)
- [W3Schools - Python Classes](https://www.w3schools.com/python/python_classes.asp) 