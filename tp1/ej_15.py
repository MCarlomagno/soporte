def program():
    lista = []
    while True:
        print("Ingrese un número. Ingrese 'fin' para salir.")
        obj = (input())
        if obj == "fin":
            break
        else:
            lista.append(obj)
    print(("Máximo:"))
    print(max(lista))
    print(("Mínimo:"))
    print(min(lista))

program()
