# O Campeão de 87

O tema do campeão do campeonato brasileiro de 1987 sempre é muito polêmico. Enquanto o Flamengo ganhou na bola, o Sport ganhou no tribunal.

O que aconteceu foi que, na época, os clubes brasileiros estavam brigados com a nossa querida CBF, pois os grandes clubes estavam cansados de viagens tão longas e calendários apertados para ter que jogar com clubes muitas vezes inferiores e que não valiam a pena o esforço. Além disso, naquela época, a CBF estava com dinheiro curto e não teria verba para fazer o Campeonato Brasileiro de 1987.

Com isso, os 4 grandes clubes de São Paulo, os 4 grandes do Rio de Janeiro, as duplas mineira e gaúcha, e o Bahia representando o Nordeste, decidiram se reunir e fazer um campeonato à parte da CBF, que seria chamado de Copa União. Como não daria para fazer um campeonato com somente 13 times, pediram para as federações de Goiás, Pernambuco e Paraná escolherem seus clubes mais populares para disputar também o campeonato. Foi assim que Santa Cruz, Goiás e Coritiba entraram na Copa também.

Com isso, o campeonato estava formado. Porém, a CBF conseguiu dinheiro para fazer o campeonato depois e decidiu, então, pegar os times que sobraram e fazer um outro chaveamento chamado de Módulo Amarelo, e chamou a Copa União de Módulo Verde. A ideia da CBF era pegar os campeões e vices de cada módulo e fazer um chaveamento. No entanto, quem assinou esse acordo foi Eurico Miranda, o presidente do Vasco, sem convencer ninguém do Módulo Verde.

E assim, quando o Flamengo foi o campeão dos grandes clubes, a CBF queria que ele e o Internacional (vice) jogassem contra o Sport e Guarani para decidir o campeão. O Flamengo, que já era campeão da Copa União (o verdadeiro campeonato nacional daquele ano, tendo em vista os patrocínios e a atenção que trazia), decidiu que não iria jogar, pois nada tinha sido acordado com ele. Então, a CBF decidiu dar o Campeonato Brasileiro de 1987 para o campeão do Módulo Amarelo (Sport), e assim nasceu uma das maiores polêmicas do futebol brasileiro.

A partir de toda essa história, você, aluno de IP, foi convocado pela CBF para desenvolver um **sistema que simule todos os acontecimentos do campeonato da época**, dadas as instruções do atual presidente Samir Xaud:

Crie um programa que receba os times e o estado de cada time;
Você irá colocar os times em um dicionário, este dicionário deve possuir 2 times do Sudeste, 2 do Sul e 2 do Nordeste;
Seu programa deve receber inputs até o input ser “FIM” ou for atingido a quantidade máxima de clubes (6 clubes);
Caso a cota de região já tenha sido atingida, o clube não deve entrar no dicionário e o programa deve pedir outro clube no lugar ( ex: já existe (Coritiba, Sul) e (Grêmio, Sul), então não deverá entrar mais nenhum time do sul na lista). Você deve coletar o estado do clube e criar um mecanismo que identifique a sua região.
Você também vai receber os jogos e seus placares, considerando que cada vitória vale 3 pontos, cada empate vale 1 ponto e a derrota vale nenhum. Calcule a pontuação de cada clube. Em caso de empate na pontuação, o desempate será o saldo de gols (gols feitos - gols sofridos).
Seu programa deverá pôr os clubes em ordem de pontuação decrescente. Os 4 primeiros passarão para a próxima fase.
Na próxima fase serão as semifinais, onde o primeiro jogará com o quarto e o segundo jogará com o terceiro e os vencedores irão para a final.
Nas semifinais, seu programa não vai receber o placar do jogo dessa vez, ele vai começar a pedir entradas com o nome de um jogador e seu clube. Isso significa que ele fez um gol. Assim, o time que fizer faz mais gols vence\*\*. Quando receber "FIM" a partida acaba. Se ela acabar empatada o vencedor deve ser o que ficou melhor posicionado na fase de liga.
O mesmo que acontece na semifinal (citado no tópico anterior) vai acontecer na final.
No fim, você também vai ter que calcular o artilheiro desta fase final (semifinais + final).

