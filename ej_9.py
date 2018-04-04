def generar_n_caracteres(entero, caracter):
    return caracter*entero


n = 5
car = "x"
assert generar_n_caracteres(n, car) == "xxxxx"
