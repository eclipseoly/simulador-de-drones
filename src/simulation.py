# Aqui fica o "cérebro" do simulador, que controla as regras do ambiente, mas sem desenhar nada na tela.
# movimento em relacao ao tempo
# colisao
# registro de evento

import drones
import metrics
import random
import time

quantColisoes = 0
quantConcluidos = 0
distanciaMedia = 0
segs = 0
colisoes = 0
chegaram = 0
conjuntoDrones = []
acabou = False


def criandoDrones(n,largura,altura,velocidade):
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
            posx = random.randint(1,820)
            posy = random.randint(1,620)

            if not conjuntoDrones:
                posValida = True
            
            for droneComp in conjuntoDrones:
                if droneComp.posx == posx and droneComp.posy == posy:
                    posValida = False
                    break    
                else:
                    posValida = True
        
        while destinoValido == False:
            destinox = random.randint(1,820)
            destinoy = random.randint(1,620)

            if destinox != posx or destinoy != posy:
                destinoValido = True

        drone = drones.drone(largura,altura,posx,posy,destinox,destinoy,velocidade)
        conjuntoDrones.append(drone)

def verficaColisao(conjuntoDrones):
    global quantColisoes
    for drone in conjuntoDrones:
        for droneComp in conjuntoDrones:
            if drone is droneComp or drone.status != "normal" or droneComp.status != "normal":
                continue
            if abs(drone.posx - droneComp.posx) <= droneComp.largura / 2 and abs(drone.posy - droneComp.posy) <= droneComp.altura / 2:
                drone.status = "colidiu"
                droneComp.status = "colidiu"
                quantColisoes +=2
def locomocao(conjuntoDrones,n):
    global quantColisoes, quantConcluidos, segs, chegaram, colisoes,acabou
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


        verficaColisao(conjuntoDrones)

        metrics.colisoes.append(quantColisoes/2)
        metrics.chegaram.append(chegaram)
        metrics.distancia.append(distanciaMedia)
        # atualiza o tempo
        metrics.tempos.append(segs)
        segs += 0.016
        
        if quantConcluidos + quantColisoes == n:
            acabou = True
            return "fim da simulacao"
        
        time.sleep(0.016)
    
# entradas comuns
# saidas e metricas
# cenarios (pode ter uma interface dividida com os dois cenarios representados)
# utilizar grafos


# trheads simuladas
# plano cartesiano = escolhe os pontos de recarga, ponto de destino e ponto de inicio