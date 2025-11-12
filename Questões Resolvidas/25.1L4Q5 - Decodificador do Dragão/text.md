# Decodificador do Dragão

Em mais uma de suas muitas aventuras em busca das esferas do dragão, Goku e Bulma se deparam com um imenso problema: o dispositivo rastreador das esferas foi destruído após a invasão de Piccolo Daimaoh à Terra!

Como seria extremamente exaustivo construir um novo aparelho do zero e sozinha, Bulma recorre aos melhores programadores que ela conhece: os alunos de Introdução à Programação do Centro de Informática. A missão é clara: construir um decodificador de coordenadas a partir de expressões aritméticas em notação prefixa.

# Processo de Decodificação

Cada esfera está associada a um único par ordenado (x, y) dentro de uma matriz quadrada de dimensão n × n. No entanto, essas coordenadas não são fornecidas diretamente — elas estão codificadas em ** expressões aritméticas prefixadas (notação polonesa)** para cada coordenada x ou y. Seu trabalho como programador é criar um sistema de decodificação que siga este processo:

**Avaliação de Expressões (notação prefixada):**
Cada linha contém uma expressão aritmética prefixada, como + 3 2 .
O programa deve avaliar cada expressão e verificar se o resultado é um número primo.

**Conversão em Bits:**
Se o resultado for um número primo, adicione o caractere '1' à string binária. Caso contrário, adicione '0'.
Após as expressões, forme uma string de bits (como "01010110"), e converta esse valor binário para decimal.

**Redução Módulo n:**
Pegue o valor decimal gerado e calcule o resto da divisão por n (valor % n). Esse valor será a coordenada x ou y da esfera.

**Organização das Coordenadas:**
O primeiro grupo de expressões sempre forma o valor de x da i-ésima esfera.
O segundo grupo de expressões forma o valor de y dessa mesma esfera.

**Delimitação de Pontos:**
Após cada grupo sempre terá uma linha vazia.
A linha "------------------------------------" marca o inicio do par (x, y) da esfera atual.

**Término da Entrada:**
A entrada termina quando for lida a linha: "Todos os bits foram decodificados".

**Resolvendo notações polonesas:**
Como Bulma é uma inventora brilhante e muito solidária, ela obviamente não ia deixar essa tarefa para vocês sem uma explicação clara de como funciona a resolução de notações pré-fixas, aqui vai um pequeno passo a passo:

1 - Normalmente, escrevemos expressões aritméticas da seguinte forma “{operando1} {operador} {operando2}”, exemplo: 3 + 4, 7 - 2 \* 3, 8 / 4 + 2 e assim por diante.

2 - No entanto, a notação polonesa possui a forma: “{operador} {operando1} {operando2}”, ou seja, o operador vem antes dos operandos.

3 - A estratégia mais comum para resolver esse tipo de expressão é percorrê-la da direita para esquerda, utilizando a estrutura de dados pilha (stack).

A cada número encontrado, empilhe.
Para cada operador encontrado, desempilhe dois operandos, aplique a operação, e empilhe o resultado novamente.

4 - Exemplo: \* + 2 3 4, percorrendo da direita para esquerda, temos o seguinte processo:

Empilhe os números conforme forem encontrados da direita para a esquerda, ou seja, primeiro 4, depois 3, depois 2.
Ao encontrar o operador ‘+’, desempilhe os números 2 e 3, e empilhe “(2 + 3)” = 5.
Ao encontrar o operador ‘_’, desempilhe o número 4, e empilhe “((2 + 3) _ 4)” = 20 .

Obs.0: A estrutura de dados pilha, como pode ser observado acima, tem um comportamento de LIFO (Last-In, First-Out), ou seja, os últimos elementos a entrarem na pilha, serão os primeiros a sair. No exemplo acima, podemos ver isso, em que empilhamos o 4, o 3 e o 2, nessa ordem. E, ao desempilhar, os dois últimos empilhados são retirados.

Obs.1: Teremos somente as operações soma(+), subtração(-), multiplicação(\*) e divisão(/).

Obs.2: Considere que no caso do operador da divisão (“/”), não haverá **divisão por 0 e todas as ** divisões feita terão resto zero (divisão inteira).

**OBRIGATORIO:** no mínimo as seguintes funções e seus respectivos objetivos:
Função para calcular a expressão prefixa;
Função para verificar se é primo;
Função para converter de binário para decimal;
Função para processar as coordenadas (que será reutilizada tanto para a coordenada de x, quanto para a de y).
Função para saber qual é a esfera mais perto.
Lembrando que tuplas (,) está proibido, mas podem usar listas [,].

# Input

1 - O código começa recebendo um número inteiro n ≥ 3, indicando a ordem da matriz quadrada.

n

2 - Logo após isso, você irá receber as coordenadas cartesianas indicando a localização de Goku no mapa da seguinte forma, com os parênteses incluídos na entrada:

(x_goku, y_goku)

3 - Em seguida, recebemos uma linha vazia

4- Uma quantidade indeterminada desse bloco de entradas que representarão cada esfera:

Linhas de expressões aritméticas em notação pré-fixa para x.
Linha vazia, indicando o fim da codificação da coordenada x.
Linhas de expressões aritméticas em notação pré-fixa para y.
Linha vazia, indicando o fim da codificação da coordenada y.
A linha: “------------------------------------” indicando o fim da decodificação da esfera do dragão em análise.

