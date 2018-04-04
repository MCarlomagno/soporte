def multip(lista):
    acum = 1
    for num in lista:
        acum = acum * num
    return acum


list = [1, 2, 3, 4]
assert multip(list) == 24
