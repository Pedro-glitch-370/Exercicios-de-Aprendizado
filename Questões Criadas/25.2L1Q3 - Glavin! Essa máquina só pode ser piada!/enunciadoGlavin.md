# Glavin! Essa máquina só pode ser piada!
*Nível: Fácil*

*“ — Isso exigiria algum tipo de rebigulador, o que é um conceito tão ridículo que me dá vontade de rir alto e cair na gargalhada!”*

O professor Frink pode até zombar de certas hipóteses, mas até ele reconhece que, no universo dos Simpsons, uma mera piada pode se revelar como uma previsão disfarçada.

Por isso, intrigado com a quantidade de previsões da série que realmente se confirmaram, Frink decidiu construir uma máquina para avaliar se uma previsão é **confiável** ou não — quem sabe, dessa forma, ele descubra se o rebigulador deixe de ser apenas teoria um dia.

Mas, é claro, uma máquina tão engenhosa só poderia ganhar vida com a ajuda de VOCÊ, futuro mestre programador, que irá contribuir com toda a lógica interna dela. E não se preocupe, pois todo o resto vai ficar a cargo do professor!

## Input

Primeiro, o programa da máquina deve receber uma entrada contendo o nome do futuro inventor:

> `nome`
> 

Depois, o programa deve receber uma entrada contendo o ano em que será feita a invenção:

> `ano`
> 

Se o ano for **divisível** pelo número de letras do nome, então a previsão será **confiável**. Caso contrário, a previsão será **instável**.

**OBS:** Não há casos de nomes compostos.

## Output

Antes de receber os dois inputs, inicie o programa com a seguinte mensagem:

> `Ativando a máquina…`
> 

Caso a previsão seja confiável, deve-se printar:

> `Previsão confiável! O rebigulador será real em <ano>!`
> 

No entanto, caso a previsão seja confiável e o inventor seja Frink, deve-se printar no lugar:

> `Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!`
> 

Já em caso da previsão ser instável, deve-se printar:

> `Previsão instável! <nome> também deve achar que o rebigulador é ridículo...`
> 

Porém, da mesma forma, caso a previsão seja instável e o inventor seja Frink, deve-se printar no lugar:

> `Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!`
> 

**OBS1**: **ano** e **nome** representam as entradas fornecidas.

**OBS2**: O **nome** no output deve sempre começar com letra maiúscula.

# Examples

**Case: 1**

Input

Homer
2030

Output

Ativando a máquina...
Previsão confiável! O rebigulador será real em 2030!

**Case: 2**

Input

Marge
2054

Output

Ativando a máquina...
Previsão instável! Marge também deve achar que o rebigulador é ridículo...

**Case: 3**

Input

Frink
2055

Output

Ativando a máquina...
Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!
