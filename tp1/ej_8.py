def superposicion(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
            break
    return False


lista1 = [1, 2, 3, 4]
lista2 = [4, 5, 6, 7]
lista3 = [8, 9]
assert superposicion(lista1, lista2) == True
assert superposicion(lista1, lista3) == False
