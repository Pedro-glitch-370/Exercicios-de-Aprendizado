# Debuggando o Ping Pong

O campeonato de tênis de mesa do InterCIn está próximo e os alunos de IP precisam mostrar que entendem mais do que apenas segurar uma raquete. Eles precisam mostrar domínio sobre lógica e, obviamente, programação. Para isso, os alunos foram convocados para um desafio especial: eles receberam o desafio de criar um programa que faça a simulação de rodadas de tênis de mesa com regras personalizadas.

Mostre que assim como o Calderano, você também é um gênio no que faz!! O jogo funciona a partir de algumas regras.

**Regras do jogo**:
Com uma quantidade ímpar de sets definida na entrada do programa, o jogador que ganhar mais sets ganha a disputa;

Para ganhar o ponto de um set, o jogador participa de várias rodadas, sendo que cada rodada corresponde a uma sequência de jogadas, ou seja, um sequência de ações entre os jogadores. A cada rodada vencida, o jogador que venceu ganha um ponto.

Um set só deve acabar quando um jogador alcançar no mínimo 3 pontos sob uma vantagem de 2 pontos em relação ao outro jogador. Dessa forma, se ambos os jogadores possuírem 2 pontos, o set acaba quando um dos jogadores alcançar 4 pontos (considerando que o outro jogador não fez nenhum ponto, caso contrário a condição de vitória continua a mudar, até que algum dos jogadores adquira dois pontos de vantagem sobre o outro).

Existem duas ações que podem ser realizadas durante uma rodada: o saque e a rebatida de bola. Por padrão, o saque da primeira rodada de cada set deverá ser realizado pelo primeiro jogador (conforme a entrada), enquanto nos demais saques da rodada, o saque é realizado pelo jogador que pontuou na última rodada.

Um saque só é válido se tocar a mesa duas vezes: a primeira vez na área do jogador que realizou o saque e a segunda na área do oponente.

A rebatida de bola ocorre sempre após um saque válido, quando o oponente manda a bola de volta. Porém, a bola pode ser derrubada durante esse processo e o jogador que cometer esse erro estará dando o ponto da rodada ao seu oponente.

Os jogadores realizam a disputa sempre num mesmo nível, que pode ser aprendizes, básicos ou amostradinhos. O nível da disputa determina a quantidade máxima de rebatidas numa rodada, que representa quantas vezes os jogadores conseguem rebater a bola sem cometer erros:
Se a disputa for entre "aprendizes": 1 rebatida máxima
Se a disputa for entre "básicos": 2 rebatidas máximas
Se a disputa for entre "amostradinhos": 3 rebatidas máximas

Mesmo assim, a bola pode ser derrubada em qualquer rebatida, informação que seria fornecida conforme uma entrada da seguinte frase:

{jogador} deixou a bola cair

Se a quantidade máxima de rebatidas for atingida sem que nenhum jogador tenha derrubado a bola, o programa receberá mais duas entradas, que correspondem à velocidade dos jogadores (valores inteiros), e vence a rodada quem for menos afobado tiver a menor velocidade:

velocidade_jogador1 (int)
velocidade_jogador2 (int)

# Input

As duas primeiras entradas do programa serão duas strings, representando os dois jogadores que irão competir.

jogador_1 (str)
jogador_2 (str)

Logo após, o programa deve receber uma nova entrada, dessa vez um número inteiro ímpar maior que 0, representando a quantidade de sets que serão realizados para decidir o vencedor.

num_sets (int)

Em seguida, o programa recebe o nível da disputa (aprendizes , básicos ou amostradinhos), que será utilizado para determinar a quantidade máxima de rebatidas a cada ponto:

nivel_disputa (str)

Durante cada ponto, a ação dos jogadores pode ser saque ou rebatida e é indicada conforme uma entrada:

acao (str)

Quando a ação de saque é recebida, após ela o programa recebe mais duas entradas, que representam qual parte da mesa a bola tocou:

entrada1 (str)
entrada2 (str)

