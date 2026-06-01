# Aqui fica o "cérebro" do simulador, que controla as regras do ambiente, mas sem desenhar nada na tela.
# movimento em relacao ao tempo
# colisao
# registro de evento

import drones
import metrics
import random
import time
import gui

quantColisoes = 0
quantConcluidos = 0
distanciaMedia = 0
segs = 0
colisoes = 0
chegaram = 0
conjuntoDrones = []
acabou = False
somaTemposChegada = 0
passosGerais = 0


def criandoDrones(n, largura, altura, velocidade):
    global quantColisoes, quantConcluidos, segs, chegaram, colisoes
    global somaTemposChegada, passosGerais
    quantColisoes = 0
    quantConcluidos = 0
    segs = 0
    chegaram = 0
    colisoes = 0
    somaTemposChegada = 0
    passosGerais = 0

    metrics.colisoes.clear()
    metrics.chegaram.clear()
    metrics.tempos.clear()
    metrics.distancia.clear()

    for i in range(n):
        # depois implemento pra pegar da interface
        posValida = False
        destinoValido = False

        tentativas = 0
        max_tentativas = 500

        while posValida == False:
            posx = random.randint(1, 820)
            posy = random.randint(1, 620)

            posValida = True

            for droneComp in conjuntoDrones:
                if abs(droneComp.posx - posx) < largura and abs(droneComp.posy - posy) < altura:
                    posValida = False
                    break

            tentativas += 1
            if tentativas >= max_tentativas:
                break  # Desiste de achar uma posição para este drone

        # Se estourou as tentativas, encerra a criação de TODOS os drones restantes
        if tentativas >= max_tentativas:
            print(
                f"Mapa lotado! A simulação foi forçada a iniciar com apenas {len(conjuntoDrones)} drones.")
            break
        # -------------------------------

        while destinoValido == False:
            destinox = random.randint(1, 820)
            destinoy = random.randint(1, 620)

            if destinox != posx or destinoy != posy:
                destinoValido = True

        drone = drones.drone(largura, altura, posx, posy,
                             destinox, destinoy, velocidade)
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
                quantColisoes += 2


def locomocao(conjuntoDrones, n):
    global quantColisoes, quantConcluidos, segs, chegaram, colisoes, acabou
    global somaTemposChegada, passosGerais

    # --- CORREÇÃO DE LÓGICA ---
    # Descobre a quantidade REAL de drones que foram gerados no mapa
    total_drones = len(conjuntoDrones)

    # Prevenção extra caso o usuário inicie com 0 drones
    if total_drones == 0:
        acabou = True
        return "sem drones"

    while True:
        passosGerais += 1
        distanciaMedia = 0
        for drone in conjuntoDrones:
            if drone.status == "normal":
                # vai retornar 1 se concluiu e 0 senao
                resultado = drone.locomocao()
                quantConcluidos += resultado
                if resultado == 1:
                    chegaram += 1
                    somaTemposChegada += segs
            distanciaMedia += drone.distanciaPercorrida

        # Usa o total_drones real para não distorcer a média
        distanciaMedia /= total_drones

        verficaColisao(conjuntoDrones)

        # salva os dados da simulacao na lista dos graficos
        metrics.colisoes.append(quantColisoes/2)
        metrics.chegaram.append(chegaram)
        metrics.distancia.append(distanciaMedia)
        metrics.tempos.append(segs)

        # atualiza o tempo
        segs += 0.016

        # --- A CONDIÇÃO DE PARADA CORRIGIDA ---
        # Agora ele verifica se a soma bate com a quantidade real gerada
        if quantConcluidos + quantColisoes == total_drones:
            acabou = True
            print("concluidos:", quantConcluidos, "colisoes:",
                  quantColisoes, "total:", quantConcluidos + quantColisoes)
            return "fim da simulacao"

        time.sleep(0.016)

# entradas comuns
# saidas e metricas
# cenarios (pode ter uma interface dividida com os dois cenarios representados)
# utilizar grafos


# trheads simuladas
# plano cartesiano = escolhe os pontos de recarga, ponto de destino e ponto de inicio
