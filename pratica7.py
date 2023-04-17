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
    def __init__(self, nome, email, salario, codigo=None) -> None:
        self.__codigo = codigo
        self.__nome = nome
        self.__email = email
        self.__salario = salario

    def get_salario(self):
        return self.__salario

    def aumenta_salario(self, percentual):
        self.__salario += self.__salario * (percentual / 100)
        return self.__salario


class Chefe(Empregado):
    def __init__(self, nome, email, salario, beneficio, codigo=None) -> None:
        super().__init__(nome, email, salario, codigo=codigo)
        self.__beneficio = beneficio

    def aumenta_salario(self, percentual):
        salario = self.get_salario()
        acrescimo = (self.__beneficio / salario) * 100 + percentual
        salario_atual = super().aumenta_salario(acrescimo)
        return salario_atual


class Estagiario(Empregado):
    def __init__(self, nome, email, salario, desconto, codigo=None) -> None:
        super().__init__(nome, email, salario, codigo)
        self.__desconto = desconto

    def aumenta_salario(self, percentual):
        salario = self.get_salario()
        acrescimo = percentual - (self.__desconto / salario) * 100
        salario_atual = super().aumenta_salario(acrescimo)
        return salario_atual


class Ingresso:
    def __init__(self, valor) -> None:
        self.__valor = valor

    def imprime_valor(self):
        return self.__valor


class VIP(Ingresso):
    def __init__(self, valor) -> None:
        valor *= 1.10
        super().__init__(valor)

    def imprime_valor(self):
        return super().imprime_valor()


class Normal(Ingresso):
    def __init__(self, valor) -> None:
        super().__init__(valor)

    def categoria(self):
        print(self.categoria)


class CamaroteInferior(VIP):
    def __init__(self, valor, localizacao) -> None:
        super().__init__(valor)
        self.__localizacao = localizacao

    def get_localizacao(self):
        return self.__localizacao

    def show_localizacao(self):
        print(self.__localizacao)


class CamaroteSuperior(VIP):
    def __init__(self, valor, localizacao) -> None:
        valor *= 1.10
        super().__init__(valor)
        self.__localizacao = localizacao

    def get_localizacao(self):
        return self.__localizacao

    def show_localizacao(self):
        print(self.__localizacao)


class Funcionario:
    def __init__(self, nome, endereco, telefone, email) -> None:
        self.__nome = nome
        self.__endereco = endereco
        self.__telefone = telefone
        self.__email = email

    def exibe_dados(self):
        print(
            f"Nome: {self.__nome}\nEmail: {self.__email}\nEndereco: {self.__endereco}\nTelefone: {self.__telefone}"
        )

    def retorna_dados(self):
        return (self.__nome, self.__email, self.__endereco, self.__telefone)


class Assistente(Funcionario):
    def __init__(self, nome, endereco, telefone, email, matricula, salario) -> None:
        super().__init__(nome, endereco, telefone, email)
        self.__matricula = matricula
        self.__salario = salario

    def get_matricula(self):
        return self.__matricula


class Tecnico(Assistente):
    def __init__(
        self, nome, endereco, telefone, email, matricula, salario, bonus
    ) -> None:
        super().__init__(
            nome, endereco, telefone, email, matricula, salario=salario + bonus
        )

    def exibe_dados(self):
        nome, _ = self.retorna_dados()
        matricula = self.get_matricula()
        print(f"Matrícula: {matricula}\nNome: {nome}")


class Administrativo(Assistente):
    def __init__(
        self, nome, endereco, telefone, email, matricula, turno, salario
    ) -> None:
        self.__turno = turno
        if turno == "noite":
            salario *= 1.1
        super().__init__(nome, endereco, telefone, email, matricula, salario)

    def exibe_dados(self):
        nome, _ = self.retorna_dados()
        matricula = self.get_matricula()
        print(f"Matrícula: {matricula}\nNome: {nome}")


class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.__idade = idade


class Rica(Pessoa):
    def __init__(self, nome, idade, dinheiro) -> None:
        super().__init__(nome, idade)
        self.__dinheiro = dinheiro

    def faz_compras(self):
        self.__dinheiro /= 2


class Pobre(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)

    def trabalha(self):
        print("Trabalhando...")


class Mendigo(Pessoa):
    def __init__(self, nome, idade) -> None:
        super().__init__(nome, idade)

    def mendiga(self):
        print("Mendiga...")


pobre = Pobre("Renato", "34")
pobre.trabalha()
rica = Rica("Vanessa", 40, 1_000_000)
rica.faz_compras()