# Input

Primeiramente, o seu programa vai receber os times até o input "FIM" ser enviado ou a quantidade máxima de clubes (6) for atingida:

clube ou FIM (str)

Seu estado:

sigla_estado (str)

Após terminar de receber os clubes e seus dados:

Placares no formato:

time_1 0 X 0 time_2 (str)

Exemplo:

Náutico 8 x 0 Sport

Obs: Sempre serão 15 confrontos.

Após terminar a fase de liga:

Jogadores no formato:

Jogador - Time (str)

Obs.: Lembre que, nas semifinais e final, isso indica que o Jogador fez gol pelo Time.

# Output

Caso o programa receba um time cuja cota de região já foi atingida, imprima:

Cota para a região {região} atingida. Por favor, insira um clube de outro estado, de outra região.

Caso FIM seja informado e o campeonato não tenha atingido 6 clubes, imprima a seguinte frase e encerre o programa:

Ai não dá, com {qtd_de_time} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF

Após os resultados da fase de liga serem informados, a saída deve ser a ordem da tabela no seguinte formato:

time_1 - x pontos

time_2 - y pontos

...

time_6 - z pontos

Em seguida, imprima os confrontos da semifinal:

Os confrontos foram definidos:

{time_1} X {time_4}

{time_2} X {time_3}

Quando a semifinal for começar, imprima:

Vai começar o confronto, quem será que vence?

A cada gol, imprima:

Gol do {clube}, {jogador} é o nome da emoção

Ao fim do jogo, imprima:

Fim de jogo.

Placar: {time_vencedor} {gols_vencedor} X {time_perdedor} {gols_perdedor}

Caso o time passe porque venceu, imprima:

O {time_vencedor} venceu e foi para a final, será que vai ser campeão?

Caso ele empate e passe por ter sido melhor na fase de liga, imprima:

O {time_vencedor} passa para a final após vencer nos pênaltis, será que vai ser campeão? Repita o processo para a segunda semifinal.f

Para a final, imprima:

Vai começar a grande decisão, quem será o campeão brasileiro de 1987?

A cada gol, imprima:

Gol do {clube}, {jogador} é o nome da emoção

Ao fim do jogo, imprima:

Fim de jogo.

Placar: {time_vencedor} {gols_vencedor} X {gols_perdedor} {time_perdedor}

Caso o Sport seja o clube campeão, imprima:\*\*

Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do ‘Brasileiro de Questão de IP’

Caso o Santa Cruz seja o campeão, imprima:

O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação

**ATENÇÃO:**
Nos dois casos anteriores, o título deve ser passado para o vice. Porém, se o vice continuar sendo Sport ou Santa, passe para quem fez mais pontos entre os outros dois times que foram para as semifinais.

Caso o Flamengo seja o clube campeão, imprima:

Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.

Caso o campeão seja qualquer outro, imprima:

E o campeão do real Campeonato Brasileiro de 1987 foi o {nome_do_campeão}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B

No fim, caso o artilheiro seja do time campeão, imprima:

{jogador} garantiu o título do campeonato e a artilharia, que ano feliz para ele

Caso ele seja artilheiro e não seja campeão, imprima:

Apesar de não ter sido campeão, pelo menos {jogador} foi o artilheiro, a culpa não foi dele

Caso ninguém seja artilheiro (ou seja, a semifinal e final terminam empatadas e o critério de desempate dos times é aplicado):

Esse ano o nivel foi fraco, não tivemos um artilheiro

**ATENÇÃO:**
O critério de desempate do artilheiro será ordem alfabética.
NÃO será permitido o uso de LISTAS na questão, a menos que seja na utilização de split(). Consequentemente, não é permitido .values() e .keys().
Não será permitido o uso de sorted(), você deve ordenar o dicionário manualmente.

# Examples

**Case: 1**

Input

