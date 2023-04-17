from math import pi


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        return f"Nome: {self.nome}\nIdade: {self.idade}"

    def __str__(self) -> str:
        return self.mostrar_info()


class Aluno(Pessoa):
    def __init__(self, nome, idade, nota) -> None:
        super().__init__(nome, idade)
        self.nota = nota

    def mostrar_info(self):
        info_pessoa = super().mostrar_info()
        info_pessoa += f"\nNota: {self.nota}"
        return info_pessoa

    def __str__(self) -> str:
        return self.mostrar_info()


aluno1 = Aluno("Renan", 20, 10)
print(aluno1)


class Veiculo:
    def __init__(self, marca, modelo, ano) -> None:
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def mostrar_info(self):
        return f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}"


class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, qtd_portas) -> None:
        super().__init__(marca, modelo, ano)
        self.qtd_portas = qtd_portas

    def mostrar_info(self):
        info_veiculo = super().mostrar_info()
        info_veiculo += f"\nQuantidade de portas: {self.qtd_portas}"
        return info_veiculo


class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas) -> None:
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def mostrar_info(self):
        info_veiculo = super().mostrar_info()
        info_veiculo += f"\nCilindradas: {self.cilindradas}"
        return info_veiculo

    def __str__(self) -> str:
        return self.mostrar_info()


print(Moto("Honda", "CG", 2007, 125))


class Animal:
    def __init__(self, nome, peso) -> None:
        self.nome = nome
        self.peso = peso

    def comer(self):
        self.peso += 1


class Cachorro(Animal):
    def __init__(self, nome, peso) -> None:
        super().__init__(nome, peso)

    def latir(self):
        return "AU!"


class Gato(Animal):
    def __init__(self, nome, peso) -> None:
        super().__init__(nome, peso)

    def miar(self):
        return "miau"


class Funcionario(Pessoa):
    def __init__(self, nome, idade, salario) -> None:
        super().__init__(nome, idade)
        self.salario = salario

    def aumenta_salario(self, porcentagem):
        self.salario += self.salario * porcentagem / 100
        return self.salario


functionario1 = Funcionario("Renan", 20, 1000)
print(functionario1.aumenta_salario(10))


class Forma:
    def area(self, comprimento, altura):
        return comprimento * altura


class Retangulo(Forma):
    def __init__(self, comprimento, altura) -> None:
        self.comprimento = comprimento
        self.altura = altura

    def area(self):
        return super().area(self.comprimento, self.altura)


class Circulo(Forma):
    def __init__(self, raio) -> None:
        self.raio = raio

    def area(self):
        return self.raio**2 * pi


circulo = Circulo(2)
print(circulo.area())
retangulo = Retangulo(2, 3)
print(retangulo.area())


class ContaCorrente:
    def __init__(self, numero, saldo, cliente) -> None:
        self.__numero = numero
        self.__saldo = saldo
        self.__cliente = cliente

    def creditar(self, valor):
        self.saldo += valor

    def debitar(self, valor):
        self.saldo -= valor

    def get_saldo(self):
        return self.__saldo


class ContaEspecial(ContaCorrente):
    def __init__(self, numero, saldo, cliente, limite) -> None:
        super().__init__(numero, saldo, cliente)
        self.__limite = limite

    def debitar(self, valor):
        super().debitar(valor)
        return self.get_saldo()


class ContaPoupanca(ContaCorrente):
    def __init__(self, numero, saldo, cliente, saldo_minimo) -> None:
        super().__init__(numero, saldo, cliente)
        self.__saldo_minimo = saldo_minimo

    def debitar(self, valor):
        super().debitar(valor)
        return self.get_saldo()

    def atualizar_saldo(self):
        return self.get_saldo()

    def get_saldo_minimo(self):
        return self.__saldo_minimo


class ContaInvestimento(ContaCorrente):
    def __init__(self, numero, saldo, cliente, dia_investimento, periodo) -> None:
        super().__init__(numero, saldo, cliente)
        self.__dia_investimento = dia_investimento
        self.__periodo = periodo

    def atualizar_saldo(self, saldo):
        self.__saldo = saldo
        return self.__saldo


class Empregado:
    def __init__(self, codigo, nome, email, salario) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumenta_salario(self, percentual):
        self.__salario *= percentual / 100
        return self.__salario


class Chefe:
    pass
