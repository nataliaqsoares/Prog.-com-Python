""" Utilizando o que aprendemos com funções, modifique o constrtutor da classe Televisão de forma que min e max sejam
parametros opcionais, em que min vale 2 e max vale 14, caso outro valor não seja passado. """


class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = min
        self.cmin = min
        self.cmax = max

    def muda_canal_para_baixo(self):
        if self.canal - 1 < self.cmin:
            self.canal = self.cmax
        else:
            self.canal -= 1

    def muda_canal_para_cima(self):
        if self.canal + 1 > self.cmax:
            self.canal = self.cmin
        else:
            self.canal += 1


tv = Televisao()
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)
for x in range(0, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)
