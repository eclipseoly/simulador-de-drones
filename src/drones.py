import numpy as np

class Drone: #Boa prática: classes começam com letra maiúscula

    def __init__(self,largura,altura,posx,posy,destinox,destinoy,velocidade,sigma=0.2,seed=None):
        self.largura = largura
        self.altura = altura
        self.posx = posx
        self.posy = posy
        self.destinox = destinox
        self.destinoy = destinoy
        self.sigma = sigma
        self.velocidade = velocidade

        # Correção 1: Inicializador correto do NumPy
        self.desvio = np.random.default_rng(seed)

    def locomocao(self):
        
        # Correção 2: Sem 'while True'. O método dá apenas 1 passo por vez.

        # calcula a distancia entre o ponto em que esta ate onde quer chegar

        # Correção 3: Calcula a diferença mantendo o sinal (+ ou -)
        dx = self.destinox - self.posx
        dy = self.destinoy - self.posy

        # A distância total ainda usa Pitágoras
        distancia = (dx**2 + dy**2) ** 0.5

        # se a distancia for menor que o passo que ele pode percorrer entao chegou ao destino
        if distancia < self.velocidade:

            # Correção 4: Atualiza a posição real do drone

            self.posx = self.destinox
            self.posy = self.destinoy
            print("Chegou ao destino!")
            return True # Avisa ao sistema que este drone terminou a rota
            
        # calcula o ruido aleatorio
        # .normal indica que o numero aleatortio e gerado sobre distancia gaussiana
        # sigma e desvio padrao
        # 0 indica a tendencia a ser zero
        ruido_x = self.desvio.normal(0, self.sigma)
        ruido_y = self.desvio.normal(0, self.sigma)

        # Correção 5: Move o drone - (Direção Normalizada * Velocidade) + Ruído
        self.posx += (dx / distancia) * self.velocidade + ruido_x
        self.posy += (dy / distancia) * self.velocidade + ruido_y

        print(f"Posição: ({self.posx:.1f}, {self.posy:.1f})")
        return False # Avisa ao sistema que ainda está voando

        # Correção 6: Remoção do Time Sleep