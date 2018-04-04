def cant_digitos(nro):
    num = str(nro)
    long = 0
    for digit in num:
        long = long + 1
    return long


a = 5
b = 12
assert cant_digitos(a) == 1
assert cant_digitos(b) == 2
