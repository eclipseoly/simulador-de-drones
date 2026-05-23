# Aqui fica o "cérebro" do simulador, que controla as regras do ambiente, mas sem desenhar nada na tela.
# movimento em relacao ao tempo
# colisao
# registro de evento

import drones
quantColisoes = 0
quantConcluidos = 0

def criandoDrones(n,largura,altura,posx,posy,destinox,destinoy,velocidade):
    conjuntoDrones = []
    for i in range(n):
        # depois implemento pra pegar da interface
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
    global quantColisoes
    global quantConcluidos
    while True:
        for drone in conjuntoDrones:
            if drone.status == "normal":
                quantConcluidos += drone.locomocao()
                verficaColisao(conjuntoDrones)
        if quantConcluidos + quantColisoes == n:
            return
        

def calculaMetricas():
    pass
# entradas comuns
# saidas e metricas
# cenarios (pode ter uma interface dividida com os dois cenarios representados)
# utilizar grafos


# trheads simuladas
# plano cartesiano = escolhe os pontos de recarga, ponto de destino e ponto de inicio4