""" Adicione os atributos tamanho e marca a classe Televisão. Crie dois objetos Televisão e atribua tamanhos e marcas
diferentes. Depois, imprima o valor desses atributos de forma a confirmar a independencia dos valores de cada instancia
(objeto)."""


class Televisao:
    def __init__(self):
        self.ligada = False
        self.canal = 2
        self.tamanho = 49
        self.marca = 'Samsung'
