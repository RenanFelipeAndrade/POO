from random import shuffle
from typing import List, Union
from math import pi
from random import randint


class Animal:
    def falar(self):
        print("Eu sou um animal")


class Cachorro(Animal):
    def falar(self):
        print("au")


class Gato(Animal):
    def falar(self):
        print("miau")


class Peixe(Animal):
    def falar(self):
        print("...")


animal = Animal()
cachorro = Cachorro()
gato = Gato()
peixe = Peixe()

animal.falar()
cachorro.falar()
gato.falar()
peixe.falar()


def ex2():
    lista_gatos: List[Gato] = [Gato() for _ in range(3)]
    lista_cachorros: List[Cachorro] = [Cachorro() for _ in range(3)]
    lista_peixes: List[Peixe] = [Peixe() for _ in range(3)]
    lista_animais: List[Animal] = [Animal() for _ in range(3)]
    lista_bicho: List[Union[Animal, Gato, Cachorro, Peixe]] = [
        *lista_gatos,
        *lista_cachorros,
        *lista_peixes,
        *lista_animais,
    ]
    shuffle(lista_bicho)

    for bicho in lista_bicho:
        bicho.falar()


class Carro:
    def digirir(self):
        print("Dirigindo ...")


class CarroGasolina(Carro):
    def digirir(self):
        print("Dirigindo a gasolina...")


class CarroEletrico(Carro):
    def digirir(self):
        print("Dirigindo a bateria...")

class Forma:
    def area(self, largura=0, altura=0):
        return largura * altura

class Quadrado(Forma):
    def area(self, lado):
        return lado * lado

class Circulo(Forma):
    def area(self, raio):
        return raio * 2 * pi


def ex4():
    lista_quadrado: List[Quadrado] = [Quadrado() for _ in range(3)]
    lista_circulo: List[Circulo] = [Circulo() for _ in range(3)]
    lista_forma: List[Forma] = [Forma() for _ in range(3)]
    lista_figuras: List[Union[Forma, Circulo, Quadrado]] = [
        *lista_forma,
        *lista_circulo,
        *lista_quadrado,
    ]
    shuffle(lista_figuras)

    for figura in lista_figuras:
        if type(figura) == Forma:
            print(figura.area(randint(1,10), randint(1,10)))
        else:
            print(figura.area(randint(1,10)))


class Empregado:
    def pagar_salario(self):
        return "Salário pago"
        
class EmpregadoHora(Empregado):
    def pagar_salario(self):
        horas_trabalhadas = randint(4,16)
        valor_hora = 20
        return horas_trabalhadas * valor_hora

class EmpregadoMes(Empregado):
    def pagar_salario(self):
        return randint(1100, 2100)

def ex5():
    lista_empregado: List[Empregado] = [Empregado() for _ in range(3)]
    lista_empregado_hora: List[EmpregadoHora] = [EmpregadoHora() for _ in range(3)]
    lista_empregado_mes: List[EmpregadoMes] = [EmpregadoMes() for _ in range(3)]
    lista_funcionarios: List[Union[EmpregadoMes, EmpregadoHora, Empregado]] = [
        *lista_empregado_mes,
        *lista_empregado_hora,
        *lista_empregado,
    ]
    shuffle(lista_funcionarios)

    for funcionario in lista_funcionarios:
        print(funcionario.pagar_salario())

class ContaBancaria:
    saldo = 0
    def deposito(self, valor):
        self.saldo += valor

    def retirada(self, valor):
        if self.saldo-valor<=0:
            return self.saldo
        self.saldo -= valor
        return valor

class ContaPoupanca(ContaBancaria):
    def deposito(self, valor):
        self.saldo += valor * 1.2

class ContaCorrente(ContaBancaria):
    def deposito(self, valor):
        self.saldo += valor * 1.1
