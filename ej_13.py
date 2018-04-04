def es_primo(n):
    for i in range(2, n):
        for j in range(2, n):
            if i*j == n:
                return False
    return True


assert es_primo(7) == True
assert es_primo(6) == False
