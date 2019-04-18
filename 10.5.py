""" Utilizando a classe Televisão modificada no exercicio anterior, crie duas instancias (objetos), especificando o
valor de min e max por nome. """


class Televisao:
    def __init__(self, min=2, max=14):
        self.ligada = False
        self.canal = 2
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


tv = Televisao(min=1, max=22)
for x in range(0, 120):
    tv.muda_canal_para_baixo()
    print(tv.canal)
for x in range(0, 120):
    tv.muda_canal_para_cima()
    print(tv.canal)

tv_sala = Televisao(min=1, max=64)
for x in range(0, 120):
    tv_sala.muda_canal_para_baixo()
    print(tv_sala.canal)
for x in range(0, 120):
    tv_sala.muda_canal_para_cima()
    print(tv_sala.canal)
