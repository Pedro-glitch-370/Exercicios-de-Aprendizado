#função para os tipos de ataque
def atacar(atacante, nome_atacante, defensor, nome_defensor, tipo, eh_blue):
    
    #ataque especial e seu cooldown
    if tipo == "especial":
        if atacante["cooldown"] > 0:
            print(f"Sistema: {nome_atacante} tenta usar {atacante['especial'][0]}, mas falha!")
            print(f"Sistema: {atacante['especial'][0]} estará disponível em {atacante['cooldown']} turnos")
            return
        
        dano = int(atacante["especial"][1] * atacante["buff_especial"])

        if eh_blue:
            dano = int(dano * 1.05)

        defensor["HP"] -= dano
        atacante["cooldown"] = 3

        #obs: max utilizado apenas para encurtar o código (serve para impedir que a vida fique negativa)
        if eh_blue:
            print(f"Sistema: {nome_atacante} usa {atacante['especial'][0]}! É super efetivo!! {nome_defensor} agora está com {max(defensor['HP'], 0)} de vida!")
        else:
            print(f"Sistema: {nome_atacante} usa {atacante['especial'][0]}! {nome_defensor} está com {max(defensor['HP'], 0)} de vida!")

    #ataque normal
    elif tipo == "normal":
        dano = int(atacante["normal"][1] * atacante["buff_normal"])

        if eh_blue:
            dano = int(dano * 1.05)

        defensor["HP"] -= dano
        print(f"Sistema: {nome_atacante} usa {atacante['normal'][0]}! {nome_defensor} está com {max(defensor['HP'], 0)} de vida!")

    #status
    elif tipo == "status":
        efeito = atacante["status"][1]

        if efeito == "buff_especial":
            atacante["buff_especial"] *= 1.15
        elif efeito == "debuff_normal":
            defensor["buff_normal"] *= 0.85
        elif efeito == "debuff_todos":
            defensor["buff_normal"] *= 0.90
            defensor["buff_especial"] *= 0.90

        print(f"Sistema: {nome_atacante} usa {atacante['status'][0]}!")

#prints iniciais
print("=========== POKÉMON RED & BLUE - PYTHON VERSION ===========")
print('Professor Oak: "Qual inicial você vai escolher?"')

#dicionários com dados dos pokémons
pokemons = {
    "Venusaur": {
        "HP": 364,
        "Velocidade": 80,
        "normal": ["Razor Leaf", 78],
        "especial": ["Solar Beam", 94],
        "status": ["Growth", "buff_especial"],
        "buff_normal": 1.0,
        "buff_especial": 1.0,
        "cooldown": 0
    },
    "Charizard": {
        "HP": 360,
        "Velocidade": 100,
        "normal": ["Fire Spin", 80],
        "especial": ["Fire Blast", 98],
        "status": ["Growl", "debuff_normal"],
        "buff_normal": 1.0,
        "buff_especial": 1.0,
        "cooldown": 0
    },
    "Blastoise": {
        "HP": 362,
        "Velocidade": 78,
        "normal": ["Water Pulse", 79],
        "especial": ["Hydro Pump", 81],
        "status": ["Withdrawn", "debuff_todos"],
        "buff_normal": 1.0,
        "buff_especial": 1.0,
        "cooldown": 0
    }
}

#escolha do inicial
escolhido = False
while not escolhido:
    inicial = input()
    if inicial == "Bulbasaur":
        pkn_red = "Venusaur"
        pkn_blue = "Charizard"
        escolhido = True
    elif inicial == "Charmander":
        pkn_red = "Charizard"
        pkn_blue = "Blastoise"
        escolhido = True
    elif inicial == "Squirtle":
        pkn_red = "Blastoise"
        pkn_blue = "Venusaur"
        escolhido = True
    else:
        print("Sistema: Entrada inválida. Tente novamente.")

print(f"Sistema: {inicial}, eu escolho você!\n")

print("=========== INDIGO PLATEAU - SALA DO CAMPEÃO ===========")
print('Blue: "Eu estava ansioso para te ver, Red! Meu rival precisa ser forte para me manter afiado!"')
print('Red: "..."')

#faz cada personagem assumir o dicionário do seu pokémon
red = pokemons[pkn_red]
blue = pokemons[pkn_blue] 

#verifica quem é o mais rápido
if red["Velocidade"] > blue["Velocidade"]:
    turno_red = True
else:
    turno_red = False

#loop da batalha
fim = False
while red["HP"] > 0 and blue["HP"] > 0 and not fim:
    if turno_red:
        atacante, nome_atacante = red, pkn_red
        defensor, nome_defensor = blue, pkn_blue
        eh_blue = False
    else:
        atacante, nome_atacante = blue, pkn_blue
        defensor, nome_defensor = red, pkn_red
        eh_blue = True

    #input do ataque
    espera = True
    while espera:
        tipo = input()
        if tipo in ["normal", "especial", "status"]:
            espera = False
        else:
            print("Sistema: Entrada inválida. Tente novamente.")

    #executa o ataque
    atacar(atacante, nome_atacante, defensor, nome_defensor, tipo, eh_blue)

    #reduz os cooldowns existentes
    if turno_red and red["cooldown"] > 0:
        red["cooldown"] -= 1
    if not turno_red and blue["cooldown"] > 0:
        blue["cooldown"] -= 1

    #checha se a batalha acabou
    if red["HP"] <= 0 or blue["HP"] <= 0:
        fim = True

    #alterna o turno
    if not fim:
        turno_red = not turno_red #troca independente da condição que estiver

#prints finais
print()
if red["HP"] > 0:
    print("=========== BATALHA ENCERRADA - TEMOS UM NOVO CAMPEÃO! ===========")
    print('Blue: "NÃO! Não pode ser! Você me derrotou?! Depois de todo o trabalho pra virar o campeão?! Isso não é justo!"')
    print('Red: "..."')
else:
    print("=========== BATALHA ENCERRADA - DERROTA DE RED ===========")
    print('Blue: "É isso aí! Eu sou incrível ou não sou?"')
    print('Red: "..."')