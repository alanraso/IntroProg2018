## Planejamento do projeto

O primeiro passo para conseguir fazer o seu jogo é planejar quais funções você criará. Existem inúmeras vantagens nessa abordagem, mass a principal delas é: você vai poder testar cada pedaço separadamente, e, assim, quando juntar tudo, a probabilidade de confusão é bem menor.

Você pode planejar as suas funções da forma que quiser. Para quem acabou de aprender a programar, no entanto, eu sugiro que você siga as sugestões do roteiro abaixo. Mas nada impede que você tente fazer sem ele.

## Sugestão de roteiro

### Constantes e variáveis globais

Utilizando o que temos disponível no `board.py`, uma das possibilidades de conjunto de funções para fazermos o jogo pode ser:

1. `desenha_tabuleiro`: essa função será responsável por desenhar o tabuleiro inicial 5x5 das lâmpadas Algumas coisas necessárias para essa função:
  1.1. __O estado inicial:__ ou seja, para cada uma das 25 lâmpada, a informação se ela está acesa ou apagada. Podemos usar, para isso, uma lista de variáveis booleanas, ou ainda uma lista de 0 e 1.
  1.2. __A posição de cada círculo:__ ou seja, a dupla (x, y) que representa a posição dos centros dos 25 círculos. Tanto este valor quanto o estado serão usados posteriormente. 
  1.3. __Teste sua função__: é muito importante sempre ir testando o funcionamento dela até atingir o comportamento desejado, isto é, abrir uma janela com os 25 círculos desenhados e posicionados como desejado.
2. `acha_indice_circ`: função que será enviada para o `board.registra_click`. Ela será responsável por identificar s