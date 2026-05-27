# simulador-de-drones
Simulador para a disciplina de Tópicos em Modelos Analítico
instalar o python 3.12.3
instalar o tkinker

"""
 Documentação Gui - Interface

Documentação Técnica: Módulo de Interface Gráfica (GUI)
Projeto: Simulador de Drones
Arquivo Correspondente: src/gui.py

1. Visão Geral do Módulo
O módulo "gui.py" atua como a camada de Front-end (Interface de Usuário) do Simulador de Drones. Desenvolvido sob o paradigma de Orientação a Objetos, ele fornece um ambiente visual interativo para que o usuário insira parâmetros de simulação, acompanhe os logs de execução do sistema em tempo real e observe a renderização gráfica do deslocamento vetorial e de possíveis colisões dos agentes (drones).

2. Requisitos e Configuração do Ambiente
Para a correta execução e renderização da interface gráfica, o ambiente de desenvolvimento requer a instalação de bibliotecas externas específicas, gerenciadas via "pip".

Dependências Externas (Instalação Necessária):

CustomTkinter: Biblioteca de terceiros utilizada para modernizar a interface padrão do Python. Permite o uso de "Dark Mode" nativo e componentes com design atualizado. Para instalar, utiliza-se o comando no terminal: pip install customtkinter

Pillow (PIL - Python Imaging Library): Biblioteca de processamento de imagens necessária para carregar, redimensionar e converter arquivos gráficos complexos (com fundo transparente/Canal Alpha) para o formato suportado pela interface. Para instalar, utiliza-se o comando no terminal: pip install Pillow

Bibliotecas Nativas (Built-in):

os: Utilizada para mapeamento dinâmico de diretórios, garantindo que o software encontre a pasta de imagens (assets) independentemente do caminho ou do sistema operacional em que for executado.

3. Arquitetura e Estrutura do Código
A interface foi encapsulada na classe "App", herdando as propriedades de janela da biblioteca CustomTkinter. A topologia visual foi dividida nos seguintes componentes modulares:

3.1. Configurações de Tela (Windowing)
A janela opera em resolução fixa de 1100x700 pixels, com o redimensionamento nativo bloqueado. Essa trava arquitetural é fundamental para garantir que o "Canvas" (a área de simulação) mantenha proporções cartesianas absolutas, evitando distorções visuais nas coordenadas calculadas pelo motor de física do simulador.

3.2. Painel Lateral (Menu de Configurações)
Posicionado à esquerda, o painel é estruturado com uma largura fixa de 250 pixels. Ele atua como o principal meio de interação do usuário, contendo a entrada de dados para definição da quantidade de drones na simulação e o botão de gatilho principal que inicia a execução visual.

3.3. Terminal de Eventos (Logger Visual)
Implementado na base do Painel Lateral utilizando um componente de caixa de texto de múltiplas linhas. A caixa é mantida em estado de somente leitura. O método interno do código, denominado "imprimir_log", é responsável por destravar a caixa momentaneamente, injetar mensagens em tempo real no console visual e rolar a tela para a linha mais recente, operando como um monitoramento visual que substitui as impressões de terminal convencionais.

3.4. Viewport de Simulação (Canvas)
O componente central do sistema gráfico é o Canvas, ancorado à direita e parametrizado para expandir e ocupar todo o espaço restante da tela. Ele atua como a malha gráfica onde são inseridas as instâncias dos drones, bases e explosões, atualizando suas posições dinamicamente de acordo com o processamento do Back-end.

3.5. Gerenciamento de Imagens (Assets)
Os recursos visuais estão isolados no diretório estático "src/assets/". Durante a inicialização da aplicação, as imagens (drones, explosão, base e alvo) são carregadas, redimensionadas para escalas ideais (40x40 e 50x50 pixels) e armazenadas na memória da aplicação, prontas para serem renderizadas sobre o fundo escuro do Canvas.

4. Instruções de Execução
O módulo possui uma condicional de segurança no final do script que garante seu funcionamento de forma isolada para testes visuais. Para iniciar e testar a interface a partir do diretório raiz do projeto, utiliza-se o comando via terminal: python src/gui.py
 """