""" Modifique a classe Televisão de forma que, se pedirmos para mudar o canal para baixo, alem do minimo, ela vai para
o canal maximo. Se mudarmos para cima, alem do canal maximo, que volte ao canal minimo. """


class Televisao:
    def __init__(self, min, max):
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


tv = Televisao(1, 99)
for x in range(0, 101):
    tv.muda_canal_para_baixo()
    print(tv.canal)
