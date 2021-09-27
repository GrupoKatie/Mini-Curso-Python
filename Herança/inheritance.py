#aqui criamos nossa classe mãe
class SerVivo:
    def __init__(self): #este é o nosso construtor
        self.tipo = 'Ser Vivo'
        self.idade = 0
    
    #métodos da classe mãe
    def nascer(self, nome):
        self.nome = nome
        print(f'Eu sou do tipo {self.tipo}. Meu nome é {self.nome} e acabei de nascer!')
    
    def amadurecer(self):
        self.idade += 1
        print(f'Eu, {self.nome}, amadureci! Minha idade é {self.idade}.')


class Humano(SerVivo):
    def __init__(self):
        super().__init__()          #uso do super para instanciarmos um objeto da classe mãe
        self.tipo = 'Humano'
    
    #método da subclasse
    def sorrir(self):
        print('(: Eu sou humano e sei rir :)')


class Gato(SerVivo):
    def __init__(self):
        super().__init__() 
        self.tipo = 'Gato'
    
    #método da subclasse
    def miar(self):
        print('Miau! Sou um gatinho e sei miar (•ㅅ•)')


class Cachorro(SerVivo): #subclasse sem uso do super
    def __init__(self):
        self.tipo = 'Cachorro'


class GatoBranco(Gato): #subclasse da subclasse
    def __init__(self):
        super().__init__()
    
    def miar(self):
        print('Eu sou um gato branco e sou rei do mundo! ᶠᵉᵉᵈ ᵐᵉ /ᐠ-ⱉ-ᐟ\ﾉ')


humano = Humano()
humano.nascer('Wilson')

branco = GatoBranco()
branco.miar()