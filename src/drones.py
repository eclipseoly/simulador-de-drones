#Responsável apenas por definir o que um drone é e o que ele sabe fazer sozinho.

class Drone:
    def __init__(self,largura,altura,posx,posy,destinox,destinoy):
        self.largura = largura
        self.altura = altura
        self.posx = posx
        self.posy = posy
        self.destinox = destinox
        self.destinoy = destinoy
        