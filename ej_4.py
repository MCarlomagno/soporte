def es_vocal(char):
    if char == "a" or char == "A"\
    or char == "e" or char == "E"\
    or char == "i" or char == "I"\
    or char == "o" or char == "O"\
    or char == "u" or char == "U":
        return True
    else:
        return False


assert es_vocal("a") == True
assert es_vocal("E") == True
assert es_vocal("i") == True
assert es_vocal("o") == True
assert es_vocal("u") == True
assert es_vocal("B") != True
assert es_vocal("b") == False
