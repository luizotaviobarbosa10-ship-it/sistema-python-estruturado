from usuario import Usuario
from sistema import Sistema

sistema = Sistema()

while True:
    print("\n1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Sair")
    opc = input("Escolha: ")

    if opc == "1":
        nome = input("Nome: ")
        sistema.cadastrar(Usuario(nome))

    elif opc == "2":
        sistema.listar()

    else:
        break
