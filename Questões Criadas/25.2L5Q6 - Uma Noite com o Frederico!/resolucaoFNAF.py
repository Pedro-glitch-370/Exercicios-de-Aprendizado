def encontrar_melhor(d_bonnie, d_chica, d_freddy, d_foxy, hora_atual, energia_atual, goldenfreddy):
    #casos bases - IMPORTANTE DEIXAR NA ORDEM
    if energia_atual <= 0:
        return -1, None
    if hora_atual == 6:
        return energia_atual, [] 

    #variáveis de controle
    melhor_energia = -1
    melhor_sequencia = None

    #flags pra otimizar o processamento
    bonnie_ativo = d_bonnie != 0 and hora_atual in [0, 3]
    chica_ativa = d_chica != 0 and hora_atual in [1, 4]
    foxy_ativo = d_foxy != 0 and hora_atual == 4 and energia_atual > 25
    freddy_ativo = d_freddy != 0 and hora_atual == 5
    golden_ativo = goldenfreddy and hora_atual == 5

    #todas as ações possíveis   
    for p_esq in [0, 1]:
        for p_dir in [0, 1]:
            for luzes in [0, 1]:
                for cam in [0, 1]:

                    vale_checar = True

                    if bonnie_ativo and p_esq == 0 and not (luzes == 1 and cam == 0):
                        vale_checar = False
                    if chica_ativa and p_dir == 0 and cam == 0:
                        vale_checar = False
                    if foxy_ativo and p_esq == 0: 
                        vale_checar = False
                    if freddy_ativo and p_esq == 0 and p_dir == 0 and cam == 0:
                        vale_checar = False
                    if golden_ativo and cam == 0:
                        vale_checar = False

                    if vale_checar:
                        acao = [p_esq, p_dir, luzes, cam]
                        
                        #custo da ação
                        custo_base = (p_esq * 7) + (p_dir * 7) + (luzes * 5) + (cam * 9)
                        energia_depois = energia_atual - custo_base - 1
                        
                        if energia_depois > 0:
                            vai_jumpscare = False
                            consumo_frustrado = 0

                            #bonnie
                            if bonnie_ativo:
                                consumo_frustrado += 3 + (d_bonnie * 0.25)
                                if not ((p_esq == 1) or (luzes == 1 and cam == 0)):
                                    vai_jumpscare = True

                            #chica
                            if chica_ativa:
                                consumo_frustrado += 2 + (d_chica * 0.35)
                                if not ((p_dir == 1) or (cam == 1)):
                                    vai_jumpscare = True
                                
                            #foxy
                            if foxy_ativo:
                                consumo_frustrado += 5 + (d_foxy * 0.15)
                                if p_esq == 0:
                                    vai_jumpscare = True

                            #freddy
                            if freddy_ativo:
                                consumo_frustrado += 3 + (d_freddy * 0.35)
                                if cam == 0 and (p_esq == 0 or p_dir == 0):
                                    vai_jumpscare = True
                            
                            #golden freddy
                            if golden_ativo: 
                                consumo_frustrado += 10 + (d_freddy * 1.95)
                                if cam == 0:
                                    vai_jumpscare = True

                            if not vai_jumpscare:
                                #atualizar energia
                                nova_energia = energia_depois - consumo_frustrado
                                if nova_energia > 0:
                                    
                                    #chamada pra próxima hora
                                    energia_restante, sequencia_sub = encontrar_melhor(d_bonnie, d_chica, d_freddy, d_foxy, hora_atual + 1, nova_energia, goldenfreddy)
                                    
                                    #checar se é melhor caminho
                                    if energia_restante > melhor_energia:
                                        melhor_energia = energia_restante
                                        melhor_sequencia = [acao] + sequencia_sub

    #caso de sucesso
    return melhor_energia, melhor_sequencia

# ------------------------------------------------------------------------

def anagrama(d_bonnie, d_chica, d_freddy, d_foxy):
    tem_zero = False
    str_anagrama = ""
    validos = [str(d_bonnie), str(d_chica), str(d_freddy), str(d_foxy)]

    if str(d_bonnie) == "0":
        tem_zero = True
        validos.remove(str(d_bonnie))
    if str(d_chica) == "0":
        tem_zero = True
        validos.remove(str(d_chica))
    if str(d_freddy) == "0":
        tem_zero = True
        validos.remove(str(d_freddy))
    if str(d_foxy) == "0":
        tem_zero = True
        validos.remove(str(d_foxy))

    for valor in validos:
        str_anagrama += valor

    if sorted(str_anagrama) == sorted("1987"):
        if tem_zero:
            return [True, True]
        return [True, False]
    return [False, False]

# ------------------------------------------------------------------------

def mensagens(d_bonnie, d_chica, d_freddy, d_foxy):
    if d_freddy == 0 and d_chica == 0 and d_freddy == 0 and d_foxy == 0:
        print('"Uh, olá? Olá? Phone Guy falando. Não tem ninguém aqui..."')
    else:
        dados = anagrama(d_bonnie, d_chica, d_freddy, d_foxy)
        goldenfreddy = dados[0]
        itsme = dados[1]

        if itsme:
            print('"IT\'S ME"') #pequeno desafio com o ' na print
        else:
            energia_max, sequencia = encontrar_melhor(d_bonnie, d_chica, d_freddy, d_foxy, 0, energia_inicial, goldenfreddy)

            output = ["PE: ", "PD: ", "LZ: ", "CAM: "]
            horario = 0

            if energia_max > 0 and sequencia is not None:
                print(f'"Uh, olá? Ei, wow, dia sete, parabéns. E ainda com {energia_max:.2f}% de energia. Eu sabia que você conseguiria."')
                
                for hora in sequencia:           
                    print(f"0{horario}:00 AM -> ", end="")

                    decisoes = []
                    horario += 1
                    
                    #processar cada decisão
                    for i in range(4):
                        decisao = "NÃO" if hora[i] == 0 else "SIM"
                        decisoes.append(output[i] + decisao)

                    print(" | ".join(decisoes))
            else:
                print('"Uh, Phone Guy falando. Uh, não tem mais ninguém do outro lado, não é?"')

# ------------------------------------------------------------------------

#começo do código
invalido = False
energia_inicial = 100
dificuldades = input().split(" ")

if len(dificuldades) == 4:
    d0 = int(dificuldades[0])
    d1 = int(dificuldades[1])
    d2 = int(dificuldades[2])
    d3 = int(dificuldades[3])

    if d0 < 0 or d0 > 20:
        invalido = True
    if d1 < 0 or d1 > 20:
        invalido = True
    if d2 < 0 or d2 > 20:
        invalido = True
    if d3 < 0 or d3 > 20:
        invalido = True

    d_bonnie = d0
    d_chica = d1
    d_freddy = d2
    d_foxy = d3

else:
    invalido = True

if not invalido:
    mensagens(d_bonnie, d_chica, d_freddy, d_foxy)
else:
    print('"Uh, Phone Guy aqui. Os animatronics estão um pouco "sapecas" esta noite."')