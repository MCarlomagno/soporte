palabras = ["aaaa","aa","aaaaaa"]

def mas_larga(palabras):
    larga = ""
    for p in palabras:
        if len(p) >= len(larga):
            larga = p
    return larga 

print(mas_larga(palabras))