class Cachorro:
    def __init__(self, raca):
        self.raca = raca
    def late(self):
        print("Au au!")

Toto = Cachorro("dálmata")

print(Toto.raca) #dálmata

Toto.late() #"Au Au!"
