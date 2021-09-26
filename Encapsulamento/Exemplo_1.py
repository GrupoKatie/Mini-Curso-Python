class Conta:
    def	__init__(self,	saldo):
        self._saldo	=	saldo

    def	get_saldo(self):
        return	self._saldo

    def	set_saldo(self,	saldo):
        if(saldo < 0):
            print("O Saldo não pode ser negativo")
        else:
            self.saldo = saldo