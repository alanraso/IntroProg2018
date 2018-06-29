Este roteiro será um auxiliador para o projeto `Lights-out` do curso de Introdução a Programação.
Tenha em mente que ele é só uma sugestão, você pode, caso deseje, implementar do seu próprio jeito.

## A interface gráfica

Para auxiliar na elaboração do projeto, foi desenvolvido um programa que usa uma interface gráfica do próprio Python, o Turtle. Se alguém quiser saber mais sobre ele, segue um [link do IME - USP](https://panda.ime.usp.br/pensepy/static/pensepy/03-PythonTurtle/olatartaruga.html).

Essa interface gráfica funcionará como um [plano cartesiano](https://www.todamateria.com.br/plano-cartesiano/) da matemática, ou seja, por meio de coordenadas (x, y) para identificar o posicionamento das coisas.

## Funções disponíveis (board.py)

Na [pasta do projeto](https://drive.google.com/drive/folders/1fFD45qTN2EFP9Vm2mghrMAId7tQmf4r9) no Drive você vai encontrar dois programas: `board.py` e `board_aux.py`. O primeiro contém algumas funções que nos ajudarão com a interface gráfica do jogo, enquanto o segundo tem apenas algumas funções auxiliares para o primeiro. Para criar o jogo, apenas o `board.py` será usado. Segue uma explicação básica de cada uma dessas funções:

```python
# Recebe como parâmetro uma string e a coloca como título da janela
def titulo(t):

# Recebe como parâmetro um código de cor e a coloca no fundo da janela
def muda_cor_fundo(cor):

# Recebe como parâmetro uma tupla (x, y) que representa o centro da lâmpada (círculo), o raio e o código da cor, e desenha o cículo conforme os parâmetros. Se você não enviar um terceiro parâmetro (cor) o círculo será branco.
def desenha_circulo(pos_centro, raio, cor = '#FFFFFF'):

# Recebe os mesmo parâmetros da função anterior e pinta o círculo. Se você não enviar um terceiro parâmetro (cor) o círculo será branco.
def pinta_circulo(pos_centro, raio, cor = '#FFFFFF'):

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

## Treinamento inicial

Para se acostumar com o `board.py` e entender as principais funções, você pode fazer alguns comandos simples. Crie uma pasta para o seu futuro `Lights-out`, coloque dentro dela os programas `board.py` e `board_aux.py`. Crie um programa para ser o seu jogo. Nesse programa, escreva na primeira linha:

```python
import board
```

Esse comando serve para que você possa usar as funções que o programa `board.py` disponibiliza. Escreva agora os seguintes comandos:

```python
import board

board.titulo('Teste')
board.aguarda()
```

O primeiro comando vai mudar o título da janela para "Teste", enquanto o segundo, como dito acima, vai mantê-la aberta. Rode seu programa e veja se aparece uma janela vazia com o respectivo título. A partir de agora, siga os passos abaixo para poder aprender o que as funções do board fazem testando. É recomendável rodar seu programa a cada passo.

1. Coloque um título qualquer na janela
2. Mude a cor de fundo da janela. O parâmetro para cor é o código hexadecimal da cor (Ex: #E459A6). Use [esta ferramenta](https://html-color-codes.info/Codigos-de-Cores-HTML/) para consultar o código da cor desejada
3. Desenhe um cículo na posição (0,0)
4. Aumente o tamanho deeste círculo
5. Pinte o círculo (usando novamente um código de cor)

