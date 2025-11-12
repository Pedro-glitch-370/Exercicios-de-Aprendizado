# Tá na Capa da Revista: O CIn!!!

O tapete vermelho do CIn está pronto para receber as maiores estrelas da computação! Um desfile de gala, organizado na sempre majestosa Aníbal Fernandes, que irá contar com o brilho dos monitores chefes da cadeira mais famosa do glorioso Centro de Informática!

E você, futura celebridade da programação, foi contratado para **tratar de qualquer subcelebridade desesperada por atenção que tente invadir a passarela!** Mas fique atento, pois invasões demais podem irritar a audiência tech e geek!

## Input

Primeiro, o programa deve receber o número de monitores que irão desfilar:

> `número_desfilantes (int)`
> 

Em seguida, o programa deve receber o nome do **único** patrocinador do evento:

> `marca_do_patrocinador (str)`
> 

Há apenas três patrocinadores possíveis: as marcas “**Tha Beauty**” (associada a “Thais Linares”**), “DeGuê?**” (associada a “Davi Brito”) e “**Diva Depressão**” (associada a “Edu e Fih”). O programa deve saber associar o nome da marca com o nome da(s) subcelebridade(s).

**OBS**: Ambos os nomes associados à “Diva Depressão” devem ser tratados como uma pessoa só, ou seja, como “**Edu e Fih**”, e não como “Edu” e “Fih”.

### Lógica do desfile

Logo depois, para a quantidade de desfilantes, o programa deve receber os nomes de todas as pessoas que estão entrando na passarela:

> `desfilante (str)`
> 

Os integrantes do desfile devem estar dentro da lista de monitores chefes de IP, que inclui: Adrieli Queiroz, Arthur Jorge, César Cavalcanti, Elisson Oliveira, Filipe Moreira, Gabriela Alves, Joab Henrique, Maria Fernanda, Miriam Gonzaga e Sofia Remindes.

Caso o nome de um desfilante não esteja entre os acima, ele se trata de um intruso. Para esse caso, há duas possibilidades de seguimento:

- Se a pessoa invasora **for a patrocinadora** do evento, sua invasão será tolerada, ou seja, seu nome não irá precisar ser removido nem substituído.
- Se a pessoa invasora **não for** a patrocinadora, ela deverá ser substituída de última hora por um monitor que **não foi chamado** em **toda** a lista de entradas.

**OBS1**: A seleção do monitor substituto deve ser feita por ordem alfabética. Por exemplo, se “Adrieli” e “Arthur” forem os únicos monitores fora da lista de entradas, a primeira é quem deve ser chamada para a substituição.

**OBS2**: Um monitor entrar como substituto o classifica como um desfilante oficial, ou seja, em caso de futuras novas invasões, ele **não poderá ser chamado novamente**.

**OBS3**: Caso não haja mais monitores livres para uma substituição, o intruso irá entrar na passarela mesmo após ser notificado como um invasor.

### Condição especial

Tantas invasões de subcelebridades desconhecidas pela galera do CIn vão quebrar o estado de flow do público! Para acalmar os ânimos dessa comunidade que vive logada 24/7, é preciso de um apelo gamer e streamer de uma verdadeira celebridade digital: o Core das Antigas!

Depois de três invasões, o programa deve **inserir** “**Core**” como um desfilante oficial exatamente após o monitor substituto do terceiro intruso.

**OBS1**: Mesmo que não haja monitor substituto para o terceiro intruso, a adição ainda deve ser realizada. Nesse caso, a posição de “Core” será logo após o intruso não substituído.

**OBS2**: A invasão por patrocinador **não deve ser considerada** na contagem do limite de três invasões.

## Output

Antes de tudo, imprima:

> `Senhoras e senhores, o desfile de gala do CIn vai começar!`
> 

### Outputs prévios e opcionais

Caso tenha ocorrido uma invasão (com substituição ou não), imprima:

> `{intruso} invadiu a passarela! Segurem ele(a), produção!`
> 

Entretanto, caso seja uma invasão feita por um **patrocinador**, deve-se imprimir no lugar:

> `Invasão tolerada por motivos de patrocínio!`
> 

Caso “**Core**” entre após a terceira invasão, imprima:

> `Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!`
> 

### Outputs obrigatórios

Para todos os casos em que entrar na passarela um monitor (já previsto ou substituto), um patrocinador ou o youtuber Core, imprima:

> `Desfilante de n° {posicao}: {desfilante}!`
> 

**OBS**: A ordem dos desfilantes deve seguir a ordem das entradas recebidas.

Somente em caso de haver uma invasão sem substituição, deve-se imprimir no lugar:

> `Desfilante de n° {posicao}: {intruso}?! Pelo visto não havia como substituir...`
> 

### Outputs finais e especiais

Ao final do programa, somente em caso de ter como intrusos as subcelebridades “Gretchen”, “Tulla Luana” e “Inês Brasil”, imprima:

> `Nas arquibancadas do CIn, sussurros indignados agitam a multidão...`
> 

Para os outputs seguintes, desconsidere qualquer erro gramatical existente.

Se tiver aparecido “**Gretchen**”, imprima:

> `"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"`
> 

Se tiver aparecido “**Tulla Luana**”, imprima:

> `"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."`
> 

Se tiver aparecido “**Inês Brasil**”, imprima:

> `"É aquele ditado... Vamo fazer o quê?"`
>

## Examples

**Case: 1**

Input:

3
DeGuê?
Adrieli Queiroz
Davi Brito
Malu Borges

Output

Senhoras e senhores, o desfile de gala do CIn vai começar!
Desfilante de n° 1: Adrieli Queiroz!
Invasão tolerada por motivos de patrocínio!
Desfilante de n° 2: Davi Brito!
Malu Borges invadiu a passarela! Segurem ele(a), produção!
Desfilante de n° 3: Arthur Jorge!

**Case: 2**

Input:

6
Tha Beauty
Gretchen
Arthur Jorge
Pepita
César Cavalcanti
Tulla Luana
Thais Linares

Output

Senhoras e senhores, o desfile de gala do CIn vai começar!
Gretchen invadiu a passarela! Segurem ele(a), produção!
Desfilante de n° 1: Adrieli Queiroz!
Desfilante de n° 2: Arthur Jorge!
Pepita invadiu a passarela! Segurem ele(a), produção!
Desfilante de n° 3: Elisson Oliveira!
Desfilante de n° 4: César Cavalcanti!
Tulla Luana invadiu a passarela! Segurem ele(a), produção!
Desfilante de n° 5: Filipe Moreira!
Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!
Desfilante de n° 6: Core!
Invasão tolerada por motivos de patrocínio!
Desfilante de n° 7: Thais Linares!
Nas arquibancadas do CIn, sussurros indignados agitam a multidão...
"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"
"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."