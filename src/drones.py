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
        self.status = "normal"
        # gera numeros aleatorios
        self.desvio = np.random.default_rng(seed)
    def locomocao(self):
        # calcula a distancia entre o ponto em que esta ate onde quer chegar
        self.distanciax = self.destinox - self.posx
        self.distanciay = self.destinoy - self.posy

        # as duas distancias de x e y reduzidas por pitagoras
        distancia = (self.distanciax**2 + self.distanciay**2) ** 0.5

        # se a distancia for menor que o passo que ele pode percorrer entao chegou ao destino
        if abs(distancia) < self.velocidade:
            distancia = 0
            self.posx = self.destinox
            self.posy = self.destinoy
            print("chegou ao destino")
            self.status = "chegou"
            return 1
        
        # calcula o ruido aleatorio
        # .normal indica que o numero aleatortio e gerado sobre distancia gaussiana
        # sigma e desvio padrao
        # 0 indica a tendencia a ser zero

        # vai ditar para onde ir, se fosse so um sinal postivo ou negativo ele iria, mas n andaria na diagonal
        direcao_x = self.distanciax / distancia
        direcao_y = self.distanciay / distancia

        # calculo o desvio por uma distribuicao gaussiana
        ruido_x = self.desvio.normal(0, self.sigma)
        ruido_y = self.desvio.normal(0, self.sigma)

        # move o drone
        self.posx += direcao_x * self.velocidade + ruido_x
        self.posy += direcao_y * self.velocidade + ruido_y

        print(f"Posição: ({self.posx:.1f}, {self.posy:.1f})")
        return 0