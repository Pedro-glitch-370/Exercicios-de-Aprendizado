#listas a serem usadas
monitores_chefes = ["Adrieli Queiroz", "Arthur Jorge", "César Cavalcanti", "Elisson Oliveira", "Filipe Moreira", "Gabriela Alves", "Joab Henrique", "Maria Fernanda", "Miriam Gonzaga", "Sofia Remindes"]
patrocinadores_marcas = [["Tha Beauty", "Thais Linares"], ["DeGuê?", "Davi Brito"], ["Diva Depressão", "Edu e Fih"]]

#inputs iniciais
numero_desfilantes = int(input())
patrocinador_marca = input()

#checar quem é o patrocinador
for lista in patrocinadores_marcas:
    if patrocinador_marca == lista[0]: #uso possível de lista dentro de lista
        patrocinador_nome = lista[1]

#receber os desfilantes originais
entradas_originais = []
for i in range(numero_desfilantes):
    nome_desfilante = input()
    entradas_originais.append(nome_desfilante) #uso de append

#listas pra controlar quem realmente vai desfilar
desfilantes_finais = []
desfilantes_aprovados = []

#checar se é um invasor
contadorCore1 = 0
for i in range(numero_desfilantes):
    aprovado = False
    eh_patrocinador = False

    for j in range(len(monitores_chefes)):
        if (entradas_originais[i] == monitores_chefes[j]) or (entradas_originais[i] == patrocinador_nome and not eh_patrocinador):
            aprovado = True

            if entradas_originais[i] == patrocinador_nome and not eh_patrocinador:
                eh_patrocinador = True

            desfilantes_aprovados.append(entradas_originais[i])
            desfilantes_finais.append(entradas_originais[i])
        
    if not aprovado:
        contadorCore1 += 1
        desfilantes_finais.append("INTRUSO")

#contadores para condição especial do Core
contadorCore2 = 3 if contadorCore1 >= 3 else -1

#checar quais monitores ainda podem ser chamados
monitores_livres = []
for i in range(len(monitores_chefes)):
    ja_entrou = False

    for j in range(len(desfilantes_aprovados)):
        if monitores_chefes[i] == desfilantes_aprovados[j]:
            ja_entrou = True
        
    if not ja_entrou:
        monitores_livres.append(monitores_chefes[i])

#fazer as substituições
i = 0
while i < len(desfilantes_finais):
    if desfilantes_finais[i] == "INTRUSO":
        contadorCore2 -= 1

        if len(monitores_livres) > 0:
            desfilantes_finais[i] = monitores_livres[0]
            monitores_livres = monitores_livres[1:] #uso possível de slicing
        else:
            desfilantes_finais[i] = entradas_originais[i]
        
        if contadorCore2 == 0:
            desfilantes_finais.insert(i+1, "Core") #uso possível de insert
            entradas_originais.insert(i+1, "IGNORAR")
            i += 1
    i += 1

print("Senhoras e senhores, o desfile de gala do CIn vai começar!")

#prints do desfile
apareceu_especial = False
for i in range(len(desfilantes_finais)):
    desfilante_atual = desfilantes_finais[i] #para pegar os substitutos
    entrada_original = entradas_originais[i] #para pegar intrusos
    
    if entrada_original in ["Gretchen", "Tulla Luana", "Inês Brasil"]: #uso possível de in em lista
        apareceu_especial = True #bool usada posteriormente pros prints especiais

    eh_monitor = False
    if entrada_original in monitores_chefes:
        eh_monitor = True
    
    if entrada_original == patrocinador_nome:
            print(f"Invasão tolerada por motivos de patrocínio!")

    elif not eh_monitor:
        if entrada_original != "IGNORAR":
            print(f"{entrada_original} invadiu a passarela! Segurem ele(a), produção!")
        
        if desfilante_atual == "Core":
            print("Muitas invasões estão deixando a galera irritada... Chama o Core pra acalmar os ânimos!")

    if desfilante_atual in monitores_chefes or desfilante_atual == patrocinador_nome or desfilante_atual == "Core":
        print(f"Desfilante de n° {i + 1}: {desfilante_atual}!")
    else:
        print(f"Desfilante de n° {i + 1}: {desfilante_atual}?! Pelo visto não havia como substituir...")

#prints especiais
if apareceu_especial:
    print("Nas arquibancadas do CIn, sussurros indignados agitam a multidão...")

    for i in range(len(entradas_originais)):
        if entradas_originais[i] == "Gretchen":
            print('"Eles tem que respeitar os meus 37 anos de carreira! Eu hoje sou um ícone, se eu morrer hoje eu vou continuar sendo a Gretchen!"')
            
        elif entradas_originais[i] == "Tulla Luana":
            print('"Ninguém ser humano está acima de mim! Mas eu estou acima de muitos... é assim que eu penso."')
            
        elif entradas_originais[i] == "Inês Brasil":
            print('"É aquele ditado... Vamo fazer o quê?"')