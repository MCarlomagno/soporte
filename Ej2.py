import math


class Circulo:
    radio = 10

    def area(self):
        return math.pi * self.radio * self.radio

    def perimetro(self):
        return 2 * math.pi * self.radio


c = Circulo()
assert (c.area() == 314.1592653589793)
assert (c.perimetro() == 62.83185307179586)
