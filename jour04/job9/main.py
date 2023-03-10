L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
max = L[0]
for i in range(1, len(L)):
    if L[i] > max:
        max = L[i]
print("Le maximum est :", max)

min = L[0]
for i in range(1, len(L)):
    if L[i] < min:
        min = L[i]
print("Le maximum est :", min)