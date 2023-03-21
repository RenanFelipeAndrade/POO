class Usuario:
    __nome_usuario = None

    def altera_nome_usuario(self, nome_usuario):
        self.__nome_usuario = nome_usuario

    def pega_nome_usuario(self):
        return self.__nome_usuario


class Admin(Usuario):
    def escreva_nome(self):
        return "Admin"

    def diga_ola(self):
        return f"Olá {self.escreva_nome()} {self.pega_nome_usuario()}"


admin1 = Admin()
admin1.altera_nome_usuario("Baltazar")
# usando propriedade privada a classe filha não tem acesso à propriedade da mãe
# a não ser que haja um getter
print(admin1.diga_ola())
