# chaine = "nikana"
# inverse = chaine[::-1]
# print(inverse)
# def inv(str):
#     for i in range (len(str)-1, -1, -1)
# chaine = "nikana"
# inverse = ""
# i = len(chaine) - 1
# while i >= 0:
#     inverse += chaine[i]
#     i -= 1
# print(inverse)
chaine = "abcdefghijklmnopqrstuvwxyz" * 10
taille = len(chaine)
n = 1
while n <= taille:
    print(chaine[:n])
    n += 2