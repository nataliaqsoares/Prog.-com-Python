""" Atualmente, a classe Televisão inicializa o canal com 2. Modifique a classe Televisão de forma a receber o canal
inicial em seu construtor. """


class Televisao:
    def __init__(self, canal):
        self.ligada = False
        self.canal = canal
