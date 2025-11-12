quarteiroes = []

quadrado = int(input())

#cria cada linha de quarteirão
for linha in range(quadrado):
    entrada = input()
    dados = entrada.split(" ")
    quarteiroes.append(dados)

#declaração de variáveis
missao_cumprida = False
vem_electro = True
tres_dias = 0
restaurados = 0
dia = 1

comando = input()

while comando != "FIM":
    #pegar a posição atual do homem-aranha
    for l in range(len(quarteiroes)):
        for c in range(len(quarteiroes[l])):
            if quarteiroes[l][c] == "H":
                linha_aranha = l
                coluna_aranha = c

    #pegar a primeira quantidade de E
    contador1 = 0
    for l in range(len(quarteiroes)):
        for c in range(len(quarteiroes[l])):
            if quarteiroes[l][c] == "E":
                contador1 += 1

    #homem-aranha sai
    quarteiroes[linha_aranha][coluna_aranha] = "."
    
    #movimentos do homem-aranha
    if comando == "Cima":
        linha_aranha -= 1
    elif comando == "Baixo":
        linha_aranha += 1
    elif comando == "Esquerda":
        coluna_aranha -= 1
    elif comando == "Direita":
        coluna_aranha += 1

    #se aranha pode vir
    linha_proibida = False
    coluna_proibida = False
    if linha_aranha < 0 or linha_aranha > quadrado - 1:
        if comando == "Cima":
            linha_aranha += 1
            linha_proibida = True
        elif comando == "Baixo":
            linha_aranha -= 1
            linha_proibida = True
    elif coluna_aranha < 0 or coluna_aranha > quadrado - 1:
        if comando == "Esquerda":
            coluna_aranha += 1
            coluna_proibida = True
        elif comando == "Direita":
            coluna_aranha -= 1
            coluna_proibida = True
    elif quarteiroes[linha_aranha][coluna_aranha] == "X":
        if comando == "Cima":
            linha_aranha += 1
            linha_proibida = True
        elif comando == "Baixo":
            linha_aranha -= 1
            linha_proibida = True
        elif comando == "Esquerda":
            coluna_aranha += 1
            coluna_proibida = True
        elif comando == "Direita":
            coluna_aranha -= 1
            coluna_proibida = True
    
    #homem-aranha vem
    quarteiroes[linha_aranha][coluna_aranha] = "H"

    #pegar a segunda quantidade de E
    contador2 = 0
    for l in range(len(quarteiroes)):
        for c in range(len(quarteiroes[l])):
            if quarteiroes[l][c] == "E":
                contador2 += 1
 
    calculo = contador1 - contador2
    restaurados += calculo
    if calculo >= 1:
        missao_cumprida = True
    
    #três dias sem restaurados
    contadorE = 0
    if not missao_cumprida:
        tres_dias += 1
    else:
        tres_dias = 0
    if tres_dias == 3:
        for l in range(len(quarteiroes)):
            for c in range(len(quarteiroes[l])):
                if quarteiroes[l][c] == "E" and contadorE == 0:
                    quarteiroes[l][c] = "X"
                    contadorE = 1
            tres_dias = 0
    missao_cumprida = False

    #pegar a quantidade de destruidos
    contadorX = 0
    for l in range(len(quarteiroes)):
        for c in range(len(quarteiroes[l])):
            if quarteiroes[l][c] == "X":
                contadorX += 1

    print(f"Dia {dia}")

    #mapa dos quarteirões
    for l in range(quadrado):
        linha = []
        for c in range(quadrado):
            coluna = " ".join(quarteiroes[l][c])
            linha.append(coluna)
        print(" ".join(linha))
    
    #mensagens
    print(f"Posição atual do Homem-Aranha: ({linha_aranha}, {coluna_aranha})")

    print(f"Quarteirões restaurados: {restaurados} | Quarteirões destruídos: {contadorX}")

    if linha_proibida or coluna_proibida:
        print("Ai! O Miranha tentou passar, mas acabou se machucando. Tenha mais cuidado!")
    elif calculo == 1 and contador2 >= 0:
        print("O Miranha restaurou um quarteirão!")
    elif contador1 == contador2:
        print("O Electro está ganhando espaço!")

    print()

    dia += 1
    if dia == 8 and contador2 > 0:
        print("O Miranha não conseguiu restaurar a cidade a tempo, o Electro venceu!")
        comando = "FIM"
    elif restaurados > 0 and contador2 == 0:
        print("Missão cumprida! Nova York está segura e o Miranha faz tudo novamente!")
        comando = "FIM"
    else:
        comando = input()

    if comando == "FIM" and contador2 > 0:
        print("Ainda existem quarteirões corrompidos! O Miranha não pode ir embora agora!")