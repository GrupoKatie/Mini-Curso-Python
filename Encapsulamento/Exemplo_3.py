
    @property
    def	nome_diferente(self):
        return	self._nome_diferente

	@nome_diferente.setter
    def	nome_diferente(self,	saldo):
        if(saldo	<	0):
            print("O Saldo não pode ser negativo")
        else:
            self._nome_diferente	=	saldo