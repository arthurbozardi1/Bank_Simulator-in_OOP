class Conta:
    def __init__(self, clientes, saldo=0, numero="", tipo="C", ativo= True):
        self.__saldo = saldo
        self.clientes = clientes
        self.numero = numero
        self.tipo = tipo
        self.operacoes = []
        self.gera_numero()
        self.ativo = ativo
        
    def gera_numero(self):
        from random import sample
        list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8 ,9]
        
        numbers = sample(list1, 7)
        self.numero = "".join(str(x) for x in numbers)

    def resumo(self):
        print("Resumo da conta:")
        for clientes in self.clientes:
            print("Cliente: {}".format(clientes.nome))
        print("Número da conta: {}".format(self.numero))
        print("Saldo: R${}".format(self.__saldo))
        print("-" * 30)
        
    def saque(self, valor):
        if self.ativo == True:
            print("Saque:")
            if valor <= self.__saldo:
                self.__saldo -= valor
                self.operacoes.append(["saque", valor])
                print("Parabéns! Saque realizado com sucesso")
                print("Seu saldo atual é: R${}".format(self.__saldo))
            else:
                print("Sem saldo suficiente!")
        print("-" * 30)
        
    def deposito(self, valor):
        if self.ativo == True:
            print("Depósito:")
            self.__saldo = self.__saldo + valor
            self.operacoes.append(['deposito', valor])
            print("O saldo atual é de R${}".format(self.__saldo))
            print("-" * 30)
        
    def extrato (self):
        print("Extrato:")    
        print(self.operacoes)
        print("-" * 30)  
    
    def fecha_conta(self):
        self.ativo = False