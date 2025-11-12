# Aprimorando a Build
*Nível: Médio*

Em um belo dia, César estava jogando Elden Ring no seu tempo livre, derrotando os inimigos e chefões durante seu caminho (morrendo de vez em quando, é claro).

Contudo, sua alegria se transformou em estresse após chegar em um dos chefões mais difíceis dos jogos Soulslike, a Malenia, Lâmina de Miquella.

Completamente humilhado por ela, César decide que estava na hora de rever seu equipamento e mudar a sua build. Com muitas armas coletadas durante sua jornada no jogo, ele fica indeciso com quais armas aprimorar e quais aprimoramentos deve fazer. Com isso em mente, César pede a você, estudante de IP, para construir um programa que ajude ele a prever como suas armas ficarão após os aprimoramentos, informando seu poder base e sua afinidade durante a análise.

# Entendendo os Aprimoramentos

Nos jogos da franquia souls, existem duas formas principais de aprimorar uma arma:

**Aumentando seu nível de forja**
**Aumentando o nível do de um atributo que coincida com os atributos da arma** (Ou seja, se a arma X possui o atributo força e eu aumento o nível força do meu personagem, o poder da arma aumenta).
Cada atributo upado aumenta o poder geral da arma em 1 ponto.
Sabendo disso, em Elden Ring, existem 5 atributos principais que podem ser upados:

Força - representado pela letra S
Destreza - representado pela letra D
Inteligência - representado pela letra I
Fé - representado pela letra F
Arcano - representado pela letra A
Além disso, as armas possuem alguma afinidade que concedem atributos extras para arma, ou seja, caso uma arma não tenha o atributo força mas seja do tipo fogo, essa arma passará a ter o atributo força.

Aqui estão as possíveis afinidades que uma arma pode ter, junto com o seu atributo extra:

Fogo - Força
Físico - Destreza
Mágico - Inteligência
Dourado - Fé
Oculto - Arcano

OBS: As afinidades extras das armas acumulam com a afinidade padrão da arma, ou seja, caso uma arma possua destreza como o atributo e sua afinidade seja físico, quando o atributo aumentado for destreza, ao invés de aumentar a força total em 1 ponto, irá aumentar em 2 pontos!

Por fim, as armas podem ser de dois tipos:

Normal - Podem ser forjadas por apenas por pedras de forja, representadas pelo sinal “+”. Aumenta o poder da arma em 3 pontos
Especial - Podem ser forjadas apenas por pedras sombrias, representadas pelo sinal “-”. Aumenta o poder da arma em 5 pontos

# Algumas observações

É obrigatório utilizar uma função recursiva para realizar os aprimoramentos das armas.

Nessa mesma função recursiva, você deverá percorrer a lista de aprimoramentos sem usar loops (for e while). Essa restrição se aplica apenas na lista de aprimoramentos, ou seja, você pode, como deve, usar loops para outras funcionalidades, como ler entradas, realizar prints, etc., exceto nessa lista em específico.

Está liberado o uso do comando eval().
Está liberado o uso do comando isistance().

# Input

Primeiramente, você receberá, até receber a entrada “finalizar”, os dados das armas que você irá aprimorar:

nome - tipo - força - afinidade_atual - atributo1 - atributo2 - … atributoN - finalizar

OBS: Não existirá atributo que não esteja nos 5 principais e nem existirá uma arma com atributos repetidos

Após isso, para cada arma recebida, você receberá uma lista que contém os aprimoramentos feitos por César, você deverá percorrer essa lista e com base nos elementos contidos, alterar as propriedades da arma sendo aprimorada:

[’X’, ‘Y’, ‘Z’,….]

Os seguintes elementos podem estar na lista:

Caracteres de atributos (S, D, I, F, A)
Caracteres de forja (+ ou -)
Outra lista, representando que a arma mudou de afinidade
Caractere especial R, representa reversão
Qualquer letra que não esteja em nenhum desses três casos, representa um outro atributo que está atrelado ao personagem e não terá efeito nenhum na arma
Caso especial: Mudança de afinidade
Quando a lista recebida possui outra lista contida nela, isso significa que a arma muda de afinidade. Isso significa que a afinidade atual da arma perde o atributo extra da afinidade antiga e ganha o atributo extra da afinidade nova.

A mudança de afinidade é baseada na afinidade atual da arma e segue a seguinte sequência:

Físico → Mágico → Fogo → Dourado → Oculto → Físico → Mágico…

# Observações:

Observação importante: a nova afinidade é sempre determinada com base na afinidade atual da arma no momento da mudança. Ou seja, a arma avança um passo nessa sequência circular, independentemente de qual tenha sido sua afinidade inicial. Por exemplo: Se a arma estiver com afinidade fogo, ela mudará para dourado e se estiver com oculto, mudará para físico.
E assim por diante.

