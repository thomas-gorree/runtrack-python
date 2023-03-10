def triangle (a, b, c):
    if a+ b > c and a + c > b and b + c > a:
        print("cecie est un triangle.")
    if a == b and b == c:
        print("le triangle est équi.")
    elif a == b or b == c or a == c:
        #ont vérif que le triangle est iso
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 :
            print ("le triangle est iso et rectangle")
        else:
            print('triangle isocèle.')
    elif a== a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2 :
        # théoreme de pythagore
        print("letriangle est rectangle.")
    else:
        print("le triangle est quelconque")

triangle(6, 2, 6)
