class Cliente:
    def __init__(self, cpf="", nome="", telefone="", data_nascimento=""):
        self.nome = nome
        self.telefone = telefone
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        
    def imprime_dados_clientes(self):
        print("Nome: {}\nCPF: {}\nTelefone: {}\nData de Nascimento: {}".format(self.nome, self.cpf, self.telefone,self.data_nascimento))
        print("-" * 30)
        