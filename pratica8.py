class Usuario:
    pontos = 0
    numero_de_artigos = 0

    def set_numero_artigos(self, nart: int):
        self.numero_de_artigos = nart

    def get_numero_artigos(self):
        return self.numero_de_artigos

    def calc_pontuacao(self):
        return 0


class Autor(Usuario):
    def calc_pontuacao(self):
        return self.numero_de_artigos * 10 + 20


class Editor(Usuario):
    def calc_pontuacao(self):
        return self.numero_de_artigos * 6 + 15


autor1 = Autor()
autor1.set_numero_artigos(8)
print(autor1.calc_pontuacao())

editor1 = Editor()
editor1.set_numero_artigos(15)
print(editor1.calc_pontuacao())
