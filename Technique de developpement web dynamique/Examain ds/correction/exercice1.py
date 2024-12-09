"""
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
"""


X = float(input("Entrez le premier nombre: "))
Y = float(input("Entrez le deuxième nombre: "))

somme = X + Y
produit = X * Y
puissance = X ** Y

print(X, " + ", Y, " = ", somme)
print(X, " * ", Y, " = ", produit)
print(X, " ** ", Y, " = ", puissance)
