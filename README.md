Descrição do Simulador

Este projeto consiste em um simulador computacional bidimensional, desenvolvido inteiramente na linguagem Python. A aplicação modela o deslocamento vetorial de múltiplos drones (tratados como agentes independentes) operando simultaneamente em um plano cartesiano.

O simulador é estruturado por uma arquitetura modularizada, compreendendo um motor de física responsável pelo cálculo de rotas, velocidades e detecção de colisões em tempo real, além de uma interface gráfica de usuário (GUI) construída com a biblioteca CustomTkinter para a renderização visual do ambiente. O sistema incorpora elementos estocásticos, como a injeção de ruído gaussiano nas trajetórias para simular perturbações ambientais, e possui um módulo de monitoramento passivo que registra eventos para a geração automatizada de relatórios analíticos e gráficos.

Objetivo do Projeto

O sistema foi desenvolvido para atender às exigências da disciplina de Tópicos em Computação – Modelagem Analítica. O objetivo central é implementar a modelagem matemática do comportamento dinâmico de entidades autônomas em rota para destinos predefinidos, validando a eficácia de algoritmos de detecção de colisão espacial concorrente.

Adicionalmente, o projeto visa aplicar conceitos práticos de avaliação de desempenho de sistemas através da coleta rigorosa de métricas durante a execução, viabilizando o estudo analítico do comportamento do sistema frente a diferentes cargas e parâmetros.

Instruções de Instalação e Execução

Pré-requisitos

É estritamente necessário possuir o ambiente Python 3.x configurado na máquina hospedeira. Recomenda-se a utilização de um ambiente virtual (venv) para o isolamento dos pacotes da aplicação.

Instalação de Dependências

O sistema depende de bibliotecas externas fundamentais para a geração da interface visual, cálculos matriciais e plotagem de dados cartesianos. Para realizar a instalação, abra o terminal na pasta raiz do projeto e execute o comando:

pip install customtkinter Pillow matplotlib numpy

Execução da Aplicação

Com todas as dependências corretamente instaladas, o simulador deve ser iniciado a partir de seu módulo principal de integração. Execute o seguinte comando no terminal:

python main.py

Explicação dos Parâmetros de Entrada

O controle primário da simulação é centralizado em um painel lateral localizado na interface gráfica. Antes do início da rotina matemática, o usuário deve estipular duas variáveis fundamentais de entrada:

Quantidade de Drones: Valor inteiro que define o número exato de entidades que serão instanciadas no plano. O sistema conta com um mecanismo de segurança de área (fail-safe). Caso o valor exigido sature o espaço físico em pixels da malha, impossibilitando uma geração livre de sobreposições, um controlador de limite de tentativas interceptará o laço de repetição, encerrando a criação excedente de drones e informando o número real de instâncias criadas através do log da interface.

Velocidade dos Drones: Valor inteiro que determina a magnitude escalar do deslocamento espacial. Este parâmetro define o incremento em pixels que cada agente aplica aos seus vetores horizontais e verticais a cada ciclo da simulação.

Descrição das Métricas Geradas
O submódulo analítico coleta dados ininterruptamente a cada iteração (passo) do motor virtual. Ao término do processamento geral, os resultados finais são dispostos em formato textual no Terminal de Eventos do sistema, enquanto os históricos temporais são consolidados em gráficos matemáticos salvos de maneira automatizada em um diretório próprio (/graphs). As métricas rastreadas são:

Quantidade de drones que chegaram ao destino: Registro absoluto de entidades que intersectaram a coordenada de seus respectivos alvos.

Percentual de sucesso das missões: Razão matemática percentual entre a quantidade final de drones bem-sucedidos e o número total de drones validados no início da execução.

Quantidade de drones que não concluíram a missão (Colidiram): Total de entidades interceptadas, desativadas antes de cumprir a rota estabelecida.

Taxa de colisão: Proporção percentual de acidentes em relação ao volume populacional absoluto do cenário.

Tempo médio para chegada ao destino: Somatório da minutagem individual cronometrada de cada drone bem-sucedido dividido pelo total de instâncias que atingiram o alvo.

Tempo total de simulação: O tempo real transcorrido (em segundos) medido desde a movimentação inaugural até a estabilização completa do último agente (seja por conclusão ou colisão).

Distância média percorrida: A média global do deslocamento euclidiano de todos os membros ativos na malha a cada passo atualizado.

Número de passos (iterações): O volume exato de ciclos de repetição executados pelo motor computacional principal até o alcance da condição de parada do sistema.

Como as Colisões são Tratadas

O gerenciamento espacial de conflitos opera sob o conceito algorítmico de Caixas Delimitadoras Ortogonais (Bounding Boxes). A verificação ocorre universalmente a cada atualização de quadro (aproximadamente a cada 16 milissegundos).

O motor avalia as entidades aos pares, obtendo a distância escalar absoluta (removendo a negatividade vetorial) entre as coordenadas do eixo X e do eixo Y de dois centros em movimento.

A condição de colisão é tida como verdadeira unicamente se a diferença posicional horizontal e a diferença posicional vertical forem simultaneamente inferiores às dimensões físicas da área preenchida pelos drones (largura e altura).

Ao constatar a interseção matemática entre duas instâncias, o algoritmo altera imediatamente os marcadores de estado (status) de ambos os agentes para o sinal de colisão.

Consequentemente, o sistema cessa qualquer alteração rotacional ou translacional futura das entidades envolvidas. Visualmente, a interface localiza as coordenadas retidas dos acidentados e realiza a substituição da renderização geométrica por um arquivo visual estático demonstrando uma explosão.

Breve Explicação sobre como o Simulador Funciona

O simulador foi desenhado em Arquitetura Orientada a Objetos em consonância com processamento multitarefa (Multithreading) para separar a carga de renderização gráfica da carga de processamento lógico-matemático. A cadência de operações divide-se em três partes:

Geração Segura (Spawning): Inicialmente, o sistema processa a instânciação randomizada das origens e destinos. Através de um laço validador, o algoritmo assegura que nenhuma entidade inicial partilhe a mesma região espacial com outra anteriormente gerada, mitigando as colisões de tempo zero.

Ciclo Cinemático: Operando integralmente em uma Thread apartada, o loop principal isola cada instância ativa, normaliza os vetores de tração fundamentados no Teorema de Pitágoras e injeta o desvio estocástico (ruído Gaussiano da biblioteca Numpy) gerando trajetórias imprevisíveis e dinâmicas.

Ponte Gráfica e Interrupção: De forma concorrente, o laço de repetição principal da interface consome as coordenadas geradas pela Thread de cálculos e efetua o redesenho constante da malha visível. A simulação atinge sua condição de quebra (Encerramento) estritamente no momento em que o agrupamento de entidades colididas somado ao agrupamento de entidades finalizadas totaliza precisamente a lotação computada na fase de geração. Comprovada essa integridade, os ciclos são rompidos, o processamento de análise estatística é acionado e as imagens matemáticas finais são exportadas.