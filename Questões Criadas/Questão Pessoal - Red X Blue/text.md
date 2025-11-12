OBS: A questão abaixo foi criada por mim mesmo para o processo de seleção da monitoria de Introdução à Programação, contribuindo para a minha aprovação ao fim do processo seletivo. O foco da questão é o uso de dicionários.

# Red X Blue - A Clássica Final do Universo Pokémon!!

Depois de inúmeras derrotas, resets e consoles jogados na parede, os mestres pokémons do CIn se revoltaram: perder para o campeão de Kanto, Blue, logo em seu último pokémon, já não era mais algo aceitável!

Para resolverem tal questão de vida e morte, decidiram contar com você, futuro campeão do mundo da programação, para construir um simulador da batalha final, em que poderiam treinar como Red, o personagem principal, e finalmente zerar o game!

# Input

No começo do primeiro jogo Pokémon, o rival Blue escolhe o seu inicial com base no inicial de Red, o personagem jogável. Portanto, a primeira linha de entrada do seu código deve receber o nome do pokémon inicial escolhido por Red.

Esse input definirá quais os pokémons, já evoluídos, irão compor a batalha:

Se o inicial for Bulbasaur, o pokémon de Red será Venusaur, enquanto o de Blue será Charizard.
Se o inicial for Charmander, o pokémon de Red será Charizard, enquanto o de Blue será Blastoise.
Se o inicial for Squirtle, o pokémon de Red será Blastoise, enquanto o de Blue será Venusaur.
Se o input dado não bater com nenhum dos três, peça o input novamente até que seja válido.
Cada um dos três pokémons jogáveis contém os atributos HP (vida), velocidade, ataque normal, ataque especial e ataque de status.

**Valores dos atributos de Venusaur:**

Possui 364 de HP e 80 de Velocidade.

Seu ataque normal é Razor Leaf (78 de dano) e seu ataque especial é Solar Beam (94 de dano).

Seu ataque de status é Growth, que aumenta 15% do dano especial do usuário.

**Valores dos atributos do Charizard:**

Possui 360 de HP e 100 de Velocidade.

Seu ataque normal é Fire Spin (80 de dano) e seu ataque especial é Fire Blast (98 de dano).

Seu ataque de status é Growl, que diminui 15% do dano básico do oponente.

**Valores dos atributos do Blastoise:**

Possui 362 de HP e 78 de Velocidade.

Seu ataque normal é Water Pulse (79 de dano) e seu ataque especial é Hydro Pump (81 de dano).

Seu ataque de status é Withdrawn, que diminui 10% dos danos normal e especial do oponente.

OBS1: É obrigatório o uso de dicionários para armazenar os dados dos pokémons.

OBS2: Devido ao pokémon de Blue sempre ter vantagem contra o de Red em relação à tipagem do pokémon, qualquer ataque de Blue que cause dano deve ser aumentado em 5%.

OBS3: Se um ataque especial for utilizado, o pokémon que o realizou precisará de dois turnos para recuperação e, somente a partir do terceiro turno, poderá utilizá-lo novamente. Caso outro ataque especial tente ser realizado nesse período, deve-se perder o turno e imprimir uma mensagem especial. Caso outro tipo de ataque seja feito nesse período, o ataque ocorrerá normalmente.

OBS4: Sempre arredonde os valores de ataques para baixo. Apesar disso, jamais deixe qualquer tipo de valor negativo, seja de ataque ou de vida.

Quanto à batalha, ela sempre se iniciará com o pokémon mais rápido, seguido pelo pokémon do oponente. Os ataques irão se alternar entre cada um dos combatentes até que um dos pokémons chegue a 0 de HP ou menos.

No turno de cada combatente, o programa deve pedir qual tipo de ataque o pokémon atual deverá fazer.

As entradas possíveis são **normal** (para ataque normal), **especial** (para ataque especial) e **status** (para ataques de status). Se a entrada recebida não for nenhuma das três, peça novamente até que seja recebida uma entrada válida.

Finalmente, se um dos pokémons for derrotado, o programa deve ser encerrado sob qualquer condição.

# Output

No começo do código, antes de receber o pokémon inicial de Red, printe, em linhas separadas:

=========== POKÉMON RED & BLUE - PYTHON VERSION ===========

Professor Oak: "Qual inicial você vai escolher?"

Após receber o input do pokémon inicial, printe:

Sistema: {inicial}, eu escolho você!

Porém, caso o input não seja válido, printe:

Sistema: Entrada inválida. Tente novamente.

Antes de começar a batalha, pule uma linha do output anterior e printe, em linhas separadas:

=========== INDIGO PLATEAU - SALA DO CAMPEÃO ===========

Blue: "Eu estava ansioso para te ver, Red! Meu rival precisa ser forte para me manter afiado!"

Red: "..."

Durante a batalha, se o ataque atual for de Blue e do tipo especial, printe:

Sistema: {pokemon_atacante} usa {ataque}! É super efetivo!! {pokemon_atacante} agora está com {HP} de vida!

No entanto, caso seja um ataque especial feito dentro do período de recuperação, printe em linhas separadas (independente de quem seja o atacante):

Sistema: {pokemon_atacante} tenta usar {ataque}, mas falha!

Sistema: {ataque_especial} estará disponível em {turnos_restantes} turnos!

Para qualquer outro caso de ataque danoso, printe:

Sistema: {pokemon_atacante} usa {ataque}! {pokemon_atacado} está com {HP} de vida!

Caso seja um ataque de status, printe apenas:

Sistema: {pokemon_atacante} usa {ataque}!

OBS: Caso a entrada seja inválida, printe a mesma mensagem de erro do input do inicial (”Sistema: Entrada inválida. Tente novamente.”).

