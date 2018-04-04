def sumatoria(n):
    acum = 0
    cont = 1
    while True:
        if cont <= n:
            acum = acum + cont
            cont = cont + 1
        else:
            break
    return acum

print("Ingrese un número.")
nro = int(input())
print (sumatoria(nro))
assert sumatoria(4) == 10
