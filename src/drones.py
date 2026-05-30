import numpy as np

class drone:
    def __init__(self, largura, altura, posx, posy, destinox, destinoy, velocidade, sigma=0.2, seed=None):
        self.largura = largura
        self.altura = altura
        self.posInicialx = posx
        self.posInicialy = posy
        self.posx = posx
        self.posy = posy
        self.destinox = destinox
        self.destinoy = destinoy
        self.sigma = sigma
        self.velocidade = velocidade
        self.status = "normal"
        self.desvio = np.random.default_rng(seed)
        self.distanciaPercorrida = 0
        self.distanciaPerX = 0
        self.distanciaPerY = 0

    def locomocao(self):
        # distancia ate o destino
        self.distanciax = self.destinox - self.posx
        self.distanciay = self.destinoy - self.posy
        distancia = (self.distanciax**2 + self.distanciay**2) ** 0.5

        # distancia percorrida
        self.distanciaPerX = self.posInicialx - self.posx
        self.distanciaPerY = self.posInicialy - self.posy
        self.distanciaPercorrida = (self.distanciaPerX**2 + self.distanciaPerY**2)**0.5

        if distancia < self.velocidade:
            self.posx = self.destinox
            self.posy = self.destinoy
            self.status = "chegou"
            return 1

        direcao_x = self.distanciax / distancia
        direcao_y = self.distanciay / distancia
        ruido_x   = self.desvio.normal(0, self.sigma)
        ruido_y   = self.desvio.normal(0, self.sigma)

        self.posx += direcao_x * self.velocidade + ruido_x
        self.posy += direcao_y * self.velocidade + ruido_y
        return 0