import time
import numpy as np
class drone:
    def __init__(self,largura,altura,posx,posy,destinox,destinoy,velocidade,sigma=0.2,seed=None):
        self.largura = largura
        self.altura = altura
        self.posx = posx
        self.posy = posy
        self.destinox = destinox
        self.destinoy = destinoy
        self.sigma = sigma
        self.velocidade = velocidade
        # gera numeros aleatorios
        self.desvio = np.random.default_desvio(seed)
    def locomocao(self):
        while True:
            # calcula a distancia entre o ponto em que esta ate onde quer chegar
            distanciax = abs(self.destinox - self.posx)
            distanciay = abs(self.destinoy - self.posy)

            # as duas distancias de x e y reduzidas por pitagoras
            distancia = (distanciax**2 + distanciay**2) ** 0.5

            # se a distancia for menor que o passo que ele pode percorrer entao chegou ao destino
            if distancia < self.velocidade:
                distancia = 0
                distanciax = self.destinox
                distanciay = self.destinoy
                print("chegou ao destino")
                return
            
            # calcula o ruido aleatorio
            # .normal indica que o numero aleatortio e gerado sobre distancia gaussiana
            # sigma e desvio padrao
            # 0 indica a tendencia a ser zero
            ruido_x = self.desvio.normal(0, self.sigma)
            ruido_y = self.desvio.normal(0, self.sigma)

            # move o drone
            self.posx += (distanciax + ruido_x) * self.velocidade
            self.posy += (distanciay + ruido_y) * self.velocidade

            print(f"Posição: ({self.posx:.1f}, {self.posy:.1f})")
            # sleep so pra ter um incentivo visual no terminal (acho que vo tirar depois)
            time.sleep(0.1)
            