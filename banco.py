from conta import Conta
class Banco: 
    def __init__(self, nome='', lista_contas=[], lista_clientes=[]):
        self.nome = nome
        self.lista_contas = lista_contas
        self.lista_clientes = lista_clientes
        
        
    def abre_conta(self, clientes, saldo):
        conta = Conta(clientes, saldo)
        conta.resumo()
        self.lista_contas.append(conta)
        for cliente in clientes:
            self.lista_clientes.append(cliente)
        
    def lista_contas(self):
        for conta in self.lista_contas:
            conta.resumo()
            