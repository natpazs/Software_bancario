class Cliente:

    def __init__(self, nome, email, cpf, saldo):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.saldo = saldo
        self.clientes = {}

    def getClientes(self):
        return self.clientes

    def cadastrarCliente(self, nome, email, cpf, senha):
        self.clientes[cpf] = {'Nome': nome, 'Email': email, 'Senha': senha}

    def login(self, cpf, senha):
        if cpf in self.clientes:
            if self.clientes[cpf]['Senha'] == senha:
                return "Login feito com sucesso"
        else:
            return "Senha ou usuário incorreto"

    def listarClientes(self):
        for chave, valor in self.getClientes().items():
            print(f"Nome: {valor[0]}, Email: {valor[1]}, CPF{chave}")
        
    def saque(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Valor sacado com sucesso! O seu saldo agora é de R${self.saldo}")
        else:
            print("Saldo insuficiente para o saque.")

    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
            print(f"Valor depositado realizado com sucesso! O seu saldo agora é de R${self.saldo}")
        else:
            print("Não é possível depositar esse valor.")

    def transferencia(self, valor, destinatario):
        if valor <= self.saldo:
            self.saldo -= valor
            destinatario.saldo += valor 
            print(f"Valor transferido com sucesso para {destinatario.nome}! Seu saldo agora é de {self.saldo}")
        else:
            print("Valor insuficiente para transferência.")