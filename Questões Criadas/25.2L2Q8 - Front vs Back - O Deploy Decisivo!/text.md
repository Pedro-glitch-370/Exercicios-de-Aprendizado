# Front vs Back: O Deploy Decisivo!

Cansados dos debates intermináveis sobre interfaces e servidores, 12 desenvolvedores de Front-End e Back-End finalmente encontraram uma forma de resolver suas diferenças: uma partida épica de boa e velha **queimada**!

No entanto, depois de passarem horas grudados em suas cadeiras, nem suas costas aguentam mais passar uma partida inteira em pé! E é por isso que você, aluno do CIn, foi convocado pelos devs para criar uma simulação da partida que permitam eles desenferrujar suas habilidades!

## Input

Cada time será composto obrigatoriamente por 6 jogadores cada.

Antes de iniciar a partida, deve-se pedir qual time começará com a bola. As únicas entradas válidas serão “**Front-End**” e “**Back-End**”:

> `time_atacante (str)`
> 

Todos os jogadores devem começar no campo, fora das áreas de morto.

### Ataque em campo

Cada lance de bola dos jogadores em campo será representado por uma entrada, que pode ser “**acertou**” ou “**errou**”.

> `resultado_ataque (str)`
> 

Caso a entrada seja “**acertou**”, deve-se passar um jogador do time acertado para a sua área do morto. A bola deve ser passada para esse jogador, que irá jogá-la do morto.

Por outro lado, caso a entrada seja “**errou**”, há duas possibilidades de continuação:

- Se **não houver** jogadores no morto do time acertado (ou seja, se o time que acabou de jogar a bola estiver todo em campo), o turno apenas passará para o outro time.
- Se **já houver** jogadores no morto do time acertado, uma nova entrada deve ser pedida para saber se o time adversário foi capaz de pegar a bola ou se deixou ela escapar para o morto:

> `resultado_defesa (str)`
> 

Para essa nova entrada, também há duas possibilidades:

- Caso a entrada seja “**pegou**”, o turno passa normalmente para o time que foi atacado, pois nenhum jogador foi acertado e a bola não escapou para o morto.
- Caso a entrada seja “**deixou**”, a bola passa para o morto. Dessa forma, o time que acabou de atacar irá atacar mais uma vez, agora pelo morto.

### Ataque no morto

As regras do morto são as **mesmas** dos jogadores em campo:

- Primeiro, uma entrada sobre se um jogador do time oponente foi acertado ou não.
- Se **não foi** acertado, pede-se uma entrada sobre se o time oponente foi capaz de pegar a bola ou se deixou ela escapar para a área de campo da outra equipe.
- Se **foi** acertado, o jogador no morto *retorna* para área de campo, enquanto um jogador do time acertado vai para a sua área de morto.

Os turnos seguirão até que um dos times não tenha mais nenhum jogador em campo.

**OBS**: Para *todas* as entradas, caso algo inválido seja digitado, o programa deve pedir novamente o input até que receba uma entrada válida.

## Output

Antes de pedir qualquer entrada, o programa deve imprimir: 

> `Serão 12 desenvolvedores defendendo a honra dos seus lados do código! Que vença a melhor stack!`
> 

Sempre que um jogador em campo acertar um jogador adversário, deve-se imprimir:

> `{time_atacante} acertou um jogador!`
> 

Da mesma forma, sempre que um jogador no morto acertar um jogador adversário, deve-se imprimir:

> `O morto do {time_atacante} acertou um jogador!`
> 

Em ambos os casos acima, logo após a mensagem de acerto, deve-se imprimir o estado atual de jogadores em campo da seguinte forma:

> `Back-End: {backs_em_campo} dev(s) em campo. | Front-End: {fronts_em_campo} dev(s) em campo.`
> 

Já a mensagem de vitória irá variar de qual time saiu como vencedor.

Caso o time “**Back-End**” vença, deve-se imprimir:

> `Vitória do Back-End! Restaram {backs_em_campo} devs ainda mantendo o servidor de pé!`
> 

Caso o time “**Front-End**” vença, deve-se imprimir:

> `Vitória do Front-End! Restaram {fronts_em_campo} devs ainda segurando o layout!`
> 

Quanto aos casos de entrada inválida, deve-se imprimir:

> `Entrada inválida!`
> 

**OBS1**: Não há casos de empate.

**OBS2**: Quando um dos times chegar a 0 jogadores em campo, a mensagem de acerto e a mensagem do estado atual da partida ainda devem ser impressas, seguidas logo depois da mensagem de vitória do time que venceu.

# Examples

**Case: 1**

Input:

Front-End
acertou
errou
pegou
acertou
acertou
acertou
errou
deixou
errou
pegou
acertou
acertou
errou
deixou
acertou
errou
pegou
acertou
errou
deixou
acertou
acertou
errou
pegou
acertou

Output:

Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!
Front-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 6 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 6 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 5 dev(s) em campo.
O morto do Front-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 6 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 6 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 2 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 2 dev(s) em campo. | Front-End: 4 dev(s) em campo.
O morto do Front-End acertou um jogador!
Back-End: 1 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 0 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Vitória do Front-End! Restaram 5 devs ainda segurando o layout!

**Case: 2**

Input:

Back-End
errou
acertou
acertou
errou
errou
deixou
acertou
acertou
errou
pegou
errou
pegou
errou
pegou
acertou
errou
pegou
acertou
errou
deixou
acertou
acertou
errou
deixou
errou
pegou
acertou

Output:

Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!
Front-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 6 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Entrada inválida!
Front-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 5 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 4 dev(s) em campo.
Entrada inválida!
Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 3 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 2 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 2 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 1 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 6 dev(s) em campo. | Front-End: 0 dev(s) em campo.
Vitória do Back-End! Restaram 6 devs ainda mantendo o servidor de pé!

**Case: 3**

Input:

acertou
Back-End
errou
acertou
errou
pegou
acertou
acertou
acertou
acertou
errou
pegou
acertou
errou
deixou
acertou
errou
pegou
acertou
acertou
errou
pegou
acertou
errou
deixou
errou
pegou
acertou
acertou
errou
deixou
acertou
errou
pegou
errou
pegou
acertou
acertou

Output:

Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!
Entrada inválida!
Front-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 6 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 6 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 5 dev(s) em campo.
O morto do Front-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 6 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 5 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 5 dev(s) em campo. | Front-End: 4 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 4 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 4 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 3 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 2 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 4 dev(s) em campo. | Front-End: 1 dev(s) em campo.
O morto do Front-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 2 dev(s) em campo.
Back-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 1 dev(s) em campo.
Front-End acertou um jogador!
Back-End: 2 dev(s) em campo. | Front-End: 1 dev(s) em campo.
O morto do Back-End acertou um jogador!
Back-End: 3 dev(s) em campo. | Front-End: 0 dev(s) em campo.
Vitória do Back-End! Restaram 3 devs ainda mantendo o servidor de pé!