O primeiro elemento nunca será uma sublista.
A arma pode ter N mudança de afinidades.
Caso uma arma seja aprimorada com o atributo extra de uma afinidade, o poder total da arma não é reduzido, apenas seu atributo extra é alterado.
Exemplo: caso uma arma tenha sido aprimorada com o atributo extra mágico (ou seja, inteligência) e depois mude a afinidade para fogo (o atributo extra agora é força), o poder extra adquirido pelo atributo inteligência NÃO É perdido.

# Caso especial: Reversão

César, de vez em quando, é meio indeciso quanto à build que vai fazer e vai pedir, em algumas situações, para reverter os aprimoramentos feitos dentro da sublista atual (ou seja, da mudança de afinidade em curso).

Exemplo: [’X’, ’Y’, [’X’, ’X’, ’R’], ’Z’]

Aqui, ao encontrar o caractere R na sublista, você deve desfazer os aprimoramentos feitos nela, restaurando o estado da arma antes dela, e continuar para 'Z'.
Observações:

O R aparecerá apenas dentro de sublistas.

Essas sublistas podem conter nenhum, um ou vários comandos antes do R.

Mesmo uma sublista como ['R'] é válida — nesse caso, nenhum aprimoramento é feito e a arma apenas volta ao estado anterior.

Sublistas com R podem ocorrer em qualquer profundidade, inclusive dentro de outras sublistas.

# Output

Antes do aprimoramento
Antes de tudo, seu programa deve printar as seguintes mensagens:

"Não aguento mais morrer para a Malenia, Blade of Miquella..."

"Vou refazer minha build!”

Em seguida, faça uma quebra de linha após essa última mensagem.

Durante o aprimoramento
Enquanto estiver aprimorando uma arma, caso ocorra uma reversão, seu programa deve printar uma mensagem indicando que houve uma reversão, além do poder atual da arma, antes da reversão, junto com o poder antigo da arma, após a reversão, ambas na mesma linha, e também, para qual afinidade a arma voltou:

"Hmm, não acho que isso vai funcionar..."

“{nome_arma}: {poder_antesR} -> {poder_depoisR}”

“Afinidade revertida para {afinidade_depoisR}”

Após o aprimoramento
Após uma arma ser aprimorada, imprima:

“{nome_arma} aprimorado!”

Quando todas as armas forem aprimoradas, você deverá imprimir as informações de cada arma da seguinte forma:

Primeiramente, imprima:
"Inventário:"

Após isso, para cada arma, imprima o nome da arma, junto com seu poder e sua afinidade atual:
“- {nome_arma}: {poder_arma}”

“- afinidade: {afinidade_arma}”

Se a afinidade da arma for fogo, imprima embaixo da afinidade da arma:

“Fogo... é uma das fraquezas da Malenia!!!”

Se a afinidade da arma for dourada, de maneira similar, imprima:

“É, não acho que uma arma de fé vá me ajudar muito...”

Mensagem final
Por fim, faça uma quebra de linha após esses prints e em seguida, printe a mensagem final, que são três possíveis:

Se existir pelo menos uma arma de fogo e a quantidade desse tipo for maior que todas as outras, imprima:
“Muitas armas de fogo, ela não vai ter chance!”

De maneira similar, só que com armas douradas, imprima o seguinte:
“Acho que vou ter que refazer meus aprimoramentos...”

Caso não seja nenhum desses dois casos — incluindo empates —, imprima:
“Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!”

# Examples

**Case: 1**

Input

garras - normal - 110 - físico - destreza - força
reduvia - especial - 90 - oculto - destreza - arcano
finalizar
['D', 'S', 'S', 'A', 'I', ['F', 'D', 'I', 'D']]
['V', 'A', 'A', '+', ['-', '-', 'F', 'S']]

Output

Não aguento mais morrer para a Malenia, Blade of Miquella...
Vou refazer minha build!

garras aprimorado!
reduvia aprimorado!
Inventário:
\- garras: 117
\- afinidade: mágico
\- reduvia: 104
\- afinidade: físico

Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!

**Case: 2**

Input

cão de caça - especial - 140 - físico - força - destreza
cajado de meteorito - normal - 120 - mágico - inteligência
lâmina do maliketh - especial - 150 - dourado - fé - força
finalizar
['V', 'S', 'D', 'D', '-', ['D', '-', 'D', 'S', 'R'], 'S']
['I', '+', '-', 'I', 'I', ['I', 'S', 'D', ['F', 'F', '-']]]
['F', 'S', 'S', '-', '-', 'F', 'S', 'F']

Output

Não aguento mais morrer para a Malenia, Blade of Miquella...
Vou refazer minha build!

Hmm, não acho que isso vai funcionar...
cão de caça: 158 -> 150
Afinidade revertida para físico
cão de caça aprimorado!
cajado de meteorito aprimorado!
lâmina do maliketh aprimorado!
Inventário:
\- cão de caça: 151
\- afinidade: físico
\- cajado de meteorito: 133
\- afinidade: dourado
É, não acho que uma arma de fé vá me ajudar muito...
\- lâmina do maliketh: 169
\- afinidade: dourado
É, não acho que uma arma de fé vá me ajudar muito...

Acho que vou ter que refazer meus aprimoramentos...
