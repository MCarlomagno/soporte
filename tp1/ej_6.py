def inversa(cad):
    long = 0
    for i in cad:
        long = long + 1
    if long <= 1:
        return cad
    return inversa(cad[1:]) + cad[0]


cadena = "estoy probando"
assert inversa(cadena) == "odnaborp yotse"
