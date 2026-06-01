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
from datetime import datetime
import os

# pega o diretorio de graficos idependentemente de cada sistema operacional
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GRAPHS_DIR = os.path.join(BASE_DIR, "graphs")
os.makedirs(GRAPHS_DIR, exist_ok=True)

tempos = []
colisoes = []
chegaram = []
distancia = []
passos = []

# cada ax é um axes e representa um grafico
def gerandoGraficos():

    #GRÁFICO 1: COLISÕES
    
    fig1, ax1 = plt.subplots()
    
    # Cria um espaço extra na parte de baixo da janela para caber a legenda
    fig1.subplots_adjust(bottom=0.25)
    
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

    # GRÁFICO 2: CHEGARAM AO DESTINO


    fig2, ax2 = plt.subplots()
    
    # Cria um espaço extra na parte de baixo da janela
    fig2.subplots_adjust(bottom=0.25)
    
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


    # GRÁFICO 3: DISTÂNCIA MÉDIA PERCORRIDA

    fig3, ax3 = plt.subplots()
    
    # Desenha a linha mostrando a evolução da distância média ao longo do tempo
    ax3.plot(tempos, distancia,
        color="#480caa",             
        linewidth=2,
        linestyle='--',              
        marker='o',
        markersize=3,
        markerfacecolor='#480caa',
        label='Distância'
    )
    
    # Configurações dos títulos e dos eixos X e Y
    ax3.set_title("Distancia média x Tempo")
    ax3.set_xlabel("Tempo (s)")
    ax3.set_ylabel("Distância (pixels)")
    ax3.legend()

    # salva os graficos na pasta com nomes diferentes
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    fig1.savefig(os.path.join(GRAPHS_DIR, f"colisoes_{timestamp}.png"))
    fig2.savefig(os.path.join(GRAPHS_DIR, f"chegaram_{timestamp}.png"))
    fig3.savefig(os.path.join(GRAPHS_DIR, f"distancia_{timestamp}.png"))

    plt.show()
    # modo interativo
    # plt.ion()