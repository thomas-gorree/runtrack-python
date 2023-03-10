ma_string = input(" entrez une chaine de charactères, je vais déterminer si elle contien la lettre m ")

i =0
comp =0

for i in range (len(ma_string)):
    if ma_string[i] == 'm' or 'M':
        comp = comp + 1
    i = i+ 1
print (" Votre chaine de charactères contient " + str(comp) + " fois la lettre m ou M. ")