# Homem-Aranha vs Electro: A Última Sobrecarga
*Nível: Médio*

Nova York está em colapso! Electro está espalhando o caos, dominando quarteirões e causando apagões em toda a cidade. O Homem-Aranha é a última esperança de restaurar a energia e evitar a destruição total.

O amigão da vizinhança contará com você, aluno do Espetacular CIn, para simular o avanço de Electro e a movimentação estratégica do Homem-Aranha dentro da cidade, representada por uma matriz NxN, onde cada célula representa um quarteirão da cidade.

Por ser um trabalho muito tenso, o Homem-Aranha só pode se mover uma posição por dia pra tentar restaurar o quarteirão corrompido. Porém, cuidado: se o Miranha demorar demais para agir, o estrago pode ser irreversível..

Cada quarteirão da cidade pode conter os seguintes elementos:
. → Quarteirão neutro/restaurado
E → Quarteirão corrompido por Electro (ameaça ativa)
H→ Local atual do Homem-Aranha
X → Quarteirão destruído por Electro (irrecuperável)

# Dinâmica do Jogo:

**Movimento do Homem-Aranha:**
A cada dia, o Homem-Aranha pode se mover uma casa nas direções: Cima, Baixo, Esquerda ou Direita.
Se ele pisar em um quarteirão corrompido (E), ele o restaura (.), e esse dia conta como uma ação.
Se ele pisar em um quarteirão neutro (.), nada acontece.
Ao sair de qualquer quarteirão (E ou .), o local anterior será marcado como neutro (.).
Se tentar se mover para fora da cidade ou para um quarteirão destruído (X), ele fica parado e recebe um aviso de erro.
OBS: a cada posição que o Homem-Aranha estiver, o quarteirão estará como “H”. Após sua saída, ele se torna um “.” simbolizando que foi um quarteirão restaurado.

**Destruição causada por Electro:**
Se o Homem-Aranha passar três dias seguidos sem restaurar nenhum quarteirão marcado com a letra E, o Electro percorrerá a cidade e destruirá permanentemente um dos quarteirões corrompidos restante: (E) → (X) (Electro percorre a cidade de cima pra baixo da esquerda pra direita).
Os quarteirões corrompidos que ainda podem ser restaurados serão representados por cada letra E na matriz, já os quarteirões destruídos permanentemente são dados pela letra X
Todos os X da matriz, fornecidos por input ou decorrentes da destruição do inimigo, devem ser contabilizados nos prints diários.

**Condições de Vitória e Derrota:**
O jogo pode terminar conforme as seguintes situações: se não existir mais nenhum quarteirão corrompido (E), se for digitado o comando "FIM", ou após 7 dias de jogo.
O Homem-Aranha vence se conseguir restaurar todos os quarteirões (E) → (.) antes de o jogo terminar.
Caso se passem 7 dias e o Miranha não tenha restaurado todos os quarteirões, ele perde.
Se for digitado “FIM” e ainda restarem quarteirões corrompidos (E), o jogo será encerrado imediatamente e deverá exibir a mensagem final, declarando o Miranha como perdedor.

# Input

Você deverá receber, nesta ordem, os seguintes dados:
Primeiramente você receberá um inteiro N, representando a ordem da matriz quadrada (NxN) que corresponde ao mapa da cidade.

Depois, receberá a própria matriz, com uma linha por vez e os elementos separados entre si por um espaço:

Q00 Q01 Q02 … Q0N
Q10 Q11 Q12 … Q1N
…
QN0 QN1 QN2 … QNN

E por último, o código deverá receber em sequência uma quantidade indeterminada de comandos referentes aos movimentos do Homem-Aranha, até que a entrada seja “FIM”. Os comandos serão dados linha por linha e podem ser: “Cima”, “Baixo”, “Esquerda” ou “Direita”.

{comando 1}
{comando 2}
…

# Output

A cada dia, imprima o conjunto de informações da seguinte forma:
Dia {n}
{matriz formatada linha por linha}
Posição atual do Homem-Aranha: ({linha}, {coluna})
Quarteirões restaurados: {restaurados} | Quarteirões destruídos: {destruidos}
{mensagem_especial}

OBS.1: Após cada dia, pule uma linha para separar visualmente os dias.
OBS.2: Os parênteses indicados na impressão da posição atual do Homem-Aranha são apenas caracteres utilizados na impressão de coordenadas!! O uso de tuplas não está permitido para essa lista.

Mensagem_especial:
Dependendo da ação do dia, imprima uma das mensagens abaixo após os dados principais:

Sempre que o Homem-Aranha restaurar um (E) na matriz, imprima:

O Miranha restaurou um quarteirão!

Se o Miranha não restaurou nenhum quarteirão no dia, imprima:

O Electro está ganhando espaço!

Se o movimento foi inválido (fora dos limites NxN ou X), imprima:

Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!

Mensagem Final!
Se não existir mais nenhum quarteirão corrompido, e o Homem-Aranha tiver restaurado pelo menos um quarteirão, imprima:\*\*

Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!

Caso se passem 7 dias e o homem-aranha não tenha derrotado Electro ainda, ele perde e o programa acaba exibindo a seguinte mensagem:

O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!

E caso o programa receba “FIM” mas ainda tenha quarteirões corrompidos, encerre o programa após imprimir a seguinte frase:

Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!

OBS: a regra geral para ajudar!

Cima → linha -= 1
Baixo → linha += 1
Esquerda → coluna -= 1
Direita → coluna += 1
Os indices sempre iniciam com 0, e essa posição deve ser considerada nos prints do código também!

# Examples

**Case: 1**

Input

3
. E .
H . .
. . .
Direita
FIM

Output

Dia 1
. E .
. H .
. . .
Posição atual do Homem-Aranha: (1, 1)
Quarteirões restaurados: 0 | Quarteirões destruídos: 0
O Electro está ganhando espaço!

Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!

**Case: 2**

Input

5
. . . E .
. X . . .
. . H . E
E . . X .
. . . . E
Direita
Direita
Cima
Esquerda
Baixo
Direita
FIM

Output

Dia 1
. . . E .
. X . . .
. . . H E
E . . X .
. . . . E
Posição atual do Homem-Aranha: (2, 3)
Quarteirões restaurados: 0 | Quarteirões destruídos: 2
O Electro está ganhando espaço!

Dia 2
. . . E .
. X . . .
. . . . H
E . . X .
. . . . E
Posição atual do Homem-Aranha: (2, 4)
Quarteirões restaurados: 1 | Quarteirões destruídos: 2
O Miranha restaurou um quarteirão!

Dia 3
. . . E .
. X . . H
. . . . .
E . . X .
. . . . E
Posição atual do Homem-Aranha: (1, 4)
Quarteirões restaurados: 1 | Quarteirões destruídos: 2
O Electro está ganhando espaço!

Dia 4
. . . E .
. X . H .
. . . . .
E . . X .
. . . . E
Posição atual do Homem-Aranha: (1, 3)
Quarteirões restaurados: 1 | Quarteirões destruídos: 2
O Electro está ganhando espaço!

Dia 5
. . . X .
. X . . .
. . . H .
E . . X .
. . . . E
Posição atual do Homem-Aranha: (2, 3)
Quarteirões restaurados: 1 | Quarteirões destruídos: 3
O Electro está ganhando espaço!

Dia 6
. . . X .
. X . . .
. . . . H
E . . X .
. . . . E
Posição atual do Homem-Aranha: (2, 4)
Quarteirões restaurados: 1 | Quarteirões destruídos: 3
O Electro está ganhando espaço!

Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!
