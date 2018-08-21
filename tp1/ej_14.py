inicio = (0,0)
salida =(3,3)
lab = [[False,False,True,True],[True,False,True,True],[True,False,True,True],[True,False,False,False]]
recorridos = []
def buscar_salida(laberinto, inicio, salida, recorridos):
    i = inicio[0]
    j = inicio[1]

    if inicio == salida:
        return "solucionado"
    #considerando que se tienen 4 posibles movimientos
    #(adelante, atras, izquierda, derecha)
    if laberinto[i+1][j] == False and (i+1,j) not in recorridos and i<2:
        recorridos.append((i+1,j))
        buscar_salida(laberinto, (i+1,j), salida,recorridos)
    elif laberinto[i][j+1] == False and (i,j+1) not in recorridos and j<2:
        recorridos.append((i,j+1))
        buscar_salida(laberinto, (i,j+1), salida,recorridos)
    elif laberinto[i][j-1] == False and (i,j-1) not in recorridos and j>0:
        recorridos.append((i,j-1))
        buscar_salida(laberinto, (i,j-1), salida,recorridos)
    elif laberinto[i-1][j] == False and (i-1,j) not in recorridos and i>0:
        recorridos.append((i-1,j))
        buscar_salida(laberinto, (i-1,j), salida,recorridos)
    else:
        return "no hay mas movimientos"


resultado = buscar_salida(lab, inicio, salida, recorridos)

print(resultado)