Se as entrada forem "SA", seguida por "AO": é o único tipo de saque válido (primeira a bola toca na sua área e em seguida toca na área do oponente)
Se as entrada forem "SA", seguirda por "SA": a bola quica duas vezes na área do sacador → ponto para o adversário
Se as entradas forem "AO", seguida por "AO": saque direto para o oponente → ponto para o adversário
Se houver pelo menos uma das entradas igual a "REDE" → saque inválido, ponto para o adversário
Caso o saque seja válido, haverá uma entrada (ação) “rebatida”, indicando o ínício das rebatidas de bola entre os jogadores:

rebatida

**OBS**: Essa entrada corresponde à ação de tentativa de rebatida, não uma rebatida em si, ou seja, não necessáriamente ao receber a entrada rebatida, siginifica que o jogador rebateu. Isso só será determinado na proxima entrada.

As entradas seguintes representam as rebatidas:

entrada_Acao (str)

Se a entrada for "oponente rebateu”, a bola ainda está em jogo e ninguém cometeu nenhum erro até então. Você deve contabilizar a rebatida realizada e receber as novas entradas correspondentes às ações dos jogadores.
oponente rebateu

Se a entrada for "{jogador} deixou a bola cair”, então o ponto da rodada vai para o adversário.

{jogador} deixou a bola cair

Se a quantidade máxima de rebatidas for atingida sem que nenhum jogador tenha derrubado a bola, o programa receberá mais duas entradas, que correspondem à velocidade dos jogadores (valores inteiros), e vence a rodada quem tiver a menor velocidade:

velocidade_jogador1 (int)
velocidade_jogador2 (int)

# Output

Se ambos os jogadores tiverem alguns dos seguintes nomes Luis, Lavoisier, Joab ou Renan, o programa deve imprimir a seguinte frase:

Essa partida vai ser épica! O jogo vai ser emocionante!

Ao início de cada set, imprima:

Iniciando o {n}º set

Ao realizar um saque, imprima:

O saque é de {sacador}

Se o saque for “SA” seguido de “AO”, o saque será válido e você deve imprimir a seguinte frase:

Um saque PERFEITO!!

Se a bola quicar duas vezes na área do sacador (”SA” seguido de “SA”):

{sacador}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??

Se a bola tocar a área do oponente duas vezes ("AO" seguido de "AO"):

Boa, {sacador}! Deu ponto de graça pro oponente!! Agora quem saca é {oponente}

Se alguma das entradas for “REDE”:

Vish, ainda bateu na rede

Ao final do programa, imprima a seguinte frase:

Depois de {num_sets} set(s) vibrante(s), o grande vencedor é {Vencedor}!!

Fim do jogo!

# Examples

**Case: 1**

Input

Ana
Joao
1
amostradinhos
saque
SA
AO
rebatida
Joao deixou a bola cair
saque
AO
AO
saque
SA
AO
rebatida
Ana deixou a bola cair
saque
SA
AO
rebatida
Ana deixou a bola cair

Output

Iniciando o 1º set
O saque é de Ana
Um saque PERFEITO!!
O saque é de Ana
Boa, Ana! Deu ponto de graça pro oponente!! Agora quem saca é Joao
O saque é de Joao
Um saque PERFEITO!!
O saque é de Joao
Um saque PERFEITO!!
Depois de 1 set(s) vibrante(s), o grande vencedor é Joao!!
Fim do jogo!

**Case: 2**

Input

Luis
Lavoisier
1
básicos
saque
SA
AO
rebatida
oponente rebateu
oponente rebateu
10
20
saque
SA
AO
rebatida
oponente rebateu
oponente rebateu
20
22
saque
SA
AO
rebatida
Lavoisier deixou a bola cair

Output

Essa partida vai ser épica! O jogo vai ser emocionante!
Iniciando o 1º set
O saque é de Luis
Um saque PERFEITO!!
O saque é de Luis
Um saque PERFEITO!!
O saque é de Luis
Um saque PERFEITO!!
Depois de 1 set(s) vibrante(s), o grande vencedor é Luis!!
Fim do jogo!
