# 1 c) É a personificação de um objeto da vida real.
# 2 a) Um objeto nos dá a capacidade de trabalhar com a classe e ter várias instâncias desta mesma classe.
# 3 b) Uma variável dentro de uma classe.
# 4 a) Uma função dentro de uma classe.
# 5 Nome: Usuario; Propriedades: Nome e sobrenome; Método: hello


class Usuario:
    nome = ""
    sobrenome = ""

    def hello(self):
        return f"Olá {self.nome.capitalize()} {self.sobrenome.capitalize()}"


usuario1 = Usuario()
usuario1.nome, usuario1.sobrenome = "Renan", "Andrade"
print(f"Nome: {usuario1.nome}\nSobrenome: {usuario1.sobrenome}")
print(usuario1.hello())
print("\n")

usuario2 = Usuario()
usuario2.nome, usuario2.sobrenome = "Jane", "Silva"
print(usuario2.hello())
