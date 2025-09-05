#dicionário pra fazer ordem alfabética
alfabeto = {"1" : "AÁÂaáâ", "2" : "Bb", "3" : "Ccç", "4" : "Dd", "5" : "EÉÊeéê", "6" : "Ff", "7" : "Gg", "8" : "Hh", "9" : "IÍÎiíî", "10" : "Jj",
            "11" : "Kk", "12" : "Ll", "13" : "Mm", "14" : "Nn", "15" : "OÓÔoóô", "16": "Pp", "17": "Qq", "18": "Rr", "19": "Ss", "20": "Tt", "21": "UÚÛuúû",
            "22": "Vv", "23": "Ww", "24": "Xx", "25": "Yy", "26": "Zz"}

#função pra fazer ordem alfabética
def ordem_alfabetica(alfabeto, nome_atual, nome_prox):

    if len(nome_atual) > 0:
        atual_agora = nome_atual[0]
        resto_agora = nome_atual[1:]
    else:
        return True

    if len(nome_prox) > 0:
        atual_prox = nome_prox[0]
        resto_prox = nome_prox[1:]
    else:
        return False

    for chave in alfabeto:
        if atual_agora in alfabeto[chave]:
            chave_r = int(chave)
        if atual_prox in alfabeto[chave]:
            chave_t = int(chave)
        
    if chave_r == chave_t:
        return ordem_alfabetica(alfabeto, resto_agora, resto_prox)
    elif chave_r > chave_t:
        return True
    elif chave_t > chave_r:
        return False
    
#função pra caso sport e santa forem pra final
def titulo(ficaram, ranking):
    melhor_time = ""
    ind_melhor = 6

    for chave in ficaram:
        nome = ficaram[chave][0]
        for ind in range(len(ranking)):
            if ranking[ind][0] == nome:

                if melhor_time == "" or ind < ind_melhor:
                    melhor_time = nome
                    ind_melhor = ind
                    
    return melhor_time

#função pra definir finalista e quem ficou pra trás
def atualizar(finalistas, ficaram, referencia, passou, ficou):
    posf, poss = 0, 0
    if posf in finalistas:
        posf += 1
    if poss in ficaram:
        poss += 1
    finalistas[posf], ficaram[poss] = referencia[passou], referencia[ficou]
    return finalistas, ficaram

#função para os jogos da fase final
def fase_final(gol, ind1, ind2, referencia, artilheiros, finalistas, ficaram, semi):
    if semi:
        print("Vai começar o confronto, quem será que vence?")

    #resetar gols
    referencia[ind1] = (referencia[ind1][0], 0)
    referencia[ind2] = (referencia[ind2][0], 0)

    while gol != "FIM":
        #receber input
        gol = input()
        if gol != "FIM":
            dados = gol.split(" - ")
            jogador = dados[0]
            equipe = dados[1]
            print(f"Gol do {equipe}, {jogador} é o nome da emoção")

            #atualizar dados dos pnts dos times
            if equipe == referencia[ind1][0]:
                referencia[ind1] = (referencia[ind1][0], referencia[ind1][1] + 1)
            elif equipe == referencia[ind2][0]:
                referencia[ind2] = (referencia[ind2][0], referencia[ind2][1] + 1)

            #atualizar dados dos artilheiros
            if artilheiros == {}:
                artilheiros[0] = {"jogador" : jogador, "pnt" : 1, "equipe" : equipe}
            else:
                apareceu = False
                for ind in artilheiros:
                    if jogador == artilheiros[ind]["jogador"] and equipe == artilheiros[ind]["equipe"] and not apareceu:
                        artilheiros[ind]["pnt"] += 1
                        apareceu = True

                if not apareceu:
                    nova_pos = len(artilheiros)
                    artilheiros[nova_pos] = {"jogador": jogador, "pnt": 1, "equipe": equipe}

    if gol == "FIM":
        if referencia[ind2][1] > referencia[ind1][1]:
            vencedor, gols_v = referencia[ind2][0], referencia[ind2][1]
            perdedor, gols_p = referencia[ind1][0], referencia[ind1][1]

            if semi:
                finalistas, ficaram = atualizar(finalistas, ficaram, referencia, ind2, ind1)

        else:
            vencedor, gols_v = referencia[ind1][0], referencia[ind1][1]
            perdedor, gols_p = referencia[ind2][0], referencia[ind2][1]

            if semi:
                finalistas, ficaram = atualizar(finalistas, ficaram, referencia, ind1, ind2)
        
        print("Fim de jogo.")
        print(f"Placar: {vencedor} {gols_v} X {gols_p} {perdedor}")

        if semi:
            if referencia[ind1][1] == referencia[ind2][1]:
                print(f"O {vencedor} passa para a final após vencer nos pênaltis, será que vai ser campeão?")
            else:
                print(f"O {vencedor} venceu e foi para a final, será que vai ser campeão?")
            return artilheiros, finalistas, ficaram
        else:
            return artilheiros, vencedor, perdedor