Ao final da batalha, independente do resultado, pule uma linha do output anterior.

Caso Red seja o vencedor do combate, printe:

=========== BATALHA ENCERRADA - TEMOS UM NOVO CAMPEÃO! ===========

Blue: "NÃO! Não pode ser! Você me derrotou?! Depois de todo o trabalho pra virar o campeão?! Isso não é justo!"

Red: "..."

Caso contrário, se Blue for o vencedor, printe:

=========== BATALHA ENCERRADA - DERROTA DE RED ===========

Blue: "É isso aí! Eu sou incrível ou não sou?"

Red: "..."

OBS: Não existe casos de empate.

# Examples

**Case: 1**

Input

Charmander
normal
especial
normal
especial
normal
status
normal
especial
normal

Output

=========== POKÉMON RED & BLUE - PYTHON VERSION ===========
Professor Oak: "Qual inicial você vai escolher?"
Sistema: Charmander, eu escolho você!

=========== INDIGO PLATEAU - SALA DO CAMPEÃO ===========
Blue: "Eu estava ansioso para te ver, Red! Meu rival precisa ser forte para me manter afiado!"
Red: "..."
Sistema: Charizard usa Fire Spin! Blastoise está com 282 de vida!
Sistema: Blastoise usa Hydro Pump! É super efetivo!! Charizard agora está com 275 de vida!
Sistema: Charizard usa Fire Spin! Blastoise está com 202 de vida!
Sistema: Blastoise tenta usar Hydro Pump, mas falha!
Sistema: Hydro Pump estará disponível em 2 turnos
Sistema: Charizard usa Fire Spin! Blastoise está com 122 de vida!
Sistema: Blastoise usa Withdrawn!
Sistema: Charizard usa Fire Spin! Blastoise está com 50 de vida!
Sistema: Blastoise usa Hydro Pump! É super efetivo!! Charizard agora está com 190 de vida!
Sistema: Charizard usa Fire Spin! Blastoise está com 0 de vida!

=========== BATALHA ENCERRADA - TEMOS UM NOVO CAMPEÃO! ===========
Blue: "NÃO! Não pode ser! Você me derrotou?! Depois de todo o trabalho pra virar o campeão?! Isso não é justo!"
Red: "..."

**Case: 2**

Input

Bulbasaur
status
status
normal
status
status
especial
normal
status
status
status
normal
especial
normal
normal
especial

Output

=========== POKÉMON RED & BLUE - PYTHON VERSION ===========
Professor Oak: "Qual inicial você vai escolher?"
Sistema: Bulbasaur, eu escolho você!

=========== INDIGO PLATEAU - SALA DO CAMPEÃO ===========
Blue: "Eu estava ansioso para te ver, Red! Meu rival precisa ser forte para me manter afiado!"
Red: "..."
Sistema: Charizard usa Growl!
Sistema: Venusaur usa Growth!
Sistema: Charizard usa Fire Spin! Venusaur está com 280 de vida!
Sistema: Venusaur usa Growth!
Sistema: Charizard usa Growl!
Sistema: Venusaur usa Solar Beam! Charizard está com 236 de vida!
Sistema: Charizard usa Fire Spin! Venusaur está com 196 de vida!
Sistema: Venusaur usa Growth!
Sistema: Charizard usa Growl!
Sistema: Venusaur usa Growth!
Sistema: Charizard usa Fire Spin! Venusaur está com 112 de vida!
Sistema: Venusaur usa Solar Beam! Charizard está com 72 de vida!
Sistema: Charizard usa Fire Spin! Venusaur está com 28 de vida!
Sistema: Venusaur usa Razor Leaf! Charizard está com 25 de vida!
Sistema: Charizard usa Fire Blast! É super efetivo!! Venusaur agora está com 0 de vida!

=========== BATALHA ENCERRADA - DERROTA DE RED ===========
Blue: "É isso aí! Eu sou incrível ou não sou?"
Red: "..."

**Case: 3**

Input

squirtle
Squirtle
normal
normal
normal
status
status
normal
normal
normal
especia
especial
normal
normal

Output

=========== POKÉMON RED & BLUE - PYTHON VERSION ===========
Professor Oak: "Qual inicial você vai escolher?"
Sistema: Entrada inválida. Tente novamente.
Sistema: Squirtle, eu escolho você!

=========== INDIGO PLATEAU - SALA DO CAMPEÃO ===========
Blue: "Eu estava ansioso para te ver, Red! Meu rival precisa ser forte para me manter afiado!"
Red: "..."
Sistema: Venusaur usa Razor Leaf! Blastoise está com 281 de vida!
Sistema: Blastoise usa Water Pulse! Venusaur está com 285 de vida!
Sistema: Venusaur usa Razor Leaf! Blastoise está com 200 de vida!
Sistema: Blastoise usa Withdrawn!
Sistema: Venusaur usa Growth!
Sistema: Blastoise usa Water Pulse! Venusaur está com 206 de vida!
Sistema: Venusaur usa Razor Leaf! Blastoise está com 127 de vida!
Sistema: Blastoise usa Water Pulse! Venusaur está com 127 de vida!
Sistema: Entrada inválida. Tente novamente.
Sistema: Venusaur usa Solar Beam! É super efetivo!! Blastoise agora está com 26 de vida!
Sistema: Blastoise usa Water Pulse! Venusaur está com 48 de vida!
Sistema: Venusaur usa Razor Leaf! Blastoise está com 0 de vida!

=========== BATALHA ENCERRADA - DERROTA DE RED ===========
Blue: "É isso aí! Eu sou incrível ou não sou?"
Red: "..."
