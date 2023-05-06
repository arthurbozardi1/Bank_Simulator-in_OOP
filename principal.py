from cliente import Cliente
from banco import Banco
from conta import Conta
from ContaEspecial import contaEspecial

cliente_banco = Banco()

class Menu:
    def __init__(self):
        self.opcoes = [['sair',0]]
        
    def add_opcao(self, opcao, nmr_opcao):
        
        self.opcoes.append([opcao, nmr_opcao])
    
    def exibe(self):
        for x in self.opcoes:
            print (x)
        self.opcao_escolhida = int(input("Digite o número da opcao escolhida: "))
        
    def execute(self):
        while True:
             
            self.exibe()
    
            if self.opcao_escolhida == 0:#SAIR
                print('Você saiu!')
                break
        
            elif self.opcao_escolhida == 1: #CADASTRO CLIENTE
                cpf_novo = input('Digite o cpf: ')
                nome_novo = input('Digite o nome: ')
                telefone_novo = input('Digite o número de telefone: ')
                data_nascimento_novo = input('Digite sua data de nascimento: ')
                novo_cliente = Cliente(cpf = cpf_novo, nome = nome_novo, telefone = telefone_novo, data_nascimento = data_nascimento_novo)
            
            elif self.opcao_escolhida == 2: #ABRIR CONTA
                
                novo_saldo = input('Digite o saldo: ')
                cpf = input('Digite o cpf: ')
                for novo_cliente in cliente_banco.lista_clientes:
                    if cpf == novo_cliente.cpf:
                        novo_cliente.imprime_dados_cliente()
                    
                    else:
                        cpf_novo = input('Digite o cpf: ')
                        nome_novo = input('Digite o nome: ')
                        telefone_novo = input('Digite o número de telefone')
                        data_nascimento_novo = input('Digite sua data de nascimento')
                        novo_cliente = Cliente(cpf = cpf_novo, nome = nome_novo, telefone = telefone_novo, data_nascimento = data_nascimento_novo)
                cliente_banco.abre_conta([novo_cliente], novo_saldo)                
            
            elif self.opcao_escolhida == 3: #SAQUE
                numero_saque = input('Digite o numero da conta: ')
                valor_saque = input('Digite o valor de saque: ')
            
                for cnt in cliente_banco.lista_contas:
                    if numero_saque == cnt.numero:
                        sacar = Conta
                        valor_saque = float(input('Digite o valor que deseja sacar: '))
                        sacar.saque(valor_saque)
            
            elif self.opcao_escolhida == 4: #DEPÓSITO
                numero_deposito = input('Digite o número da conta: ')
                valor_deposito = input('Digite o valor de depósito: ')
                for cnt in cliente_banco.lista_contas:
                    if numero_deposito == cnt.numero:
                        deposito = Conta
                        valor_deposito = float(input('Digite o valor que deseja depositar: '))
                        deposito.deposito(valor_deposito)

                    else:
                        print('O número da conta não existe.')
            
            
            elif self.opcao_escolhida == 5: #EXTRATO**
                numero_extrato = input('Digite o numéro da conta: ')
                for cnt in cliente_banco.lista_contas:
                    if numero_extrato == cnt.numero:
                        ver_extrato = Conta
                        ver_extrato.extrato()
                        
                    else:
                        print('Conta não encontrada.')
                   
menu = Menu()

menu.add_opcao("Cadastro de cliente", 1)
menu.add_opcao("Abrir conta", 2)
menu.add_opcao("Saque", 3)
menu.add_opcao("Depósito", 4)
menu.add_opcao("Extrato", 5)
menu.execute()

