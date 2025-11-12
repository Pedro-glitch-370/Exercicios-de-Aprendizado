# A Grande Final!
*Nível: Difícil*

Enfim chegamos à grande decisão da copa do mundo de tênis de mesa! De um lado, temos o grande tenista chinês Lin Shidong, atual melhor jogador do esporte do planeta. Do outro, a grande sensação do tênis de mesa mundial, uma estrela em ascensão e que vem crescendo nos momentos decisivos: o brasileiro Hugo Calderano!

Mas espere, há uma reviravolta! Os organizadores da competição acreditam muito no potencial do brasileiro e, por pensarem que essa final seria facilmente vencida por ele e por quererem trazer mais emoção, pediram para que você, aluno de IP, desenvolva um algoritmo que determine o grande campeão com base nos acontecimentos da partida!

**As regras da partida são:**

Cada partida é disputada no modelo “melhor de 5 sets”. Ou seja, vence o primeiro atleta que conquiste 3 sets.
O primeiro atleta que fizer 5 pontos em um determinado set é declarado vencedor do set.
Obs. 1: Em caso de empate em 4 a 4 pontos, a disputa segue no formato “vai a 2” (o primeiro que abrir dois pontos de vantagem leva o set!).

Em caso de empate em 2 a 2 no número de sets, o quinto set será disputado na forma de um “tie-break” até 7 pontos (CLIQUE AQUI para saber mais).
No tie-break, caso haja um empate de 6 a 6, a disputa também seguirá no formato "vai a 2".
Em um set, apenas um atleta joga como sacador. Ao encerrar um set, o sacador muda para o outro atleta. Em um eventual quinto set, os jogadores alternam no saque, seguindo as regras oficiais de um tie-break (o primeiro sacador será quem sacar no primeiro set!).
Obs. 2: Entenda "set" como "uma rodada" da partida.

# Input

A primeira entrada irá informar quem é o primeiro sacador da partida, podendo ser hugo ou lin:

sacador_1

Terá um máximo de cinco (5) sets. Em cada um deles, para cada ponto, será fornecida uma entrada no seguinte modelo:

ação_1-ação_2-ação_3-. . . -ação_n

Obs. 1: Os movimentos são separados por hífens, sem espaços. As ações são intercaladas, de forma que a primeira é sempre do sacador, e os atletas vão alternando nas ações (jogador_1-jogador_2-jogador_1-jogador_2-. . .).

Obs. 2: Não é permitido o uso de split(), pois retorna uma lista. Mas, você pode navegar em cada letra de um string usando for caractere in texto: ...

Existem cinco tipos de ação:

**Ataque**: O jogador bate uma bola ofensiva. Nesse caso, o próximo movimento deve ser obrigatoriamente defensivo. Caso contrário, quem efetuou o ataque ganha o ponto.
**Defesa**: O jogador bate uma bola defensiva. Nesse caso, o próximo jogador não pode efetuar uma bola de defesa em seu próximo movimento. Se o jogador defender uma defesa, ele perde a jogada e o ponto vai para o adversário.
**Controle**: O jogador bate uma bola neutra, de controle. Nesse caso, o próximo jogador está livre para escolher seu próximo movimento.
**Saque**: Só pode ser o primeiro movimento do ponto, usado para iniciar a disputa. A próxima bola não pode ser de ataque; caso contrário, o sacador leva o ponto por ace.
**Erro**: Nesse caso, o jogador não conseguiu devolver a bola pro outro lado da mesa e perde automaticamente o ponto.
Obs. No saque, mesmo sendo realizado na ordem certa, o jogador pode errar.

Cada ponto termina quando algum jogador cometer um erro ou não escolher o ataque correto.

# Output

Inicialmente, deve-se imprimir, numa única linha, uma mensagem aos telespectadores informando o início da partida:

Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!

Sempre que um novo set for iniciado, deve-se imprimir:

Set {set_n}:

Em cada ponto:

Se um atleta fizer um ponto de saque, imprima:
Uau, um ace! {jogador} solta o braço e deixa o adversário parado!

Se um atleta não usar defesa em uma bola de ataque, imprima:
{jogador} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!

Se um jogador tentar usar defesa em uma bola de defesa, imprima:
{jogador} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.

Se um jogador não conseguir defender a bola do adversário (ou seja, se sua ação for um "erro"), imprima:
{jogador} se estica, tenta a defesa, mas não alcança — ponto para o adversário.

Ao final de cada ponto, informe o vencedor e o placar:

Ponto para {jogador}!

Placar do {numero_do_set} set : {pontos_hugo} x {pontos_lin}

Se um set for para o “vai a 2”, imprima:

O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!

Se um set for vencido por 5 a 0, imprima:

Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {jogador} passeia na mesa

Caso não tenha sido 5 a 0, imprima:

E o set vai para {jogador}!

Ao final de cada set, informe o vencedor e o placar:

Placar do jogo: {sets_hugo} x {sets_lin}

Se houver um quinto set, imprima:

Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!

Se o tie-break for para o “vai a 2”, imprima:

O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?

Se o tie-break for vencido por 7 a 0, imprima:

Fim de tie-break! {jogador} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!

Ao final da partida, informe o vencedor:

