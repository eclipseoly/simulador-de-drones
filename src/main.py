# import drones
import metrics
# import gui
import simulation
def main():
    n = int(input("numero de drones"))
    largura = 1
    altura = 1
    velocidade = float(input("velocidade de cada drone"))
    simulation.criandoDrones(n,largura,altura,velocidade)
    metrics.gerandoGraficos()
    pass
if __name__ == "__main__":
    main()
