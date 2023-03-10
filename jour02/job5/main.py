num1 = 15
num2 = 18
operateur = '*'

def calcule(num1, operateur, num2):
    result = 0
    if operateur == '*':
        result = num1 + num2
    return result

print(calcule(num1 ,operateur, num2))
