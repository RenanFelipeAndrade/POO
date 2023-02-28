# 1. Nós usamos o modificador de acesso private a fim de: d) B e C estão corretas


print("\nUsuario")


class Usuario:
    __primeiroNome = ""
    ultimoNome = ""

    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def getPrimeiroNome(self):
        return f"O primeiro nome é: {self.__primeiroNome}"

    def hello(self):
        return f"Olá {self.primeiroNome.capitalize()}"


usuario1 = Usuario()
usuario1.setPrimeiroNome("Joe")
print(usuario1.getPrimeiroNome())


print("\nEmpregado")


class Empregado:
    nome = ""
    __salario = ""
    projeto = ""

    def setSalario(self, salario):
        self.__salario = salario

    def getSalario(self):
        return self.__salario

    def mostrar(self):
        return f"Nome: {self.nome}\nSalário: {self.__salario}"

    def trabalho(self):
        return self.nome


empregado1 = Empregado()
empregado1.nome = "Joe"
empregado1.setSalario(10)
print(empregado1.mostrar())


print("\nRobo")


class Robo:
    __nome = ""
    __ano_construcao = ""

    def getNome(self):
        return self.__nome

    def getAnoConstrucao(self):
        return self.__ano_construcao

    def setNome(self, nome):
        self.__nome = nome

    def setAnoConstrucao(self, ano_contrucao):
        self.__ano_construcao = ano_contrucao

    def diga_alo(self):
        return f"Nome: {self.__nome}\nAno construção: {self.__ano_construcao}"


robo1 = Robo()
robo1.setAnoConstrucao(1954)
robo1.setNome("Unimate")

print(robo1.diga_alo())


print("\nLaptop")


class Laptop:
    __preco = ""

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco


laptop1 = Laptop()
print(laptop1.get_preco())
laptop1.set_preco(3999)

print("\nPessoa")


class Pessoa:
    __primeiroNome = ""
    __ultimoNome = ""

    def getPrimeiroNome(self):
        return self.__primeiroNome

    def getUltimoNome(self):
        return self.__ultimoNome

    def setPrimeiroNome(self, primeiroNome):
        self.__primeiroNome = primeiroNome

    def setUltimoNome(self, ultimoNome):
        self.__ultimoNome = ultimoNome


pessoa1 = Pessoa()
pessoa1.setPrimeiroNome("João")
pessoa1.setUltimoNome("Carvalho")

print(pessoa1.getPrimeiroNome())
print(pessoa1.getUltimoNome())
