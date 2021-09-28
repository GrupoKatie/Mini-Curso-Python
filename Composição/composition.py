class Conta:
    def __init__(self, numero, cliente, saldo):
        self.numero = numero
        self.saldo = saldo
        self.limite = limite
        self.historico = Historico()
    
    def transfere(self, destino, valor):
        print(f"Transferindo R${valor} para {destino}")

class Historico:
    def __init__(self):
        self.transacoes = []
        self.dataAbertura = datetime.datetime.today()
    
    def imprime(self):
        print(f"data de abertura: {self.dataAbertura}")
        print("Transações: ")

        for transacao in self.transacoes:
            print(transacao)