#função pra controlar o número de times por região
def checar_estado(estado, estados, times, clube):
    aceito = False
    for regiao in estados:
        if estado in estados[regiao]:

            contador = 0
            for t in times[regiao]:
                contador += 1

            if contador < 2:
                aceito = True
                times[regiao][contador] = (clube, estado, 0, 0, 0) #em ordem, pnts, gols feitos, gols sofridos
            else:
                print(f"Cota para a região {regiao} atingida. Por favor, insira um clube de outro estado, de outra região.")
            return times, aceito

#dicionário pra controlar o número de times por região
estados = {"Sudeste" : ("RJ", "SP", "ES", "MG"), "Sul" : ("RS", "SC", "PR"),
           "Nordeste" : ("PE", "BA", "CE", "MA", "PI", "SE", "RN", "AL", "PB")}

#dicionário pra armazenar os times
times = {"Sudeste" : {}, "Sul" : {}, "Nordeste" : {}}

#valores apenas iniciais pra começar o loop
clube = "temp"
qtd_times = 0

#receber clubes e seus estados
while clube != "FIM" and qtd_times < 6:
    clube = input()

    if clube != "FIM":
        estado = input()
        times, aceito = checar_estado(estado, estados, times, clube)
        if aceito:
            qtd_times += 1

if qtd_times != 6:
    print(f"Ai não dá, com {qtd_times} somente não dá para fazer um campeonato, essa ideia de Copa União foi um fiasco mesmo, #VOLTACBF")

