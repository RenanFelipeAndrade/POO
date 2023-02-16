# 1. c) A palavra-chave self


class Usuario:
    primeiroNome = ""
    ultimoNome = ""

    def hello(self):
        return f"Olá {self.primeiroNome.capitalize()}"


usuario1 = Usuario()
usuario1.primeiroNome, usuario1.ultimoNome = "Jonnie", "bravo"
print(usuario1.hello())