Flamengo
RJ
Grêmio
RS
Bahia
BA
Corinthians
SP
Internacional
RS
Santa Cruz
PE
Santa Cruz 1 X 2 Flamengo
Grêmio 2 X 0 Corinthians
Bahia 0 X 2 Internacional
Corinthians 0 X 3 Santa Cruz
Internacional 1 X 3 Flamengo
Bahia 2 X 4 Grêmio
Santa Cruz 1 X 0 Internacional
Corinthians 3 X 0 Bahia
Flamengo 1 X 0 Grêmio
Bahia 0 X 4 Santa Cruz
Grêmio 1 X 1 Internacional
Flamengo 4 X 0 Corinthians
Santa Cruz 2 X 1 Grêmio
Bahia 2 X 5 Flamengo
Internacional 1 X 0 Corinthians
Zico - Flamengo
FIM
Pipico - Santa Cruz
FIM
Bebeto - Flamengo
FIM

Output

Flamengo - 15 pontos
Santa Cruz - 12 pontos
Grêmio - 7 pontos
Internacional - 7 pontos
Corinthians - 3 pontos
Bahia - 0 pontos
Os confrontos foram definidos:
Flamengo X Internacional
Santa Cruz X Grêmio
Vai começar o confronto, quem será que vence?
Gol do Flamengo, Zico é o nome da emoção
Fim de jogo.
Placar: Flamengo 1 X 0 Internacional
O Flamengo venceu e foi para a final, será que vai ser campeão?
Vai começar o confronto, quem será que vence?
Gol do Santa Cruz, Pipico é o nome da emoção
Fim de jogo.
Placar: Santa Cruz 1 X 0 Grêmio
O Santa Cruz venceu e foi para a final, será que vai ser campeão?
Vai começar a grande decisão, quem será o campeão brasileiro de 1987?
Gol do Flamengo, Bebeto é o nome da emoção
Fim de jogo.
Placar: Flamengo 1 X 0 Santa Cruz
Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.
Bebeto garantiu o título do campeonato e a artilharia, que ano feliz para ele

**Case: 2**

Input

Sport
PE
Flamengo
RJ
Grêmio
RS
Vitória
BA
Palmeiras
SP
Atlético Paranaense
PR
Sport 1 X 1 Flamengo
Palmeiras 2 X 2 Atlético Paranaense
Vitória 0 X 3 Grêmio
Atlético Paranaense 0 X 1 Sport
Grêmio 1 X 2 Flamengo
Vitória 0 X 0 Palmeiras
Sport 1 X 0 Grêmio
Atlético Paranaense 2 X 0 Vitória
Flamengo 0 X 0 Palmeiras
Vitória 0 X 3 Sport
Palmeiras 3 X 3 Grêmio
Flamengo 2 X 0 Atlético Paranaense
Sport 0 X 0 Palmeiras
Vitória 0 X 0 Flamengo
Grêmio 4 X 4 Atlético Paranaense
Jorginho - Sport
FIM
Zico - Flamengo
Zico - Flamengo
FIM
Diego Souza - Sport
FIM

Output

Sport - 11 pontos
Flamengo - 9 pontos
Grêmio - 5 pontos
Palmeiras - 5 pontos
Atlético Paranaense - 5 pontos
Vitória - 2 pontos
Os confrontos foram definidos:
Sport X Palmeiras
Flamengo X Grêmio
Vai começar o confronto, quem será que vence?
Gol do Sport, Jorginho é o nome da emoção
Fim de jogo.
Placar: Sport 1 X 0 Palmeiras
O Sport venceu e foi para a final, será que vai ser campeão?
Vai começar o confronto, quem será que vence?
Gol do Flamengo, Zico é o nome da emoção
Gol do Flamengo, Zico é o nome da emoção
Fim de jogo.
Placar: Flamengo 2 X 0 Grêmio
O Flamengo venceu e foi para a final, será que vai ser campeão?
Vai começar a grande decisão, quem será o campeão brasileiro de 1987?
Gol do Sport, Diego Souza é o nome da emoção
Fim de jogo.
Placar: Sport 1 X 0 Flamengo
Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'
Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.
Zico garantiu o título do campeonato e a artilharia, que ano feliz para ele
