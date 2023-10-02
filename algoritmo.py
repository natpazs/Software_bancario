from classe import *
import os



def main():
    a = True
    while a == 1:
        try:
            print("Bem vindo ao Banco")
            print("--- MENU ---")
            print("01 - Cadastrar Cliente")
            print("02 - Login")
            print("03 - Sair")

            menu = int(input("Qual opção você deseja? \n -"))
            os.system("pause")
            os.system("cls")


            match menu:
                case 1:
                    nome = input("Informe seu nome:")
                    email = input("Informe seu email:")
                    cpf =  int(input("Informe seu cpf:"))
                    saldo = int(input("Informe seu saldo:"))
                    senha = input("Informe sua senha:")
                    cliente = Cliente(nome, email, cpf, senha, saldo)
                    banco.cadastrarCliente(nome,email,cpf,senha, saldo)
                    os.system("pause")
                    os.system("cls")

                case 2:
                    login = banco.login(int(input("Informe seu cpf: ")), input("Informe sua senha: "))
                    print(login)
                    os.system("pause")
                    os.system("cls")

                    match login:

                        case "Login feito com sucesso":
                            print("01 - Sacar")
                            print("02 - Depositar")
                            print("03 - Transferir")
                            print("04 - Voltar")
                            print("05 - Sair")
                            menu2 = int(input("Qual opção você deseja \n - "))
                            os.system("pause")
                            os.system("cls")
                            
                            match menu2:
                                case 1:
                                    valor = float(input("Informe o valor a ser sacado: "))
                                    cliente.saque(valor)
                                    os.system("pause")
                                    os.system("cls")
                                case 2:
                                    valor = float(input("Informe o valor a ser depositado: "))
                                    cliente.deposito(valor)
                                    os.system("pause")
                                    os.system("cls")
                                case 3:
                                    valor = float(input("Informe o valor a ser transferido: "))
                                    destinatario = input("Informe o destinatário da transferência: ")
                                    cliente.transferencia(valor, destinatario)
                                    os.system("pause")
                                    os.system("cls")
                                case 4:
                                    os.system("cls")
                                case 5:
                                    break
                        case _:
                            print("Valor invalido")

                            os.system("pause")
                case 3:
                    break
                case _:
                    print("Valor invalido")
        
        except Exception as erro:
            print("Valor invalido")
            print(erro.__class__.__name__)