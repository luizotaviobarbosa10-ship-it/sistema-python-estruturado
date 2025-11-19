class Sistema:
    def __init__(self):
        self.usuarios = []

    def cadastrar(self, usuario):
        self.usuarios.append(usuario)
        print("Usuário cadastrado!")

    def listar(self):
        print("\n--- Usuários ---")
        for u in self.usuarios:
            print("- ", u.nome)
