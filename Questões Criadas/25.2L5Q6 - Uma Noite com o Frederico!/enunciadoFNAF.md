# Uma Noite com o Frederico!
*Nível: Difícil*

Um arrepio desagradável toma seu corpo. Suas pernas logo tremem feito duas folhas de papel e o sour frio começa a escorrer pela testa. Depois de finalmente ficar cara a cara com a temida quinta lista de IP, quase não lhe restam forças para encarar as faces monstruosas da última questão, moldadas nas formas dos mascotes mais memoráveis da franquia de terror “**Five Nights at Freddy’s**”!

Como desafio final dessa jornada de arrepiar, você deve enfrentar mais vez o seu maior medo, **a recursão**, para criar um algoritmo capaz de calcular a **melhor sequência possível de ações para sobreviver ao jogo**. Você será capaz de sobreviver?

## Input

Seu ponto de partida é a tela de configuração da Custom Night: Uma **única entrada** em que o programa deve receber **quatro números inteiros**, cada um representando o nível de IA de cada animatronic do quarteto principal. Quanto maior o valor, mais difícil e **custoso** será lidar com o animatronic.

> **`niveis_dificuldade (str)`**
> 

Os valores devem ir de 0 até 20, representando, respectivamente, **Bonnie, Chica, Freddy e Foxy**.

**OBS1**: Se a entrada não tiver 4 valores ou tiver números que não estão entre 0 e 20, ela deve ser considerada **inválida** e toda a análise da melhor sequência **não deve ser feita**.

**OBS2**: Se o valor de uma dificuldade for 0, o animatronic associado à dificuldade não estará presente na noite, ou seja, **não atacará em momento algum**.

### Simulação

Seu objetivo é encontrar a **melhor sequência de decisões** que não apenas façam o personagem **sobreviver até o fim da noite**, mas também terminar ela com a **maior energia restante possível**.

A energia inicial deve sempre ser considerada **100**. A cada hora, deve ser decrementado **1** de energia, começando já às 0h.

Quanto às decisões, são elas:

- **Abrir ou Fechar a Porta Esquerda** - Se fechada, consome **7** de energia por hora.
- **Abrir ou Fechar a Porta Direita** - Se fechada, consome **7** de energia por hora.
- **Ligar ou Desligar as Luzes** - Se ligadas, consomem **5** de energia por hora.
- **Abrir e Olhar a Câmera** - Se aberta, consome **9** de energia por hora.

Essas decisões são tomadas em cada uma das **seis horas** da noite em que o jogo ocorre, podendo ocorrerem de forma **simultânea**.

Tal qual o jogo, o programa deve iniciar às **0h** e seguir até às **5h**. Será considerado vitória apenas caso o personagem alcance as **6h** **vivo e com mais do que 0 de energia**.

**OBS1**: Valores maiores do que 0 e menores do 1 também devem ser considerados como vitória.

**OBS2**: Está permitido o uso de **None** para essa questão.

### Ataques

Cada um dos quatro animatronics realizam ataques à sua maneira. Seus ataques podem, no entanto, ser frustrados, o que **impede a morte imediata do personagem**, mas **aumentam o consumo de energia** durante a hora do ataque.

O funcionamento dos animatronics ocorre da seguinte forma:

- **Bonnie**: Ataca às **0h** e às **3h**. Seu ataque pode ser frustrado se **a porta esquerda estiver fechada** ou se **as luzes estiverem acesas e o personagem não estiver olhando as câmeras**. Um ataque frustrado seu consome 3 de energia + (dificuldade de Bonnie x 0.25).
- **Chica**: Ataca às **1h** e às **4h**. Seu ataque pode ser frustrado se **a porta direita estiver fechada** ou se **o personagem estiver olhando as câmeras**. Um ataque frustrado seu consome 2 de energia + (dificuldade de Chica x 0.35).
- **Foxy**: Ataca às **4h** se a energia nesse horário estiver **maior do que a metade da energia inicial**. Seu ataque pode ser frustrado se **a porta esquerda estiver fechada**. Um ataque frustrado consome 5 de energia + (dificuldade de Foxy x 0.15).
- **Freddy**: Ataca às **5h**. Seu ataque pode ser frustrado se **ambas as portas estiverem fechadas** ou se **o personagem estiver olhando as câmeras**. Um ataque frustrado consome 3 de energia + (dificuldade de Freddy x 0.35).

**OBS**: Caso dois animatronics ataquem na mesma hora, os dois ataques devem ser frustrados para o personagem continuar vivo.

### Caso Especial

Caso o nível de dificuldade seja um **anagrama de 1987**, um quinto animatronic deve ser adicionado à noite: **Golden Freddy**. Porém, essa condição deve ser aplicada quando os números são **estritamente 1, 9, 8 e 7**, em qualquer ordem.

Golden Freddy ataca às **5h** e seu ataque pode ser frustrado se **o personagem estiver olhando as câmeras** nesse horário. Caso isso ocorra, é consumido 10 de energia + (dificuldade de Freddy x 1.95).

No entanto, caso os quatro números estejam presentes **junto com o número 0**, o programa deve **realizar um print especial**, que será esclarecido abaixo, e **encerrar imediatamente o programa**.

## Output

Caso a entrada seja considerada inválida, imprima:

> **`"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."`**
> 

Caso nenhum animatronic esteja presente, ou seja, a dificuldade de todos seja 0, imprima:

> **`"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."`**
> 

Caso não exista nenhuma sequência de decisões que faça o personagem sobreviver, imprima:

> **`"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"`**
> 

Caso exista alguma sequência em que o personagem termine com vida, imprima:

> **`"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_restante}% de energia. Eu sabia que você conseguiria."`**
> 

Uma nova quebra de linha deve ser feita, e então a sequência com a maior quantidade de energia restante deve ser imprimida. Para cada hora, das 0h até às 5h, deve ser seguido o seguinte modelo:

> **`{horario} AM -> PE: {decisao} | PD: {decisao} | LZ: {decisao} | CAM: {decisao}`**
> 

**Legenda**: PE = Porta Esquerda, PD = Porta Direita, LZ = Luzes, CAM = Câmera.

**OBS1**: A energia deve ser imprimida com aproximação de **duas casas decimais**.

**OBS2**: As decisões devem ser impressas como “**SIM**”, indicando que tal ferramenta foi fechada/usada, ou “**NÃO**”, indicando o contrário.

Por fim, caso a condição do anagrama de Golden Freddy se aplique, mas com um dígito 0 entre os números, deve-se printar:

> **`"IT'S ME"`**
>

## Examples

**Case: 1**

Input:

20 20 20 20

Output:

"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com 2.00% de energia. Eu sabia que você conseguiria."
00:00 AM -> PE: NÃO | PD: NÃO | LZ: SIM | CAM: NÃO
01:00 AM -> PE: NÃO | PD: SIM | LZ: NÃO | CAM: NÃO
02:00 AM -> PE: NÃO | PD: NÃO | LZ: NÃO | CAM: NÃO
03:00 AM -> PE: NÃO | PD: NÃO | LZ: SIM | CAM: NÃO
04:00 AM -> PE: SIM | PD: SIM | LZ: NÃO | CAM: NÃO
05:00 AM -> PE: NÃO | PD: NÃO | LZ: NÃO | CAM: SIM

**Case 2**

Input:

0 0 0 0

Output:

"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."

**Case 3**

Input:

1 9 8 7

Output:

"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"

**Case 4**

Input:

9 17 0 8

Output:

"IT'S ME"

**Case 5**

Input:

3 2 1

Output:

"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."