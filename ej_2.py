def max_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n2:
        return n1
    else:
        if n2 > n3:
            return n2
        else:
            return n3


assert max_de_tres(2, 3, 4) == 4
assert max_de_tres(5, 6, 7) != 6
