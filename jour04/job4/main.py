def liste_fruits():
    fruits = ["pomme", "cerise", "orange", "melon"]
    fruits.insert(2, "Mangue")
    return fruits
fruits = liste_fruits()

print(fruits)