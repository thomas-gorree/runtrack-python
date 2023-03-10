# def my_len(phrase):
#     count = 0
#     for i in phrase:
#         count += 1
#     return count

# def find_long_words(n, phrase):
#     current_word = ""
#     long_words = []
#     long_word2 = ""
#     for i in range(my_len(phrase)):
#         if phrase[i] != " ":
#             current_word += phrase[i]
#         else:
#             if my_len(current_word) > n:
#                 long_words += [current_word]
#             current_word = " "
#     for i in range(my_len(current_word)):
#         long_word2 += long_words[i]
#     return long_word2

# print(find_long_words(3, "La peur est le chemin vers le côté obscur la peur mène à la colère lacolère mène à la haine la haine mène à la souffrance"))


# def mots_plus_longs(chaine, n): # ma fonction
#     #mon mots vas etre ma liste .split()
#     mots = chaine.split() # split() =séparer la chaîne en mots individuels
    
#     mots_long = []
#     for mot in mots:
#         #mon mot vas me servire a vérif si le premier mot vas etre bon

#         if len(mot) > n: # si le mot est plus petit que n il sera pas retnue sur le append
            
#             mots_long.append(mot) # ajouter le mot à la liste si sa longueur est supérieure à n
    
#     return mots_long # ma boucle recommence

# # Exemple d'utilisation
# chaine = "La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"
# n = 3

# mots_long = mots_plus_longs(chaine, n)

# print(mots_long) # ['peur', 'chemin', 'vers', 'côté', 'obscur', 'peur', 'mène', 'colère', 'colère', 'mène', 'haine', 'haine', 'mène', 'souffrance']



def my_len(phrase):
    
    count = 0 # La variable count est initialisée à zéro

    #i= a la premier charaquetére 1 elment pour une liste et 1 lettre pour un mot et ensuite il passe au prochain

    for i in phrase: #La boucle for parcourt chaque caractère de phrase un à un, en commençant par le premier
        
        count += 1#À chaque itération, la variable count est incrémentée de 1
    
    return count #Après la fin de la boucle, la fonction retourne la valeur de count, 
#qui représente le nombre total de caractères dans la chaîne phrase


def ajout(liste, x): # ses la def de append
    
    liste += [x] # sa dit que j'ajoute x a la liste
    
    return list


def separation(str): #ses une def de split()
    
    phrase = []# La variable phrase est initialisée à une liste vide.

    mot = "" #La variable mot est initialisée à une chaîne vide

    for i in str:# La boucle for parcourt chaque caractère de la chaîne str un à un, en commençant par le premier

        if i != " ": #Si le caractère 'i' n'est pas un espace, alors il est ajouté à la chaîne "mot"
            
            mot += i #Si le caractère i est un espace, alors la chaîne mot est ajoutée à la liste phrase 
        
        else:
            
            ajout(phrase,mot) # en appelant une fonction ajout() 
           
            mot = ""
    
    return phrase #  puis la variable mot est réinitialisée à une chaîne vide

def my_long_word(n,str):
    mots = separation(str)
    phrase = ""
    for i in mots:
        if my_len(i) > n:
            phrase += i
            phrase += " "
    return phrase

print(my_long_word(3," La peur est le chemin vers le côté obscur la peur mène à la colère la colère mène à la haine la haine mène à la souffrance"))





