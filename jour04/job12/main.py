def longeur(Liste):
    count = 0
    for i in Liste:
        count += 1
    return count


liste = [4, 5, 256545, 6, 10]

def tri_insertion(liste):
    for i in range(1, longeur(liste)):
        valeur = liste[i]
        j = i - 1
        while j >= 0 and liste[j] > valeur:
            liste[j+1] = liste[j]
            j -= 1
        liste[j+1] = valeur
    return liste


print(tri_insertion(liste))