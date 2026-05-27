# Como a coleta de métricas é uma exigência forte, este módulo vai atuar como um "espião" passivo, apenas anotando o que acontece.
# n de drones colididos
# drones que chegaram ao destino
# drones que n chegaram
# tempo medio de respost
# tempo total
# distancia media percorrida
# taxa de colisao
# numero de passos/iteracoes ate o fim da execucao
import matplotlib.pyplot as plt
import time

tempos = []
colisoes = []
chegaram = []
distancia = []
passos = []
distanciaDesvio = []

# cada ax é um axes e representa um grafico
def gerandoGraficos():
    fig1, ax1 = plt.subplots()
    ax1.plot(tempos, colisoes,
        color='#ff4d4d',
        linewidth=2,
        linestyle='--',
        marker='o',
        markersize=3,
        markerfacecolor='#ff4d4d',
        label='Colisões')
    ax1.set_title("Colisões x Tempo")
    ax1.set_xlabel("Tempo (s)")
    ax1.set_ylabel("Colisões")
    ax1.legend()

    # ax1.fill_between(tempos, distancia, distanciaDesvio, color="purple")

    fig2, ax2 = plt.subplots()
    ax2.plot(tempos, chegaram,
        color='#00e676',
        linewidth=2,
        marker='s',
        markersize=3,
        markerfacecolor='#00e676',
        label='Chegaram')
    ax2.set_title("Drones que chegaram x Tempo")
    ax2.set_xlabel("Tempo (s)")
    ax2.set_ylabel("Drones")
    ax2.legend()

    plt.show()
    # modo interativo
    # plt.ion()