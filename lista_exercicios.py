class Bola:
    def __init__(self, cor, circunferencia, material) -> None:
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def troca_cor(self, cor):
        self.cor = cor

    def mostra_cor(self):
        return self.cor


class Quadrado:
    def __init__(self, tamanho_lado) -> None:
        self.tamanho_lado = tamanho_lado

    def mudar_valor_lado(self, valor):
        self.tamanho_lado = valor

    def retornar_valor_lado(self):
        return self.tamanho_lado

    def calcular_area(self):
        return self.tamanho_lado**2


class Retangulo:
    def __init__(self, comprimento, altura) -> None:
        self.comprimento = comprimento
        self.altura = altura

    def mudar_valor_lado(self, comprimento, altura):
        self.comprimento = comprimento
        self.altura = altura

    def retornar_valor_lado(self):
        return self.comprimento, self.altura

    def calcular_area(self):
        return self.comprimento * self.altura

    def calcular_perimetro(self):
        return self.comprimento * 2 + self.altura * 2


def retangulo():
    """
    Programa para criação de retângulo através de inputs do usuário
    """
    comprimento = int(input("Insira o comprimento do retângulo: "))
    altura = int(input("Insira a altura do retângulo: "))
    retangulo = Retangulo(altura=altura, comprimento=comprimento)
    return f"A quantidade de pisos de 1m quadrado necessária é {retangulo.calcular_area()} e de rodapés {retangulo.calcular_perimetro()}"


class Pessoa:
    def __init__(self, nome, idade, peso, altura) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self):
        if self.idade < 21:
            self.altura = 0.5
        self.idade += 1
        return self.idade

    def engordar(self, kilos):
        self.peso += kilos
        return self.peso

    def emagrecer(self, kilos):
        self.peso -= kilos
        return self.peso

    def crescer(self, crescimento):
        self.altura += crescimento
        return self.altura


class ContaCorrente:
    def __init__(self, numero_conta, nome, saldo=0) -> None:
        self.numero_conta = numero_conta
        self.nome = nome
        self.saldo = saldo

    def alterar_nome(self, nome):
        self.nome = nome
        return nome

    def depositar(self, quantia):
        self.saldo += quantia
        return self.saldo

    def sacar(self, quantia):
        if self.saldo <= 0:
            return 0
        self.saldo -= quantia
        return quantia


class TV:
    # valores default arbitrários
    def __init__(self, numero_canal, volume) -> None:
        if numero_canal < 0:
            raise ValueError("O número do canal não pode ser negativo")

        self.numero_canal = numero_canal
        if volume < 0 or volume > 100:
            raise ValueError("O volume tem de estar entre 0 e 100")
        self.volume = volume

    def aumentar_volume(self, quantia=1):
        if self.volume + quantia >= 100:
            self.volume = 100
            return self.volume
        self.volume += quantia
        return self.volume

    def diminuir_volume(self, quantia=1):
        if self.volume - quantia <= 0:
            self.volume = 0
            return self.volume
        self.volume -= quantia
        return self.volume


class BichinhoVirtual:
    def __init__(self, nome, fome, saude, idade) -> None:
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def retornar_nome(self):
        return self.nome

    def retornar_fome(self):
        return self.fome

    def retornar_saude(self):
        return self.saude

    def retornar_idade(self):
        return self.idade

    @property
    def humor(self):
        return self.saude + self.fome


class Macaco:
    def __init__(self, nome, bucho=[]) -> None:
        self.nome = nome
        self.bucho = bucho

    def comer(self, alimento):
        self.bucho.append(alimento)
        return self.bucho

    def ver_bucho(self):
        return self.bucho

    def digerir(self):
        self.bucho = []
        return self.bucho


def macaco():
    macaco1 = Macaco("flemis", [])
    macaco1.comer("banana")
    macaco1.comer("maça")
    macaco1.comer("laranja")
    print(macaco1.ver_bucho())

    macaco2 = Macaco("nambo", ["tomate", "uva"])
    macaco1.comer(macaco2)
    print(macaco1.ver_bucho())


class Ponto:
    def __init__(self, x: int, y: int) -> None:
        self.x: int = x
        self.y: int = y

    def mostrar_valores(self):
        return self.x, self.y


class RetanguloCentro(Retangulo):
    def __init__(self, comprimento, altura) -> None:
        super()._init__(comprimento, altura)

    def centro_retangulo(self) -> Ponto:
        x = self.comprimento / 2
        y = self.altura / 2
        return Ponto(x, y)


