#inputs
j1 = input()
j2 = input()

#print especial
if j1 == "Luis" or j1 == "Lavoisier" or j1 == "Joab" or j1 == "Renan":
    if j2 == "Luis" or j2 == "Lavoisier" or j2 == "Joab" or j2 == "Renan":
        print("Essa partida vai ser épica! O jogo vai ser emocionante!")

#declaração de variáveis
n_sets = int(input())
numero_sets = n_sets
n = 0
ganhador_rodada = ""
pntfinal_1 = 0
pntfinal_2 = 0

#definição do nível
nivel = input()
reb_atual = 0
if nivel == "aprendizes":
    reb_max = 1
elif nivel == "básicos":
    reb_max = 2
elif nivel == "amostradinhos":
    reb_max = 3

#loop dos sets
while n_sets > 0:
    pnt1 = 0
    pnt2 = 0
    jogo = True
    n += 1
    sacador = j1
    print(f"Iniciando o {n}º set")

    #loop de cada partida
    while jogo:
        reb_atual = 0
        acao = input()
        if acao == "saque":
            print(f"O saque é de {sacador}")
            e1 = input()
            e2 = input()
            if e1 == "SA" and e2 == "AO":
                print("Um saque PERFEITO!!")
                acao = input()
                if acao == "rebatida":
                    acao_reb = input()
                    while acao_reb == "oponente rebateu" and reb_atual <= reb_max:
                        troca_j = j1
                        j1 = j2
                        j2 = troca_j
                        troca_p = pnt1
                        pnt1 = pnt2
                        pnt2 = troca_p   
                        reb_atual += 1
                        if reb_atual >= reb_max:
                            v1 = int(input())
                            v2 = int(input())
                            if v1 > v2:
                                pnt2 += 1
                                ganhador_rodada = j2
                            elif v2 > v1:
                                pnt1 += 1
                                ganhador_rodada = j1
                            acao_reb = ""
                        else:
                            acao_reb = input()
                    if acao_reb == f"{j2} deixou a bola cair":
                        pnt1 += 1
                        ganhador_rodada = j1
                    elif acao_reb == f"{j1} deixou a bola cair":
                        pnt2 += 1
                        ganhador_rodada = j2
            elif e1 == "SA" and e2 == "SA":
                pnt2 += 1
                print(f"{j1}, a bola quicou duas vezes na sua própria área! Que saque feio foi esse??")
                ganhador_rodada = j2
                troca_j = j1
                j1 = j2
                j2 = troca_j
                troca_p = pnt1
                pnt1 = pnt2
                pnt2 = troca_p
            elif e1 == "AO" and e2 == "AO":
                pnt2 += 1
                print(f"Boa, {j1}! Deu ponto de graça pro oponente!! Agora quem saca é {j2}")
                ganhador_rodada = j2
                troca_j = j1
                j1 = j2
                j2 = troca_j
                troca_p = pnt1
                pnt1 = pnt2
                pnt2 = troca_p
            elif e1 == "REDE" or e2 == "REDE":
                pnt2 += 1
                print("Vish, ainda bateu na rede")
                ganhador_rodada = j2
                troca_j = j1
                j1 = j2
                j2 = troca_j
                troca_p = pnt1
                pnt1 = pnt2
                pnt2 = troca_p
            if ganhador_rodada == j1:
                sacador = j1
            elif ganhador_rodada == j2:
                sacador = j2

        if (pnt1 >= 3 and pnt1 >= (pnt2 + 2)) or (pnt2 >= 3 and pnt2 >= (pnt1 + 2)):
            jogo = False

    pntfinal_1 += pnt1
    pntfinal_2 += pnt2
    n_sets -= 1

#definição do vencedor e print final
vencedor = ""
if pntfinal_1 > pntfinal_2:
    vencedor = j1
elif pntfinal_2 > pntfinal_1:
    vencedor = j2

print(f"Depois de {numero_sets} set(s) vibrante(s), o grande vencedor é {vencedor}!!\nFim do jogo!")