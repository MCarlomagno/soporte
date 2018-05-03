class Rectangulo:
    base = 8
    altura = 2

    def area(self):
        return self.base * self.altura


r = Rectangulo()
assert r.area() == 16