Se Hugo ganhar sem tie-break:
Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!

Se Hugo ganhar com tie-break:
Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!

Se Hugo perder no tie-break:
Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!

Se Hugo perdeu sem tie-break:
Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!

# Examples

**Case: 1**

Input

hugo
saque-ataque
saque-controle-defesa-defesa
saque-controle-ataque-controle
saque-controle-controle-erro
saque-controle-controle-controle-controle-erro
erro
saque-controle-defesa-ataque-erro
saque-controle-erro
saque-defesa-defesa
saque-controle-controle-controle-defesa-controle-ataque-defesa-defesa
saque-erro
saque-controle-controle-controle-ataque-ataque
saque-controle-controle-controle-controle-controle-controle-erro
saque-controle-controle-defesa-controle-defesa-controle-controle-defesa-defesa
saque-defesa-ataque-erro

Output

Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!
Set 1:
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 1 set : 1 x 0
Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 2 x 0
Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!
Ponto para Hugo!
Placar do 1 set : 3 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 4 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 5 x 0
Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Hugo passeia na mesa
Placar do jogo: 1 x 0
Set 2:
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 1 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 2 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 3 x 0
Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 4 x 0
Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 5 x 0
Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Hugo passeia na mesa
Placar do jogo: 2 x 0
Set 3:
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 3 set : 1 x 0
Hugo acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!
Ponto para Hugo!
Placar do 3 set : 2 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 3 set : 3 x 0
Lin tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.
Ponto para Hugo!
Placar do 3 set : 4 x 0
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 3 set : 5 x 0
Fim de set! Domínio total: 5 a 0, sem chance para o adversário — Hugo passeia na mesa
Placar do jogo: 3 x 0
Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!

**Case: 2**

Input

lin
saque-erro
saque-defesa-erro
saque-defesa-ataque-erro
saque-defesa-ataque-defesa-erro
saque-erro
saque-defesa-ataque-erro
saque-defesa-erro
saque-erro
saque-erro
saque-defesa-erro
saque-defesa-ataque-erro
saque-defesa-ataque-defesa-erro
saque-erro
saque-defesa-ataque-erro
saque-defesa-erro
saque-erro
saque-erro
saque-defesa-erro
saque-defesa-ataque-erro
saque-erro
saque-defesa-ataque-defesa-erro
saque-defesa-ataque-erro
saque-erro
saque-erro
saque-defesa-erro
saque-defesa-ataque-erro
saque-defesa-ataque-defesa-erro
saque-erro
saque-defesa-erro
saque-defesa-ataque-erro
saque-defesa-ataque-defesa-erro
saque-erro
saque-defesa-ataque-erro
saque-erro
saque-erro
saque-defesa-erro
saque-defesa-erro
saque-erro
saque-defesa-ataque-erro
saque-defesa-erro
saque-defesa-erro
saque-erro
saque-erro
saque-defesa-erro
saque-defesa-erro
saque-erro
saque-defesa-erro

Output

Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!
Set 1:
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 1 set : 0 x 1
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 1 x 1
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 1 set : 1 x 2
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 2 x 2
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 1 set : 2 x 3
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 1 set : 2 x 4
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 1 set : 3 x 4
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 1 set : 3 x 5
E o set vai para Lin!
Placar do jogo: 0 x 1
Set 2:
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 2 set : 1 x 0
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 2 set : 1 x 1
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 2 x 1
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 2 set : 2 x 2
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 2 set : 3 x 2
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 2 set : 4 x 2
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 2 set : 4 x 3
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 2 set : 5 x 3
E o set vai para Hugo!
Placar do jogo: 1 x 1
Set 3:
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 3 set : 0 x 1
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 3 set : 1 x 1
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 3 set : 1 x 2
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 3 set : 1 x 3
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 3 set : 2 x 3
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 3 set : 2 x 4
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 3 set : 2 x 5
E o set vai para Lin!
Placar do jogo: 1 x 2
Set 4:
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 4 set : 1 x 0
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 4 set : 1 x 1
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 4 set : 2 x 1
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 4 set : 2 x 2
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 4 set : 3 x 2
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 4 set : 3 x 3
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 4 set : 4 x 3
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 4 set : 4 x 4
O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 4 set : 5 x 4
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 4 set : 6 x 4
E o set vai para Hugo!
Placar do jogo: 2 x 2
Set 5:
Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 5 set : 0 x 1
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 5 set : 1 x 1
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 5 set : 1 x 2
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 5 set : 2 x 2
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 5 set : 2 x 3
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 5 set : 3 x 3
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 5 set : 3 x 4
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 5 set : 4 x 4
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 5 set : 4 x 5
Uau, um ace! Hugo solta o braço e deixa o adversário parado!
Ponto para Hugo!
Placar do 5 set : 5 x 5
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 5 set : 5 x 6
Lin se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Hugo!
Placar do 5 set : 6 x 6
O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?
Uau, um ace! Lin solta o braço e deixa o adversário parado!
Ponto para Lin!
Placar do 5 set : 6 x 7
Hugo se estica, tenta a defesa, mas não alcança — ponto para o adversário.
Ponto para Lin!
Placar do 5 set : 6 x 8
E o set vai para Lin!
Placar do jogo: 2 x 3
Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!
