def calc_leng(cad):
    i = 0
    for char in cad:
        i = i + 1
    return i


cade = "A ver si entendí."
assert calc_leng(cade) == 17
assert calc_leng(cade) != 18
assert calc_leng(cade) != 16
