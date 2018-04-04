def maxi(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


assert maxi(1, 2) == 2
assert maxi(2, 3) != 2
assert maxi(3, 4) != 2
