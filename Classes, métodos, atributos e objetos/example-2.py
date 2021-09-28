class Cachorro:
    quantidade = 0
    cachorros = []

    def __init__(self, raca, idade):
        self.raca = raca
        self.idade = idade
    
    def late(self):
        print("Au au!")
    
    def mudaIdade(self):
        self.idade = self.idade + 1 #Incrementação

Toto = Cachorro("dálmata", 2)
print(Toto.idade) #2
Toto.mudaIdade()
print(Toto.idade) #3