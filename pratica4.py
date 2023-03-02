class Usuario:
    def __init__(self, primeiroNome, ultimoNome) -> None:
        self.__primeiroNome = primeiroNome
        self.__ultimoNome = ultimoNome

    def getNomeCompleto(self):
        return f"{self.__primeiroNome} {self.__ultimoNome}"


usuario1 = Usuario("Johnny", "Bravo")
print(usuario1.getNomeCompleto())
