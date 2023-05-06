from conta import Conta
class contaEspecial(Conta):
    
    def __init__(self, clientes, saldo=1000, tipo="C", limite=200):
        super().__init__(clientes, saldo, tipo)
        self.limite = limite
        
    def saque (self, valor):
        if valor <= (self.saldo + self.limite):
            self.__saldo -= valor
            print('Saque bem sucedido')
            print('Seu saldo é {}'.format(self.__saldo))
            