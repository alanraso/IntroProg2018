# Lights-out

## A interface gráfica

Para auxiliar na elaboração do projeto do Lights-out, foi desenvolvido um programa que usa uma interface gráfica do próprio Python, o Turtle. Se alguém quiser saber mais sobre ele, segue um [link do IME - USP](https://panda.ime.usp.br/pensepy/static/pensepy/03-PythonTurtle/olatartaruga.html).

Essa interface gráfica funcionará de forma semelhante a um [plano cartesiano](https://www.todamateria.com.br/plano-cartesiano/) da matemática, ou seja, por meio de coordenadas (x, y) para identificar o posicionamento das coisas. A única diferença é que o eixo y teria o sentido oposto, apontando "para baixo", pois isso facilita a abstração e uso de matrizes na programação.

## Funções disponíveis (board.py)

Nessa [pasta](https://drive.google.com/drive/folders/1fFD45qTN2EFP9Vm2mghrMAId7tQmf4r9?usp=sharing) no Drive, você vai encontrar dois programas: `board.py` e `board_aux.py`. O primeiro contém algumas funções que nos ajudarão com a interface gráfica do jogo, enquanto o segundo tem apenas algumas funções auxiliares para o primeiro. Para criar o jogo, apenas o `board.py` será usado. Segue uma explicação básica de cada uma dessas funções:

```python
# Recebe como parâmetro uma string e a coloca como título da janela
def titulo(t):

# Recebe como parâmetro uma string, que é o código de uma cor no formato hexadecimal (ex: #FFFFFF), e preenche o fundo da janela com essa cor
def muda_cor_fundo(cor):

# Recebe como parâmetro uma tupla (x, y) de floats que representa o centro da lâmpada (círculo), um float que representa o raio e o código da cor, e desenha o cículo conforme os parâmetros. Se você não enviar um terceiro parâmetro (cor) o círculo será preto. OBS: você pode desenhar um círculo "por cima" do outro, se precisar
def desenha_circulo(pos_centro, raio, cor = '#000000'):

# Recebe como parâmetro uma fução que é executada quando há algum clique na janela.
# A função 'acao_click', por sua vez, recebe como parâmetro dois números x e y, que correspondem às coordenadas do local em que foi clicado na janela
def registrar_click(acao_click):

# Função semelhante ao input do Python que abre um popup, espera o usuário digitar um texto e retorna em forma de string
def input_popup(titulo, mensagem):

# Igual à anterior, mas retorna um número
def input_num_popup(titulo, mensagem, valor_min, valor_max):

# Essa função deve ser utilizada no final do seu programa principal. Ela é responsável por manter a janela aberta e aguardar alguma ação a ser realizada pelo usuário
def aguarda():

# Remove tudo o que foi desenhado na janela
def limpa_tela():

# Fecha a janela e finaliza a interface gráfica
def fechar_janela()
```
