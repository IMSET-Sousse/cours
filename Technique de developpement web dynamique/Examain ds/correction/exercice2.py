"""
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
"""

X = int(input("Entrez un nombre: "))

if X % 2 ==0:
    pair = "pair"
else:
    pair = "impair"

if X == 0:
    signe = "nul"
elif X > 0:
    signe = "positif"
else:
    signe = "negatif"

print(X, " est ", signe, " et ", pair)