5- A condição de parada “Todos os bits foram decodificados”.

# Output

1 - Antes de tudo, começamos imprimindo a seguinte mensagem nostálgica:

'🟠 Vamos conquistar as esferas do dragão! 🟠'

2 - Em seguida uma linha tracejada, exatamente com 74 traços:

'--------------------------------------------------------------------------'

3 - Depois uma linha vazia:

''

4 - Após isso, vários outputs com o modelo:

'Coordenada x da {i}ª esfera do dragão obtida pelo código binário {cadeia_binária}: {x}'

'Coordenada y da {i}ª esfera do dragão obtida pelo código binário {cadeia_binária}: {y}'

'As coordenadas da {i}ª esfera do dragão são: ({x}, {y})'

''

No qual i representa a i-ésima esfera do dragão analisada, começando da 1ª.

5 - Fechando esse bloco de saída, acrescentamos mais uma linha tracejada

'--------------------------------------------------------------------------'

6 - Pule mais uma linha

''

7 - Depois você irá colocar a matriz quadrada n x n, de tal forma que, a localização de Goku é representada na matriz como “G”, cada localização de esfera é representada como ☆ e o resto dos pontos é desenhado como “.” e entre cada ponto da mesma linha tem um espaço ' ' separando eles, exemplo:

☆ . .
. G .
. . ☆

Obs2: Não haverá casos onde duas ou mais esferas se localizam nas mesmas coordenadas (x, y), bem como Goku não poderá estar na mesma posição que nenhuma esfera.

8 - Após mais uma quebra de linha

''

9 - Agora vamos imprimir o caminho que goku irá realizar, indo desde sua localização inicial de Goku até cada esfera do dragão seguindo uma ordem de acordo com a distância euclidiana da posição atual até a esfera do dragão mais próxima a essa posição, em outras palavras: distancia_atual_esfera = ((x_esfera - x_atual)\*\*2 + (y_esfera - y_atual)\*\*2)\*\*0.5

Trajetória completa de Goku: (x_goku, y_goku) -> (x_esfera1, y_esfera1) -> (x_esfera2, y_esfera2) -> … -> (x_esferan, y_esferan)

Onde (x_esfera1, y_esfera1) é a localização da esfera mais próxima a posição inicial de goku e (x_esferan, y_esferan) a última esfera visitada.

Obs3: Caso haja empate na distância entre duas ou mais esferas, a ordem de decodificação deve ser considerada como critério de desempate na ordenação.

10 - Após coletar todas as esferas, colocamos a frase final!

Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉

Dica: para prevenir erros do comparador de saidas, utilizem print().

# Examples

**Case: 1**

Input

3
(1, 1)

---

\+ 3 2
\- 6 5
\+ - 6 2 9 \* + 7 5 3 \* + 5 6 2 \* 0 10
\+ - 8 6 1 \* \* 5 6 7

\* 20 30
\+ - 10 6 3
\+ - 6 5 3 \* _ 20 10 0
\+ / / 16 4 2 6
/ _ 8 9 3
\+ \* - 20 10 2 3 \* 0 0

---

\* 200 2 \* / 400 10 0
\+ 1000 6
\+ + 7 8 2
\+ / 6 3 1
\+ 20 6
\+ - 8 7 2
\+ 1 3

\+ 2 1
\- 5 3
\+ \* 9 3 4
\- 5 2
\+ - 7 3 3
/ 10 2
/ / 100 5 4
\+ 0 1

Todos os bits foram decodificados

Output

🟠 Vamos conquistar as esferas do dragão! 🟠
\--------------------------------------------------------------------------

Coordenada x da 1ª esfera do dragão obtida pelo código binário 10100010: 0
Coordenada y da 1ª esfera do dragão obtida pelo código binário 01000010: 0
As coordenadas da 1ª esfera do dragão são: (0, 0)

Coordenada x da 2ª esfera do dragão obtida pelo código binário 00011010: 2
Coordenada y da 2ª esfera do dragão obtida pelo código binário 11111110: 2
As coordenadas da 2ª esfera do dragão são: (2, 2)

---

☆ . .
. G .
. . ☆

Trajetória completa de Goku: (1, 1) -> (0, 0) -> (2, 2)
Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉

**Case: 2**

Input

4
(2, 0)

---

\+ - 10 1 2 \* 8 9
\+ \* 7 2 3
/ 10 2
/ / 16 4 2 \* - 9 8 2
\+ + - 10 4 6 6

\+ _ 8 5 3 \* 100 5
\+ + 2 3 2
/ _ - + 8 9 5 5 20
\- + 2 3 1
/ 10 5 \* - 3 2 5

Todos os bits foram decodificados

Output

🟠 Vamos conquistar as esferas do dragão! 🟠
\--------------------------------------------------------------------------

Coordenada x da 1ª esfera do dragão obtida pelo código binário 1011110: 2
Coordenada y da 1ª esfera do dragão obtida pelo código binário 1011011: 3
As coordenadas da 1ª esfera do dragão são: (2, 3)

---

. . . .
. . . .
G . . ☆
. . . .

Trajetória completa de Goku: (2, 0) -> (2, 3)
Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉
