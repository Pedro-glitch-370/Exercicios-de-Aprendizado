# A Infiltração e Resgate de Cesar
*Nível: Médio*

Depois de uma longa caminhada por toda Ashina, Wolf acaba de descobrir que tem uma missão ultra secreta: resgatar César do salão principal, onde ele está preso há uma semana sem ler um capítulo de mangá. Em desespero, os professores do CIn te convocaram — você, um estudante brilhante — para ajudar Wolf a encontrar o caminho mais curto até César, antes que ele morra (de tédio).

Wolf começará na posição (0, 0) da matriz que representa o salão principal, com n linhas e m colunas. César está localizado na posição (n-1, m-1), ou seja, no canto inferior direito. Wolf pode se mover para cima, baixo, esquerda e direita, respeitando os limites da matriz e os obstáculos do cenário.

# Regras do Mapa

Cada célula da matriz possui um valor entre 0 e 3, com os seguintes significados:

0: 🚫 Barreira — é impossível atravessar. (Pilar, guarda atento, parede)

1: ✅ Caminho furtivo — Wolf pode passar sem problemas.

2: 🪝 Viga no teto — Wolf pode saltar exatamente duas casas em linha reta (cima, baixo, esquerda ou direita), ignorando o conteúdo das casas intermediárias (inclusive barreiras), mas a célula de destino deve ser válida (não fora da matriz).

3: ⚔️ Inimigo fixo — Wolf pode passar, mas será visto e perderá tempo (movimento custa 3 ao invés de 1).

Obs.1: Quando você utiliza o movimento 2 (🪝 Viga no teto) ele conta como apenas 1 movimento na soma total de movimentos de Wolf, mas avança duas casas na direção selecionada. Já quando você usa o movimento 3 (⚔️ Inimigo fixo), ele conta como 3 movimentos na soma total de movimentos de Wolf, mas avança uma casa na direção selecionada. Obs.2: O salto pela viga no teto não será valido caso aterrisse fora da matriz.

# Input

Você receberá :

Duas entradas (inteiras) representando o formato do salão:

n # número de linhas

m # número de colunas

Em seguida, n linhas contendo m inteiros (0, 1, 2 ou 3), separados por espaço, representando o salão principal

Exemplo de entrada:

3
3
1 1 1
0 3 0
1 1 1

# Output

Assim que você receber as entradas deverá printar a seguinte mensagem de imediato(em prints distintos)

=== SEKIRO: O RESGATE DE CESAR ===

Wolf deve resgatar CESAR!

Em seguida:

Caso Wolf não consiga chegar ao canto inferior direito da matriz (n-1, m-1) imprima a seguinte mensagem :
MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!

Caso Wolf consiga chegar, imprima :
SUCESSO! Wolf resgatou o Cesar em {X} movimentos!

E dependendo do número de movimentos X, imprima também:

Se ele resgatar César em 4 ou menos movimentos :
PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!

Se ele resgatar César em menos de 8 movimentos :
BOM! Caminho eficiente! Mas você quase decepcionou Cesar

Se ele resgatar César em 8 ou mais movimentos :
Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!

**OBSERVAÇÃO**

A solução deve OBRIGATORIAMENTE utilizar recursão na busca pelo melhor caminho, ainda que outras estruturas (como listas ou matrizes auxiliares) sejam utilizadas.

Você deve encontrar o menor caminho até Cesar!

# Examples

**Case: 1**

Input

3
3
1 0 0
0 0 0
0 0 1

Output

=== SEKIRO: O RESGATE DE CESAR ===
Wolf deve resgatar CESAR!
MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!

**Case: 2**

Input

4
3
1 1 0
2 1 0
1 1 0
1 1 1

Output

=== SEKIRO: O RESGATE DE CESAR ===
Wolf deve resgatar CESAR!
SUCESSO! Wolf resgatou o Cesar em 4 movimentos!
PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!
