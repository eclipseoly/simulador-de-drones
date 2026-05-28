# Aqui fica o "cérebro" do simulador, que controla as regras do ambiente, mas sem desenhar nada na tela.
# movimento em relacao ao tempo
# colisao
# registro de evento

import drones
import metrics
import random

quantColisoes = 0
quantConcluidos = 0
distanciaMedia = 0
segs = 0
colisoes = 0
chegaram = 0

def criandoDrones(n,largura,altura,velocidade):
    conjuntoDrones = []
    global quantColisoes, quantConcluidos, segs, chegaram, colisoes
    quantColisoes = 0
    quantConcluidos = 0
    segs = 0
    chegaram = 0
    colisoes = 0


    metrics.colisoes.clear()
    metrics.chegaram.clear()
    metrics.tempos.clear()
    metrics.distancia.clear()

    
    for i in range(n):
        # depois implemento pra pegar da interface
        posValida = False
        destinoValido = False

        while posValida == False:
            posx = random.randint(1,100)
            posy = random.randint(1,100)

            if not conjuntoDrones:
                posValida = True
            
            for droneComp in conjuntoDrones:
                if droneComp.posx == posx and droneComp.posy == posy:
                    posValida = False
                    break    
                else:
                    posValida = True
        
        while destinoValido == False:
            destinox = random.randint(1,100)
            destinoy = random.randint(1,100)

            if destinox != posx or destinoy != posy:
                destinoValido = True

        drone = drones.drone(largura,altura,posx,posy,destinox,destinoy,velocidade)
        conjuntoDrones.append(drone)
    locomocao(conjuntoDrones,n)

def verficaColisao(conjuntoDrones):
    global quantColisoes
    for drone in conjuntoDrones:
        for droneComp in conjuntoDrones:
            if drone is droneComp or drone.status != "normal" or droneComp.status != "normal":
                continue
            if abs(drone.posx - droneComp.posx) <= droneComp.largura and abs(drone.posy - droneComp.posy) <= droneComp.altura:
                drone.status = "colidiu"
                droneComp.status = "colidiu"
                quantColisoes +=2
                return 1
    return 0
def locomocao(conjuntoDrones,n):
    global quantColisoes, quantConcluidos, segs, chegaram, colisoes
    while True:
        distanciaMedia = 0
        for drone in conjuntoDrones:
            if drone.status == "normal":
                # vai retornar 1 se concluiu e 0 senao
                resultado = drone.locomocao()
                quantConcluidos += resultado
                if resultado == 1:
                    chegaram += 1
            distanciaMedia += drone.distanciaPercorrida
        distanciaMedia /= n


        if verficaColisao(conjuntoDrones):
            colisoes += 1

        metrics.colisoes.append(colisoes)
        metrics.chegaram.append(chegaram)
        metrics.distancia.append(distanciaMedia)
        # atualiza o tempo
        metrics.tempos.append(segs)
        segs += 1
        
        if quantConcluidos + quantColisoes == n:
            return "fim da simulacao"
        
# entradas comuns
# saidas e metricas
# cenarios (pode ter uma interface dividida com os dois cenarios representados)
# utilizar grafos


# trheads simuladas
# plano cartesiano = escolhe os pontos de recarga, ponto de destino e ponto de inicio