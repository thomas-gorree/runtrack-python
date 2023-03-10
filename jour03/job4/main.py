def gethollo():
    num = 1
    while num < 100:
        if (num % 3 == 0 and num % 5 == 0):
            print('buzzfizz')
        elif (num % 5  == 0):
            print('buzz')
        elif (num % 3 == 0):
            print('fizz')
        else:
            print(num)
        num += 1
        


gethollo()