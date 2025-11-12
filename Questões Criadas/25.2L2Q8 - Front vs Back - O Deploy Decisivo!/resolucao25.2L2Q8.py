print("Serão 12 desenvolvedores defendendo a honra de seus lados do código! Que vença a melhor stack!")

back_campo, front_campo = 6, 6

#definição de quem começa a partida
quem_ataca = input()
while quem_ataca != "Front-End" and quem_ataca != "Back-End": #estrutura possível para uso de laço
    print("Entrada inválida!")
    quem_ataca = input()

jogo = True
while jogo:

    #checa se o jogo acabou
    if back_campo == 0:
        print(f"Vitória do Front-End! Restaram {front_campo} devs ainda segurando o layout!")
        jogo = False
    elif front_campo == 0:
        print(f"Vitória do Back-End! Restaram {back_campo} devs ainda mantendo o servidor de pé!")
        jogo = False

    if jogo:

        #ataque de jogador em campo
        ataque_campo = input()
        while ataque_campo != "acertou" and ataque_campo != "errou":
            print("Entrada inválida!")
            ataque_campo = input()

        if ataque_campo == "acertou":
            print(f"{quem_ataca} acertou um jogador!")

            #troca de bola do jogador em campo para morto do time oponente
            if quem_ataca == "Back-End":
                front_campo -= 1
                quem_ataca = "Front-End"
            else:
                back_campo -= 1
                quem_ataca = "Back-End"
            
            print(f"Back-End: {back_campo} dev(s) em campo. | Front-End: {front_campo} dev(s) em campo.")

            #checa se ainda há jogadores em campo de ambos os times e cria loop de possíveis acertos nos mortos
            teve_acerto = True
            while teve_acerto and front_campo > 0 and back_campo > 0:
                teve_acerto = False
                ataque_morto = input()
                while ataque_morto != "acertou" and ataque_morto != "errou":
                    print("Entrada inválida!")
                    ataque_morto = input()

                if ataque_morto == "acertou":
                    print(f"O morto do {quem_ataca} acertou um jogador!")

                    #troca de bola do morto do time atacante para morto do time oponente
                    if quem_ataca == "Back-End":
                        front_campo -= 1
                        back_campo += 1
                        quem_ataca = "Front-End"
                    else:
                        back_campo -= 1
                        front_campo += 1
                        quem_ataca = "Back-End"

                    teve_acerto = True
                    print(f"Back-End: {back_campo} dev(s) em campo. | Front-End: {front_campo} dev(s) em campo.")

                else: #ataque_morto == "errou"
                    resposta = input()
                    while resposta != "pegou" and resposta != "deixou":
                        print("Entrada inválida!")
                        resposta = input()

                    #troca de bola do morto para jogador do time oponente em campo
                    if resposta == "pegou":
                        quem_ataca = "Front-End" if quem_ataca == "Back-End" else "Back-End"

        else: #ataque_campo == "errou"
            
            #checa se já há alguém no morto para poder pegar a bola
            if quem_ataca == "Back-End" and back_campo < 6 or quem_ataca == "Front-End" and front_campo < 6:

                resposta = input()
                while resposta != "pegou" and resposta != "deixou":
                    print("Entrada inválida!")
                    resposta = input()

                #troca de bola de jogador em campo para jogador em campo do time oponente
                if resposta == "pegou":
                    quem_ataca = "Front-End" if quem_ataca == "Back-End" else "Back-End"

                elif resposta == "deixou":
                    
                    #troca de bola de jogador em campo para jogador do mesmo time no morto
                    teve_acerto = True
                    while teve_acerto and front_campo > 0 and back_campo > 0:
                        teve_acerto = False
                        ataque_morto = input()
                        while ataque_morto != "acertou" and ataque_morto != "errou":
                            print("Entrada inválida!")
                            ataque_morto = input()

                        if ataque_morto == "acertou":
                            print(f"O morto do {quem_ataca} acertou um jogador!")

                            #troca de bola de jogador no morto para jogador do time oponente (q vai pro morto)
                            if quem_ataca == "Back-End":
                                front_campo -= 1
                                back_campo += 1
                                quem_ataca = "Front-End"
                            else:
                                back_campo -= 1
                                front_campo += 1
                                quem_ataca = "Back-End"

                            teve_acerto = True
                            print(f"Back-End: {back_campo} dev(s) em campo. | Front-End: {front_campo} dev(s) em campo.")

                        else:

                            #troca de bola de jogador no morto para jogador do time oponente em campo
                            resposta = input()
                            while resposta != "pegou" and resposta != "deixou":
                                print("Entrada inválida!")
                                resposta = input()

                            if resposta == "pegou":
                                quem_ataca = "Front-End" if quem_ataca == "Back-End" else "Back-End"

            else: #sem jogadores no morto, o time oponente pega a bola
                quem_ataca = "Front-End" if quem_ataca == "Back-End" else "Back-End"