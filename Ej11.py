def divide(x, y):
    assert (y != 0)
    return x/y

try:
    print(divide(4, 0))
except TypeError:
    print("Tipo de dato incorrecto")
except AssertionError:
    print("No se puede dividir por  cero!")
except NameError:
    print("No sabemos qué es lo que estás queriendo dividir")
