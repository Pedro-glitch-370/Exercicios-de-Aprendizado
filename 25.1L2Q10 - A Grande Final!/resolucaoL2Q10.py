#print e input inicial
print("Bem amigos da Rede Globo, emoção no ar! Prepare o coração porque hoje é dia de decisão! É final de Copa do Mundo, mas não é futebol… é ping pong, meu amigo! A raquete vai cantar, a bolinha vai voar, e só um será campeão! Segura essa emoção porque vai começar!")
s1 = input()

#declaração de variáveis
sets_hugo = 0
sets_lin = 0
set_n = 1
jogador = ""
oponente = ""
vencedor_set = ""
tie_break = False
jogo = True

#loop de cada set
while jogo:
    print(f"Set {set_n}:")

    pnt_hugo = 0
    pnt_lin = 0
    j_aberto = True
    vai_2 = False

    if sets_hugo == 2 and sets_lin == 2:
        tie_break = True
        print("Agora é hora da decisão! Vamos para o tie-break, quem errar, perde tudo! É emoção até o fim!")
    
    #loop de cada ponto
    while j_aberto:
        a_atual = ""
        a_antes = ""

        if s1 == "hugo":
            jogador = "Hugo"
            oponente = "Lin"
        elif s1 == "lin":
            jogador = "Lin"
            oponente = "Hugo"

        acoes = input() + "-"

        #tipos de ações possíveis
        for acao in acoes:
            if acao != "-":
                a_atual += acao
            else:
                if a_atual == "erro":
                    if a_antes == "saque":
                        print(f"Uau, um ace! {oponente} solta o braço e deixa o adversário parado!")
                        if oponente == "Lin":
                            pnt_lin += 1 
                        elif oponente == "Hugo":
                            pnt_hugo += 1
                        print(f"Ponto para {oponente}!\nPlacar do {set_n} set : {pnt_hugo} x {pnt_lin}")
                    else:
                        print(f"{jogador} se estica, tenta a defesa, mas não alcança — ponto para o adversário.")
                        if oponente == "Lin":
                            pnt_lin += 1 
                        elif oponente == "Hugo":
                            pnt_hugo += 1
                        print(f"Ponto para {oponente}!\nPlacar do {set_n} set : {pnt_hugo} x {pnt_lin}")
                else:
                    if a_antes == "ataque":
                        if a_atual != "defesa":
                            print(f"{oponente} acelera com uma bola de ataque precisa, e o adversário não reage — ponto direto para o jogador!")
                            if oponente == "Lin":
                                pnt_lin += 1 
                            elif oponente == "Hugo":
                                pnt_hugo += 1                            
                            print(f"Ponto para {oponente}!\nPlacar do {set_n} set : {pnt_hugo} x {pnt_lin}")
                    elif a_antes == "defesa":
                        if a_atual == "defesa":
                            print(f"{jogador} tentou devolver uma bola de defesa, o que não é permitido — ponto para o adversário.")
                            if oponente == "Lin":
                                pnt_lin += 1 
                            elif oponente == "Hugo":
                                pnt_hugo += 1                            
                            print(f"Ponto para {oponente}!\nPlacar do {set_n} set : {pnt_hugo} x {pnt_lin}")
                    elif a_antes == "saque":
                        if a_atual == "ataque":
                            print(f"Uau, um ace! {oponente} solta o braço e deixa o adversário parado!")
                            if oponente == "Lin":
                                pnt_lin += 1 
                            elif oponente == "Hugo":
                                pnt_hugo += 1
                            print(f"Ponto para {oponente}!\nPlacar do {set_n} set : {pnt_hugo} x {pnt_lin}")
                troca = jogador
                jogador = oponente
                oponente = troca
                a_antes = a_atual
                a_atual = ""

        #final de set
        if not tie_break:
            if pnt_hugo == 4 and pnt_lin == 4:
                vai_2 = True
                print("O set está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva — é decisão na mesa!")
            if not vai_2:
                if pnt_hugo == 5 and pnt_lin >= 0:
                    j_aberto = False
                    vencedor_set = "Hugo"
                    sets_hugo += 1
                    if pnt_lin == 0:
                        print(f"Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {vencedor_set} passeia na mesa")
                    else:
                        print(f"E o set vai para {vencedor_set}!")
                elif pnt_lin == 5 and pnt_hugo >= 0:
                    j_aberto = False
                    vencedor_set = "Lin"
                    sets_lin += 1
                    if pnt_hugo == 0:
                        print(f"Fim de set! Domínio total: 5 a 0, sem chance para o adversário — {vencedor_set} passeia na mesa")
                    else:
                        print(f"E o set vai para {vencedor_set}!")
            else: #vai a 2
                if pnt_hugo >= 5 and pnt_hugo >= (pnt_lin + 2):
                    j_aberto = False
                    vencedor_set = "Hugo"
                    sets_hugo += 1
                    print(f"E o set vai para {vencedor_set}!")
                elif pnt_lin >= 5 and pnt_lin >= (pnt_hugo + 2):
                    j_aberto = False
                    vencedor_set = "Lin"
                    sets_lin += 1
                    print(f"E o set vai para {vencedor_set}!")
        else: #tie break sendo true
            if pnt_hugo == 6 and pnt_lin == 6:
                vai_2 = True
                print("O tie-break está pegando fogo e agora vai a 2! Quem fizer dois pontos seguidos leva, é a reta final da disputa! Quem será o grande campeão?")
            if not vai_2:
                if pnt_hugo == 7 and pnt_lin >= 0:
                    j_aberto = False
                    vencedor_set = "Hugo"
                    sets_hugo += 1
                    if pnt_lin == 0:
                        print(f"Fim de tie-break! {vencedor_set} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
                    else:
                        print(f"E o set vai para {vencedor_set}!\nPlacar do jogo: {sets_hugo} x {sets_lin}")
                elif pnt_lin == 7 and pnt_hugo >= 0:
                    j_aberto = False
                    vencedor_set = "Lin"
                    sets_lin += 1
                    if pnt_hugo == 0:
                        print(f"Fim de tie-break! {vencedor_set} arrasa com um 7 a 0 impressionante, sem dar chances para o adversário! Vitória esmagadora!")
                    else:
                        print(f"E o set vai para {vencedor_set}!")
            else: #vai a 2
                if pnt_hugo >= 7 and pnt_hugo >= (pnt_lin + 2):
                    j_aberto = False
                    vencedor_set = "Hugo"
                    sets_hugo += 1
                    print(f"E o set vai para {vencedor_set}!")
                elif pnt_lin >= 7 and pnt_lin >= (pnt_hugo + 2):
                    j_aberto = False
                    vencedor_set = "Lin"
                    sets_lin += 1
                    print(f"E o set vai para {vencedor_set}!")
        if tie_break:
            if (pnt_hugo + pnt_lin) % 2 == 1: #ímpar (rodadas 1, 3, 5...)
                if s1 == "hugo":
                    s1 = "lin"
                elif s1 == "lin":
                    s1 = "hugo"
    print(f"Placar do jogo: {sets_hugo} x {sets_lin}")

    #final do jogo
    if sets_hugo == 3 and sets_lin <= 1:
        j_aberto = False
        jogo = False
        print("Hugo garantiu a vitória sem precisar de tie-break! Uma performance sólida e sem erros, ele dominou o jogo do início ao fim e se sagrou campeão do mundo!")
    elif sets_lin == 3 and sets_hugo <= 1:
        j_aberto = False
        jogo = False
        print("Hugo não conseguiu segurar a pressão e acabou perdendo sem precisar do tie-break. Foi uma grande final, mas hoje não foi o seu dia. Vitória do chinês!")
    elif sets_hugo == 3 and sets_lin == 2:
        j_aberto = False
        jogo = False
        print("Hugo é o grande vencedor! Ele conquista o tie-break com uma performance impecável e leva a vitória!")
    elif sets_lin == 3 and sets_hugo == 2:
        j_aberto = False
        jogo = False
        print("Hugo lutou até o fim, mas no tie-break, o adversário levou a melhor. Uma derrota apertada, mas ainda assim, uma grande batalha!")
    
    #troca de sacador
    if s1 == "hugo":
        s1 = "lin"
    elif s1 == "lin":
        s1 = "hugo"

    set_n += 1