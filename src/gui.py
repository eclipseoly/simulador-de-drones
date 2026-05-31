"""
Módulo de Interface Gráfica (GUI) - Simulador de Drones
Este arquivo é responsável por toda a camada visual (Front-end) do simulador.
Ele cria a janela, os menus e o mapa onde os drones serão desenhados.
"""

import customtkinter as ctk
from PIL import Image, ImageTk # Biblioteca Pillow: Essencial para carregar, redimensionar e exibir arquivos de imagem (como os ícones dos drones)
import os
import simulation
import metrics
import threading

class App(ctk.CTk):
    """
    Classe principal da aplicação que herda de ctk.CTk.
    Trabalhar com Orientação a Objetos aqui garante que a janela e seus 
    componentes (botões, caixas de texto) fiquem encapsulados e organizados.
    """
    
    def __init__(self):
        # Inicia a "planta base" da janela do customtkinter
        super().__init__()


        self.itens_drones = {}
        self.animacaoId = None
        self.threadSimulacao = None

        
        # ======================================================================
        # 1. CONFIGURAÇÕES DA JANELA PRINCIPAL
        # ======================================================================
        
        # Define o título que aparece na barra superior da janela do Windows
        self.title("Simulador de Drones")
        
        # Define a resolução inicial da tela (Largura x Altura em pixels)
        self.geometry("1100x700") 
        
        # Bloqueia o redimensionamento da janela (eixo X e eixo Y).
        # Motivo: Se o usuário esticar a tela, a área do mapa muda de tamanho
        # e as coordenadas matemáticas dos drones ficariam distorcidas.
        self.resizable(False, False) 
        
        # ======================================================================
        # 2. PAINEL LATERAL (Menu de Configurações)
        # ======================================================================
        
        # Cria um "Frame" (um container/caixa) para agrupar os botões na esquerda.
        self.menu_frame = ctk.CTkFrame(self, width=250)
        
        # Posiciona o frame na janela. 
        # side="left": gruda na esquerda.
        # fill="y": estica o frame de cima a baixo na vertical.
        # padx e pady: criam uma margem (respiro) de 10 pixels por fora do frame.
        self.menu_frame.pack(side="left", fill="y", padx=10, pady=10)
        
        # pack_propagate(False) força o frame a manter os 250px de largura que
        # definimos acima, independentemente do tamanho dos botões dentro dele.
        self.menu_frame.pack_propagate(False) 
        
        # --- Componentes dentro do Painel Lateral ---
        
        # Rótulo de texto (Título do menu)
        self.label_titulo = ctk.CTkLabel(self.menu_frame, text="Configurações", font=("Arial", 20, "bold"))
        self.label_titulo.pack(pady=20) # pady=20 dá um espaço em cima e embaixo do texto
        
        # Caixa de entrada de texto (Onde o usuário digita os números)
        # placeholder_text é a "dica" fantasma que some quando o usuário clica
        self.entrada_qtd = ctk.CTkEntry(self.menu_frame, placeholder_text="Qtd de Drones")
        # fill="x" faz a caixinha esticar horizontalmente para preencher o frame
        self.entrada_qtd.pack(pady=10, padx=20, fill="x")


        self.velocidade_qtd = ctk.CTkEntry(self.menu_frame, placeholder_text="Velocidade dos drones")
        self.velocidade_qtd.pack(pady=10, padx=20, fill="x")


        # Botão de Ação
        # command=self.iniciar é o "gatilho". Diz ao botão qual função executar ao ser clicado (sem os parênteses).
        self.botao_iniciar = ctk.CTkButton(self.menu_frame, text="Iniciar Simulação", command=self.iniciar)
        self.botao_iniciar.pack(pady=20, padx=20, fill="x")

        # --- Terminal de Eventos (Log) ---
        
        # Um pequeno título para a área do terminal
        self.label_log = ctk.CTkLabel(self.menu_frame, text="Terminal de Eventos", font=("Arial", 14, "bold"))
        self.label_log.pack(pady=(20, 0)) # Margem apenas no topo
        
        # A caixa de texto onde as mensagens vão aparecer
        # state="disabled" faz com que o usuário não consiga digitar nela, apenas ler.
        # fg_color escuro e text_color verde para dar aquele visual "hacker/sistema"
        self.caixa_log = ctk.CTkTextbox(self.menu_frame, state="disabled", fg_color="#1e1e1e", text_color="#00ff00")
        
        # expand=True faz essa caixa devorar todo o espaço vertical que sobrou no menu
        self.caixa_log.pack(pady=10, padx=10, fill="both", expand=True)
        






        # ======================================================================
        # 3. ÁREA DO MAPA (O "Quadro Negro" da Simulação)
        # ======================================================================
        
        # O Canvas é o único componente que permite desenhar formas livres, 
        # coordenadas X/Y precisas e inserir imagens dinâmicas.
        # bg="#2b2b2b" define um fundo cinza escuro.
        # highlightthickness=0 remove uma borda branca feia padrão do tkinter.
        self.mapa_canvas = ctk.CTkCanvas(self, bg="#2b2b2b", highlightthickness=0)
        
        # Posiciona o Canvas à direita e manda ele expandir (expand=True, fill="both")
        # para devorar 100% do espaço que sobrou na janela livre do menu lateral.
        self.mapa_canvas.pack(side="right", fill="both", expand=True, padx=(0, 10), pady=10)

        # ======================================================================
        # 4. CARREGAMENTO DE IMAGENS (Assets)
        # ======================================================================
        
        # Descobre qual é a pasta exata onde este arquivo (gui.py) está salvo
        diretorio_atual = os.path.dirname(os.path.abspath(__file__))
        
        # 1. Carrega o Drone
        caminho_drone = os.path.join(diretorio_atual, "assets", "drone.png")
        img_drone = Image.open(caminho_drone).resize((60, 60), Image.Resampling.LANCZOS)
        self.icone_drone = ImageTk.PhotoImage(img_drone)
        
        # 2. Carrega a Explosão
        caminho_explosao = os.path.join(diretorio_atual, "assets", "explosao.png")
        img_explosao = Image.open(caminho_explosao).resize((40, 40), Image.Resampling.LANCZOS)
        self.icone_explosao = ImageTk.PhotoImage(img_explosao)

        # 3. Carrega a Base (Deixei um pouco maior: 50x50)
        caminho_base = os.path.join(diretorio_atual, "assets", "base.png")
        img_base = Image.open(caminho_base).resize((50, 50), Image.Resampling.LANCZOS)
        self.icone_base = ImageTk.PhotoImage(img_base)

        # 4. Carrega o Alvo (Também 50x50)
        caminho_alvo = os.path.join(diretorio_atual, "assets", "alvo.png")
        img_alvo = Image.open(caminho_alvo).resize((50, 50), Image.Resampling.LANCZOS)
        self.icone_alvo = ImageTk.PhotoImage(img_alvo)





    # ==========================================================================
    # 5. FUNÇÕES DE AÇÃO (Métodos da Interface)
    # ==========================================================================






    def imprimir_log(self, mensagem):
        """
        Substituto do 'print' padrão. Joga o texto para dentro do painel da interface.
        """
        self.caixa_log.configure(state="normal")           # 1. Destrava a caixa de texto
        self.caixa_log.insert("end", f"> {mensagem}\n")    # 2. Insere a mensagem com um marcador '>'
        self.caixa_log.see("end")                          # 3. Rola a barra de rolagem para a mensagem mais recente
        self.caixa_log.configure(state="disabled")         # 4. Trava a caixa novamente


    def animar(self):
        # movimenta os drones na tela
        for drone, item in self.itens_drones.items():
            self.mapa_canvas.coords(item, drone.posx, drone.posy)
            if(drone.status == "colidiu"):
                self.mapa_canvas.itemconfig(item, image=self.icone_explosao)
        
        if(simulation.acabou == True):
            # espera um segundo e gera os graficos
            self.after(1000, metrics.gerandoGraficos)
            return

        # nao usei while true pq congela a gui
        # chama a funcao a cada 16ms
        self.animacaoId = self.after(16, self.animar)


    def resetar(self):
        # limpa tudo das execucoes anteriores
        # cancela a animacao
        if self.animacaoId:
            self.mapa_canvas.after_cancel(self.animacaoId)
            self.animacaoId = None

        # limpa os dados dos graficos
        metrics.chegaram.clear()
        metrics.colisoes.clear()
        metrics.distancia.clear()
        metrics.tempos.clear()

        # deleta os elementos do quadro
        self.mapa_canvas.delete("all")
        # deleta os drones desenhados
        self.itens_drones.clear()

        # lista os drones criados e reseta o estado para nao acabou
        simulation.conjuntoDrones.clear()
        simulation.acabou = False

        # espera 2 segundos para matar a thread que executa a simulacao
        if self.threadSimulacao and self.threadSimulacao.is_alive():
            self.threadSimulacao.join(timeout=2)

    def iniciar(self):
        """
        Função engatilhada quando o botão 'Iniciar Simulação' é clicado.
        """

        self.resetar()

        qtd_texto = int(self.entrada_qtd.get())
        velocidade = int(self.velocidade_qtd.get())

        largura = 60
        altura = 60

        simulation.criandoDrones(qtd_texto, largura, altura, velocidade)
        for drone in simulation.conjuntoDrones:
            item = self.mapa_canvas.create_image(
                drone.posInicialx, drone.posInicialy,
                image=self.icone_drone,
                anchor="center"
            )
            self.itens_drones[drone] = item

        self.threadSimulacao = threading.Thread(target=simulation.locomocao, args = (simulation.conjuntoDrones,qtd_texto))
        self.threadSimulacao.start()
        self.animar()

        self.imprimir_log(f"Iniciando simulação... Preparando {qtd_texto} drones.")
        # ---------------------------------------------------------
        # self.mapa_canvas.create_image(100, 300, image=self.icone_base, anchor="center")
        # self.mapa_canvas.create_image(200, 300, image=self.icone_drone, anchor="center")
        # self.mapa_canvas.create_image(350, 300, image=self.icone_explosao, anchor="center") 
        # self.mapa_canvas.create_image(650, 300, image=self.icone_alvo, anchor="center")
        
        # ---------------------------------------------------------
        # SUBSTITUÍMOS O PRINT POR SELF.IMPRIMIR_LOG!
        self.imprimir_log("Todos os assets foram desenhados na tela com sucesso!")
        self.imprimir_log("Aguardando motor de física...")
        self.imprimir_log(f"")
        # ---------------------------------------------------------


def run():
    """
    Função principal que prepara o ambiente e liga o motor da interface.
    """
    # Força o CustomTkinter a usar o modo escuro, ignorando as configurações do Windows
    ctk.set_appearance_mode("dark") 
    
    # Instancia a nossa janela (cria o objeto a partir da planta baixa)
    app = App()
    
    # Inicia o 'Main Loop' (Laço Principal). 
    # Isso trava o código aqui e mantém a janela aberta desenhando a tela
    # 60 vezes por segundo, esperando o usuário clicar em algo.
    app.mainloop()

# Essa verificação de segurança garante que a interface só vai abrir se este
# arquivo (gui.py) for executado diretamente. Se outro arquivo importar o gui.py,
# a tela não vai abrir sozinha acidentalmente.
if __name__ == "__main__":
    run()