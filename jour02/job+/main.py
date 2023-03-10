def taille_nombre(x):
    if x >= 10: 
        return "cest un nombre"
    elif x <= 10 and x >= 0 : 
        return "cest un chiffre"
    else:
        return 'il y a une erreur avec le nombre'

print(taille_nombre(-10))