"""
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
"""

N = int(input("Entrez un nombre: "))

somme = 0
factorielle = 1
for i in range(1, N + 1):
    somme = somme + i
    factorielle = factorielle * i

print("La somme des nombres de 1 à ", N, " est ", somme)
print("La factorielle de ", N, " est ", factorielle)
