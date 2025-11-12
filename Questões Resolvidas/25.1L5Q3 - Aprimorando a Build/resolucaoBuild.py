#guardar os inputs de armas
def info_arma(entrada1, arsenal):
    dados_arma = entrada1.split(" - ")
    arsenal.append(dados_arma)
    return arsenal

#guardar os inputs de aprimoramentos
def info_aprimoramento(entrada2, aprimoramentos):
    dados_aprim = eval(entrada2)
    aprimoramentos.append(dados_aprim)
    return aprimoramentos

#mudar a afinidade da arma atual
def mudar_afinidade(afinidade_arma):
    if afinidade_arma == "físico":
        return "mágico"
    elif afinidade_arma == "mágico":
        return "fogo"
    elif afinidade_arma == "fogo":
        return "dourado"
    elif afinidade_arma == "dourado":
        return "oculto"
    elif afinidade_arma == "oculto":
        return "físico"

#checar cada lista de aprimoramento recebida
def aprimorar_arma(arsenal, posicao, lista):

    #dados da arma
    nome_arma = arsenal[posicao][0]
    tipo_arma = arsenal[posicao][1]
    poder_arma = int(arsenal[posicao][2])
    afinidade_arma = arsenal[posicao][3]
    atributos_arma = arsenal[posicao][4:]

    #aprimoramento
    resultados = calcular_aumento(lista, poder_arma, afinidade_arma, nome_arma, atributos_arma, tipo_arma)

    #atualizar o poder
    poder_arma = resultados[0]
    arsenal[posicao][2] = str(poder_arma)

    #atualizar a afinidade
    afinidade_arma = resultados[1]
    arsenal[posicao][3] = afinidade_arma

    return [aprimoramentos, arsenal]

#cálculo do aumento de força
def calcular_aumento(lista, poder_arma, afinidade_arma, nome_arma, atributos_arma, tipo_arma):
    if lista == []: #é pq os aprimoramentos acabaram
        return [poder_arma, afinidade_arma]

    atual = lista[0]
    resto = lista[1:]

    #checar se é sublista
    if isinstance(atual, list):
        poder_antes = poder_arma
        afinidade_antes = afinidade_arma
        afinidade_nova = mudar_afinidade(afinidade_antes)
        resultados = calcular_aumento(atual, poder_arma, afinidade_nova, nome_arma, atributos_arma, tipo_arma)
        poder_novo = resultados[0]
        afinidade_nova = resultados[1]

        #caso de reversão
        if "R" in atual:
            print("Hmm, não acho que isso vai funcionar...")
            print(f"{nome_arma}: {poder_novo} -> {poder_antes}")
            print(f"Afinidade revertida para {afinidade_antes}")
            return calcular_aumento(resto, poder_antes, afinidade_antes, nome_arma, atributos_arma, tipo_arma)

        #segue com a lista
        return calcular_aumento(resto, poder_novo, afinidade_nova, nome_arma, atributos_arma, tipo_arma)
    
    #aumento por atributo
    if atual in ["S", "D", "I", "F", "A"]:
        aumento = 0

        if atual == "S":
            if "força" in atributos_arma:
                aumento += 1
            if afinidade_arma == "fogo":
                aumento += 1
    
        elif atual == "D":
            if "destreza" in atributos_arma:
                aumento += 1
            if afinidade_arma == "físico":
                aumento += 1
            
        elif atual == "I":
            if "inteligência" in atributos_arma:
                aumento += 1
            if afinidade_arma == "mágico":
                aumento += 1
        
        elif atual == "F":
            if "fé" in atributos_arma:
                aumento += 1
            if afinidade_arma == "dourado":
                aumento += 1
        
        elif atual == "A":
            if "arcano" in atributos_arma:
                aumento += 1
            if afinidade_arma == "oculto":
                aumento += 1
        
        poder_arma += aumento
        return calcular_aumento(resto, poder_arma, afinidade_arma, nome_arma, atributos_arma, tipo_arma)
        
    #aumento por forja
    if atual in ["+", "-"]:
        aumento = 0

        if atual == "+":
            if tipo_arma == "normal":
                aumento += 3
        
        elif atual == "-":
            if tipo_arma == "especial":
                aumento += 5

        poder_arma += aumento
        return calcular_aumento(resto, poder_arma, afinidade_arma, nome_arma, atributos_arma, tipo_arma)
    
    if atual == "R":
        return [poder_arma, afinidade_arma]

    #se nenhum de cima bater
    return calcular_aumento(resto, poder_arma, afinidade_arma, nome_arma, atributos_arma, tipo_arma)

#prints iniciais
print("Não aguento mais morrer para a Malenia, Blade of Miquella...")
print("Vou refazer minha build!")
print()

#primeiros inputs
arsenal = []
entrada1 = input()
arsenal = info_arma(entrada1, arsenal)

while entrada1 != "finalizar":
    entrada1 = input()

    if entrada1 != "finalizar":
        arsenal = info_arma(entrada1, arsenal)

#segundos inputs
aprimoramentos = []
for i in range(len(arsenal)):
    entrada2 = input()
    lista_aprimoramentos = info_aprimoramento(entrada2, aprimoramentos)

#aprimoramento de cada arma
for posicao in range(len(arsenal)):
    lista = lista_aprimoramentos[posicao]
    resultados = aprimorar_arma(arsenal, posicao, lista)

    #print encerramento
    print(f"{arsenal[posicao][0]} aprimorado!")

#variáveis para fins de comparação
armas_fogo = 0
armas_fisico = 0
armas_magico = 0
armas_dourada = 0
armas_oculto = 0

#print de cada arma
print("Inventário:")
for arma in arsenal: #esse for tbm pode
    print(f"- {arma[0]}: {arma[2]}")
    print(f"- afinidade: {arma[3]}")

    if arma[3] == "fogo":
        print("Fogo... é uma das fraquezas da Malenia!!!")
        armas_fogo += 1
    elif arma[3] == "físico":
        armas_fisico += 1
    elif arma[3] == "mágico":
        armas_magico += 1
    elif arma[3] == "dourado":
        print("É, não acho que uma arma de fé vá me ajudar muito...")
        armas_dourada += 1
    elif arma[3] == "oculto":
        armas_oculto += 1
print()

#prints finais
if armas_fogo > armas_fisico and armas_fogo > armas_dourada and armas_fogo > armas_magico and armas_fogo > armas_oculto:
    print("Muitas armas de fogo, ela não vai ter chance!")
elif armas_dourada > armas_fogo and armas_dourada > armas_fisico and armas_dourada > armas_magico and armas_dourada > armas_oculto:
    print("Acho que vou ter que refazer meus aprimoramentos...")
else:
    print("Analisando meu inventário agora, acho que consigo vencer, pode vir, Malenia, Blade of Miquella!!")