def procurar_caminho(linha_wolf, linha_cesar, coluna_wolf, coluna_cesar, qtd_mov, qtd_total, mapa, ja_passou, linhas, colunas, qtd_temp):

    #checar se alcançou cesar
    if linha_wolf == linha_cesar and coluna_wolf == coluna_cesar:
        qtd_total.append(qtd_mov)
        return qtd_total

    #checar se já passou pelo lugar
    if ja_passou[linha_wolf][coluna_wolf] == "W":
        return
    
    else:
        ja_passou[linha_wolf][coluna_wolf] = "W"

        if mapa[linha_wolf][coluna_wolf] == "2":

            #pulo pra cima
            if linha_wolf - 2 >= 0:
                prox_linha = linha_wolf - 2
                prox_coluna = coluna_wolf

                #o movimento propriamente dito
                if ja_passou[prox_linha][prox_coluna] != "W" and mapa[prox_linha][prox_coluna] != "0":
                    qtd_temp = qtd_mov + 1
                    copia = copiar_ja_passou(ja_passou)
                    procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)

            #pulo pra baixo
            if linha_wolf + 2 < linhas:
                prox_linha = linha_wolf + 2
                prox_coluna = coluna_wolf  

                if ja_passou[prox_linha][prox_coluna] != "W" and mapa[prox_linha][prox_coluna] != "0":
                    qtd_temp = qtd_mov + 1
                    copia = copiar_ja_passou(ja_passou)
                    procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
        
            #pulo pra esquerda
            if coluna_wolf - 2 >= 0:
                prox_linha = linha_wolf
                prox_coluna = coluna_wolf - 2

                if ja_passou[prox_linha][prox_coluna] != "W" and mapa[prox_linha][prox_coluna] != "0":
                    qtd_temp = qtd_mov + 1
                    copia = copiar_ja_passou(ja_passou)
                    procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)  

            #pulo pra direita
            if coluna_wolf + 2 < colunas:
                prox_linha = linha_wolf
                prox_coluna = coluna_wolf + 2

                if ja_passou[prox_linha][prox_coluna] != "W" and mapa[prox_linha][prox_coluna] != "0":
                    qtd_temp = qtd_mov + 1
                    copia = copiar_ja_passou(ja_passou)
                    procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)                        
        
        else:

            #andar pra cima
            if (linha_wolf - 1) >= 0:
                prox_linha = linha_wolf - 1
                prox_coluna = coluna_wolf

                if mapa[linha_wolf - 1][coluna_wolf] == "1" or mapa[linha_wolf - 1][coluna_wolf] == "2":
                    qtd_temp = qtd_mov + 1

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
                     
                elif mapa[linha_wolf - 1][coluna_wolf] == "3":
                    qtd_temp = qtd_mov + 3

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
            
            #andar pra baixo
            if (linha_wolf + 1) < linhas:
                prox_linha = linha_wolf + 1
                prox_coluna = coluna_wolf

                if mapa[linha_wolf + 1][coluna_wolf] == "1" or mapa[linha_wolf + 1][coluna_wolf] == "2":
                    qtd_temp = qtd_mov + 1

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
                
                elif mapa[linha_wolf + 1][coluna_wolf] == "3":
                    qtd_temp = qtd_mov + 3

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)

            #andar pra esquerda
            if (coluna_wolf - 1) >= 0:
                prox_linha = linha_wolf
                prox_coluna = coluna_wolf - 1

                if mapa[linha_wolf][coluna_wolf - 1] == "1" or mapa[linha_wolf][coluna_wolf - 1] == "2":
                    qtd_temp = qtd_mov + 1

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)

                elif mapa[linha_wolf][coluna_wolf - 1] == "3":
                    qtd_temp = qtd_mov + 3
                    
                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
            
            #andar pra direita
            if (coluna_wolf + 1) < colunas:
                prox_linha = linha_wolf
                prox_coluna = coluna_wolf + 1

                if mapa[linha_wolf][coluna_wolf + 1] == "1" or mapa[linha_wolf][coluna_wolf + 1] == "2":
                    qtd_temp = qtd_mov + 1

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)

                elif mapa[linha_wolf][coluna_wolf + 1] == "3":
                    qtd_temp = qtd_mov + 3

                    if ja_passou[prox_linha][prox_coluna] != "W":
                        copia = copiar_ja_passou(ja_passou)
                        procurar_caminho(prox_linha, linha_cesar, prox_coluna, coluna_cesar, qtd_temp, qtd_total, mapa, copia, linhas, colunas, qtd_temp)
    
    #caso não encontre cesar
    return qtd_total

#copiar o mapa de casas já passadas
def copiar_ja_passou(ja_passou):
    copia = []

    for l in range(len(ja_passou)):
        linha = []
        for c in range(len(ja_passou[l])):
            linha.append(ja_passou[l][c])
        copia.append(linha)

    return copia

linhas = int(input())
colunas = int(input())

#criar o mapa
mapa = []

for n in range(linhas):
    linha = input()
    dados_linha = linha.split(" ")
    mapa.append(dados_linha)

#criar mapa de casas já passadas
ja_passou = []

for i in range(linhas):
    linha = []
    for j in range(colunas):
        linha.append("?")
    ja_passou.append(linha)

#posições dos personagens
linha_wolf = 0
coluna_wolf = 0
linha_cesar = linhas - 1
coluna_cesar = colunas - 1

print("=== SEKIRO: O RESGATE DE CESAR ===")
print("Wolf deve resgatar CESAR!")

#análise dos caminhos
qtd_temp = 0
qtd_mov = 0
qtd_total = []
qtd_total = procurar_caminho(linha_wolf, linha_cesar, coluna_wolf, coluna_cesar, qtd_mov, qtd_total, mapa, ja_passou, linhas, colunas, qtd_temp)

if qtd_total == []:
    print("MORTE! Wolf não conseguiu resgatar Cesar... ele nunca saberá quem venceu Satoru Gojo ou Sukuna!")
else:
    contador = 0
    
    #pegar o menor caminho achado
    for caminho in qtd_total:
        if caminho == qtd_total[0] and contador == 0:
            menor = caminho
            contador += 1
        else:
            if caminho < menor:
                menor = caminho

    #prints finais
    print(f"SUCESSO! Wolf resgatou o Cesar em {menor} movimentos!")

    if menor <= 4:
        print("PERFEITO! Verdadeiro Shinobi! Cesar está ORGULHOSO!!")
    
    elif menor < 8:
        print("BOM! Caminho eficiente! Mas você quase decepcionou Cesar")

    else:
        print("Wolf chegou, mas pode melhorar... Cesar está decepcionado, quase morreu de tédio!")