class Banco:
    def __init__(self, nome, endereco, cnpj,):
        self.nome = nome
        self.endereco = endereco
        self.cnpj = cnpj
        self.clientes = []

    def getCliente(self, cpf, senha):
         for cliente in self.clientes:
            if cliente.cpf == cpf and cliente.senha == senha:
                return cliente

    def cadastrarCliente(self, nome, email, cpf, senha, saldo):
        clientee = Cliente(nome, email, cpf, senha, saldo)
        self.clientes.append(clientee)

    def login(self, cpf, senha):
        for cliente in self.clientes:
            if cliente.cpf == cpf and cliente.senha == senha:
                return "Login feito com sucesso"

class Cliente:

    def __init__(self, nome, email, cpf, senha, saldo):
        self.nome = nome
        self.email = email
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo
        
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


banco = Banco("Banco","Av.Qualquer, Jundiaí, nº123", 12345678901234)