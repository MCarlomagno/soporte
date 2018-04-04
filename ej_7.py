def inversa(cad):
    long = 0
    for i in cad:
        long = long + 1
    if long <= 1:
        return cad
    return inversa(cad[1:]) + cad[0]


def es_palindromo(texto):
    if texto == inversa(texto):
        return True
    else:
        return False


cadena1 = "radar"
cadena2 = "otro texto"
assert es_palindromo(cadena1) == True
assert es_palindromo(cadena2) == False