else:
    #receber placares de jogos - FASE DE LIGA
    for jogo in range(15):
        placar = input()
        dados = placar.split(" ")

        ind_x = dados.index("X")
        time1 = " ".join(dados[:(ind_x - 1)])
        gols1 = int(dados[ind_x - 1])
        time2 = " ".join(dados[(ind_x + 2):])
        gols2 = int(dados[ind_x + 1])

        #checar os pontos ganhos
        if gols1 > gols2:
            pnt1, pnt2 = 3, 0
        elif gols2 > gols1:
            pnt1, pnt2 = 0, 3
        else:
            pnt1, pnt2 = 1, 1

        #atualizar os pontos e gols
        for regiao in times:
            for ind in times[regiao]:
                time = times[regiao][ind]
                nome = time[0]

                if nome == time1:
                    times[regiao][ind] = (nome, time[1], time[2] + pnt1, time[3] + gols1, time[4] + gols2)
                elif nome == time2:
                    times[regiao][ind] = (nome, time[1], time[2] + pnt2, time[3] + gols2, time[4] + gols1)

    #se livrar das regiões pra criar o ranking dos seis
    ranking = {}
    posicao = 0
    for regiao in times:
        for ind in times[regiao]:
            ranking[posicao] = times[regiao][ind]
            posicao += 1
            
    #ajeitando o ranking pra virar do melhor pro pior
    for atual in range(6):
        for proximo in range(atual + 1, 6):
            time_atual = ranking[atual]
            time_proximo = ranking[proximo]

            pnt_atual = time_atual[2]
            pnt_proximo = time_proximo[2]

            saldo_atual = time_atual[3] - time_atual[4]
            saldo_proximo = time_proximo[3] - time_proximo[4]

            if (pnt_proximo > pnt_atual) or (pnt_proximo == pnt_atual and saldo_proximo > saldo_atual):
                temp = ranking[atual]
                ranking[atual] = ranking[proximo]
                ranking[proximo] = temp

    #printar o ranking dos quatro primeiros
    for ind in range(6):
        print(f"{ranking[ind][0]} - {ranking[ind][2]} pontos")

    #printar a semifinal
    print("Os confrontos foram definidos:")
    print(f"{ranking[0][0]} X {ranking[3][0]}")
    print(f"{ranking[1][0]} X {ranking[2][0]}")

    #receber os inputs de gols da semifinal
    gol = "temp"
    semi = True
    artilheiros = {}
    finalistas = {}
    ficaram = {}

    #semifinal
    ind1, ind2, referencia = 0, 3, ranking   #primeiro jogo da semifinal - time1 x time4
    artilheiros, finalistas, ficaram = fase_final(gol, ind1, ind2, referencia, artilheiros, finalistas, ficaram, semi)
    ind1, ind2, referencia = 1, 2, ranking   #segundo jogo da semifinal - time2 x time3
    artilheiros, finalistas, ficaram = fase_final(gol, ind1, ind2, referencia, artilheiros, finalistas, ficaram, semi)

    #final
    gol = "temp"
    semi = False
    ind1, ind2, referencia = 0, 1, finalistas
    print("Vai começar a grande decisão, quem será o campeão brasileiro de 1987?")
    artilheiros, vencedor, perdedor = fase_final(gol, ind1, ind2, referencia, artilheiros, finalistas, ficaram, semi)

    #caso de troca de título
    if vencedor == "Sport" or vencedor == "Santa Cruz":
        if vencedor == "Sport":
            print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
        
        elif vencedor == "Santa Cruz":
            print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")

        #trocar o campeão
        if perdedor != "Sport" and perdedor != "Santa Cruz":
            vencedor = perdedor

        else:
            if perdedor == "Sport":
                print("Quem deixou o Sport participar, a Copa União só permite clubes grandes de participarem, tirem ele daqui que do jeito que eles são é capaz de irem no tribunal pedir o reconhecimento do 'Brasileiro de Questão de IP'")
            
            elif perdedor == "Santa Cruz":
                print("O terror do Nordeste agradece o reconhecimento, porém recusa o titulo, diferente do seu rival ele prefere ganhar o título em campo, e não em imaginação")

            vencedor = titulo(ficaram, ranking)
            if vencedor == "Sport" or vencedor == "Santa Cruz":

                for chave in ficaram:
                    candidato = ficaram[chave][0]

                    if candidato != vencedor and candidato != "Sport" and candidato != "Santa Cruz":
                        vencedor = candidato

    #outros prints do campeão
    if vencedor == "Flamengo":
        print("Em 1987, o Flamengo é o campeão inquestionável! Conquistou na bola e com o reconhecimento merecido. Qualquer outra conversa é história para boi dormir.")
    else:
        print(f"E o campeão do real Campeonato Brasileiro de 1987 foi o {vencedor}, ouvi dizer que a CBF tava querendo fazer um outro campeonato chamado módulo amarelo, ainda bem que todo mundo entendeu que aquilo é somente uma serie B")

    #ranking dos artilheiros
    if len(artilheiros) == 0:
        print("Esse ano o nivel foi fraco, não tivemos um artilheiro")

    else:
        #ordenar os artilheiros
        empate = False
        for atual in range(len(artilheiros)):
            for proximo in range(atual + 1, len(artilheiros)):
                j_atual = artilheiros[atual]
                j_proximo = artilheiros[proximo]

                pnt_atual = j_atual["pnt"]
                pnt_proximo = j_proximo["pnt"]

                if pnt_proximo > pnt_atual:
                    temp = artilheiros[atual]
                    artilheiros[atual] = artilheiros[proximo]
                    artilheiros[proximo] = temp

                elif pnt_proximo == pnt_atual:
                    nome_atual = j_atual["jogador"]
                    nome_prox = j_proximo["jogador"]

                    if nome_atual == nome_prox:
                        empate = True
                        troca = False
                    else:
                        troca = ordem_alfabetica(alfabeto, nome_atual, nome_prox)

                    if troca:
                        temp = artilheiros[atual]
                        artilheiros[atual] = artilheiros[proximo]
                        artilheiros[proximo] = temp
       
        #prints do artilheiro
        if empate and artilheiros[0]["jogador"] == artilheiros[1]["jogador"]:
            print("Esse ano o nivel foi fraco, não tivemos um artilheiro")

        elif artilheiros[0]["equipe"] == vencedor:
            print(f"{artilheiros[0]['jogador']} garantiu o título do campeonato e a artilharia, que ano feliz para ele")
        
        else:
            print(f"Apesar de não ter sido campeão, pelo menos {artilheiros[0]['jogador']} foi o artilheiro, a culpa não foi dele")