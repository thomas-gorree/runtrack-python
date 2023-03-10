# crée un liste est son entier 
L = [1, 2, 3, 4, 5]

# afficher la valeur et son entier
print("Valeur de L[1]:", L[1])

# pui je définit la fonction pour la remplacer L[3]
def remplacer_L3(L):
    L[3] = L[2] + L[4]

# appller pour remplacer la fonction L[3]
remplacer_L3(L)

# Afficher la valeur du terme de la liste
print("Valeur du dernier terme de la liste:", L[-1])