def retagulo_centro_ponto(
    dimensoes,
):
    def novo_centro_retangulo():
        alterar_retangulo = input("Deseja alterar o retângulo?[S/n]: ").lower()

        if alterar_retangulo != "s" or alterar_retangulo != "n":
            print("\nFaça uma escolha válida!\n")
            return novo_centro_retangulo()

        if alterar_retangulo == "n":
            return
        retangulo_index = (
            int(input("Qual retângulo deseja alterar?[número]: ")) - 1
        )  # index estava 1 à frente

        if retangulo_index < 1 and retangulo_index > len(retangulos):
            print("\nFaça uma escolha válida!\n")
            return novo_centro_retangulo()

        altura = int(input(f"Insira a altura para o retângulo {retangulo_index+1}: "))
        comprimento = int(
            input(f"Insira o comprimento para o retângulo {retangulo_index+1}: ")
        )
        x, y = RetanguloCentro(comprimento, altura).centro_retangulo().mostrar_valores()
        print(f"Numero retangulo: {index+1}\nCentro: x={x}, y={y}\n")
        return novo_centro_retangulo()

    retangulos: list[RetanguloCentro] = []
    for altura_comprimento in dimensoes:
        retangulo = RetanguloCentro(
            altura=altura_comprimento["altura"],
            comprimento=altura_comprimento["comprimento"],
        )

        retangulos.append(retangulo)
    for index, retangulo in enumerate(retangulos):
        x, y = retangulo.centro_retangulo().mostrar_valores()
        print(f"Numero retangulo: {index+1}\nCentro: x={x}, y={y}\n")

    novo_centro_retangulo()


# retagulo_centro_ponto([{"altura": 10, "comprimento": 2}])


class BombaCobustivel:
    def __init__(self, tipo_combustivel, valor_litro, qtd_combustivel) -> None:
        self.tipo_combustivel = tipo_combustivel
        self.valor_litro = valor_litro
        self.qtd_combustivel = qtd_combustivel
        if not self.combustivel_valido():
            raise ValueError("Insira um modo válido: gasolina, alcool ou diesel")

    def combustivel_valido(tipo_combustivel):
        tipos_validos = ["gasolina", "alcool", "diesel"]
        if tipo_combustivel not in tipos_validos:
            return False
        return True

    def encher_tanque(self, quantia, tipo_combustivel):
        restante = self.qtd_combustivel - quantia
        if restante <= 0:
            custo = self.valor_litro * restante
            self.alterar_qtd_total_combustivel(0)
            return {
                "quantia_abastecida": restante,
                "tipo": tipo_combustivel,
                "custo": custo,
            }
        custo = self.valor_litro * quantia
        self.alterar_qtd_total_combustivel(restante)
        return {
            "quantia_abastecida": quantia,
            "tipo": tipo_combustivel,
            "custo": custo,
        }

    def abastecer(self, quantia, modo="litro"):
        if modo != "litro" or modo != "valor":
            raise ValueError("Insira um modo válido: valor ou litro")
        if modo == "litro":
            return self.encher_tanque(quantia, self.tipo_combustivel)
        if modo == "valor":
            litros = quantia / self.valor_litro
            return self.encher_tanque(litros, self.tipo_combustivel)

    def alternar_combustivel(self, tipo_combustivel):
        if not tipo_combustivel:
            raise ValueError("Insira um modo válido: gasolina, alcool ou diesel")
        self.tipo_combustivel = tipo_combustivel

    def alterar_qtd_total_combustivel(self, quantidade):
        if quantidade <= 0:
            raise ValueError("Insira uma quantidade atual maior que 0")
        self.qtd_combustivel = quantidade


class Carro:
    def __init__(self, consumo_combustivel) -> None:
        self.consumo_combustivel = consumo_combustivel
        self.qtd_combustivel = 0

    def andar(self, distancia):
        if distancia < 0:
            raise ValueError("Insira uma distância maior ou igual a zero")
        # consumo = distancia/litro
        distancia_maxima = self.qtd_combustivel * self.consumo_combustivel
        distancia_restante = distancia_maxima - distancia
        if distancia_restante < 0:
            # retira o excedente da distancia
            self.consumo_combustivel = 0

            return {
                "distancia_percorrida": distancia,
                "qtd_combustivel": self.qtd_combustivel,
            }

        self.qtd_combustivel -= distancia / self.consumo_combustivel

        return {
            "distancia_percorrida": distancia,
            "qtd_combustivel": self.qtd_combustivel,
        }

    def obter_gasolina(self):
        return self.qtd_combustivel

    def adicionar_gasolina(self, quantia):
        if quantia < 0:
            raise ValueError("Insira um valor maior ou igual a zero")
        self.qtd_combustivel = quantia


def carro():
    meuFusca = Carro(15)  # 15 quilômetros por litro de combustível.
    meuFusca.adicionar_gasolina(20)  # abastece com 20 litros de combustível.
    print(meuFusca.qtd_combustivel)
    meuFusca.andar(100)  # anda 100 quilômetros.
    print(meuFusca.qtd_combustivel)
    print(meuFusca.obter_gasolina())  # Imprime o combustível que resta no tanque.


class ContaInvestimento(ContaCorrente):
    def __init__(self, numero_conta, nome, taxa_juros, saldo=0) -> None:
        super().__init__(numero_conta, nome, saldo)
        self.taxa_juros = taxa_juros

    def adicione_juros(self):
        self.saldo *= 1 + self.taxa_juros / 100


def conta_investimento():
    conta = ContaInvestimento(10, "John", 10, 1000)
    print(conta.saldo)
    for _ in range(5):
        conta.adicione_juros()
    print(conta.saldo)


class Funcionario:
    def __init__(self, nome, salario) -> None:
        self.__nome = nome
        self.__salario = salario

    def obter_nome(self):
        return self.__nome

    def obter_salario(self):
        return self.__salario

    def aumenta_salario(self, percentual):
        self.__salario *= 1 + percentual / 100
