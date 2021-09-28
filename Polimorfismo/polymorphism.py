class Funcionario():
    def __init__(self, nome):
        self.nome = nome
    
    def Work():
        pass

class Gerente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Gerente"

    def Work():
        print("...Gerenciando")

class Atendente(Funcionario):
    def __init__(self, nome):
        super().__init__(nome)
        self.tipo = "Atendente"

    def Work():
        print("...Atendendo")

Mariana = Gerente("Mariana")
Rita = Atendente("Rita")

funcionarios = [Mariana, Rita]

for funcionario in funcionarios:
    print(funcionario.tipo) #Gerente #Atendente
    funcionario.Work() #...Gerenciando #...Atendendo
