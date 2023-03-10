list = [1, 2, 3, 4, 5]
def echanger_le_premier_et_le_dernier(list):
        if len(list) >= 2:
                list[0], list[-1]= list[-1], list[0]
        return list

print(echanger_le_premier_et_le_dernier(list))
