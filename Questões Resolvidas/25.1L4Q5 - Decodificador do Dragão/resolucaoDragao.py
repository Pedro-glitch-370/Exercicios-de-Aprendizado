#função para realizar operações matemáticas
def analise_notacao(dados):
    operandos = []
    for dado in reversed(dados):
        if dado != "+" and dado != "-" and dado != "*" and dado != "/":
            operandos.append(int(dado))
        else:
            operando2 = operandos.pop(-2)
            operando1 = operandos.pop(-1)
            if dado == "+":
                resultado = operando1 + operando2
                operandos.append(resultado)
            elif dado == "-":
                resultado = operando1 - operando2
                operandos.append(resultado)
            elif dado == "*":
                resultado = operando1 * operando2
                operandos.append(resultado)
            elif dado == "/":
                resultado = operando1 // operando2
                operandos.append(resultado)
    return resultado

#função para conferir se o resultado é primo
def checar_primo(resultado):
    if resultado < 2:
        return 0
    for numero in range(2, int(resultado**0.5) + 1):
        if resultado % numero == 0:
            return 0 
    return 1

#função para converter de binário para decimal
def conversor(string_binaria):
    resultado_decimal = 0
    expoente = 0
    for digito in reversed(string_binaria):
        resultado_decimal += int(digito) * (2 ** expoente)
        expoente += 1
    return resultado_decimal

#função para criar mapa da questão
def criar_mapa(tamanho_matriz, cord_x_goku, cord_y_goku, qtd_esferas, cord_x, cord_y):
    for l in range(tamanho_matriz):
        linha = []
        for c in range(tamanho_matriz):
            if l == cord_x_goku and c == cord_y_goku:
                linha.append("G")
            else:
                tem_esfera = False
                for i in range(qtd_esferas):
                    if l == cord_x[i] and c == cord_y[i]:
                        tem_esfera = True
                
                if tem_esfera:
                    linha.append("☆")
                else:
                    linha.append(".")
        print(" ".join(linha))

#função para encontrar melhor caminho de goku a uma esfera
def analise_trajetoria(cord_x_goku, cord_y_goku, cord_x, cord_y):
    trajetoria = [[cord_x_goku, cord_y_goku]]
    esferas_vistas = []

    for i in range(len(cord_x)):
        esferas_vistas.append("não vista") #todas começam sem terem sido analisadas

    atual_x_goku = cord_x_goku
    atual_y_goku = cord_y_goku

    for i in range(len(cord_x)): #posicao para cada esfera existente
        menor_distancia = 99999999999999

        for j in range(len(cord_x)): #posicao para cada esfera não analisada
            if esferas_vistas[j] == "não vista":
                distancia_atual_esfera = ((cord_x[j] - atual_x_goku)**2 + (cord_y[j] - atual_y_goku)**2)**0.5
                if distancia_atual_esfera < menor_distancia:
                    menor_distancia = distancia_atual_esfera
                    esfera_a_ser_vista = j
        
        #decidida a próxima esfera
        esferas_vistas[esfera_a_ser_vista] = "vista"
        atual_x_goku = cord_x[esfera_a_ser_vista]
        atual_y_goku = cord_y[esfera_a_ser_vista]
        trajetoria.append([atual_x_goku, atual_y_goku])

    return trajetoria

#inputs iniciais
tamanho_matriz = int(input())
localizacao_goku = input() #(x_goku, y_goku)
cord_x_goku = int(localizacao_goku[1])
cord_y_goku = int(localizacao_goku[4])
linha_vazia = input()

#outputs iniciais
print("🟠 Vamos conquistar as esferas do dragão! 🟠")
print("--------------------------------------------------------------------------")
print()

#loop de entradas codificadas
entrada = input()
qtd_esferas = 0
cord_x = []
cord_y = []

while entrada != "Todos os bits foram decodificados": #loop geral

    if entrada == "------------------------------------": #loop de uma esfera
        entrada = input()

        qtd_esferas += 1
        string_binaria = ""

        while entrada != "": #loop do x

            notacao_pre_fixa_x = entrada
            dados = notacao_pre_fixa_x.split(" ")

            #análise da notação
            resultado = analise_notacao(dados)
            
            #funcao pra ver se é primo
            primo = checar_primo(resultado)
            if primo == 0: #não é primo
                string_binaria += "0"
            elif primo == 1:
                string_binaria += "1"

            entrada = input()
            #fim do loop de x

        #funcao pra converter de binário pra decimal
        decimal = conversor(string_binaria)
        cord_x_esfera = decimal % tamanho_matriz
        print(f"Coordenada x da {qtd_esferas}ª esfera do dragão obtida pelo código binário {string_binaria}: {cord_x_esfera}")
        cord_x.append(cord_x_esfera)

        entrada = input()

        string_binaria = ""
        while entrada != "": #loop do y

            notacao_pre_fixa_y = entrada
            dados = notacao_pre_fixa_y.split(" ")
            operandos = []

            #análise da notação
            resultado = analise_notacao(dados)

            #funcao pra ver se é primo
            primo = checar_primo(resultado)
            if primo == 0: #não é primo
                string_binaria += "0"
            elif primo == 1:
                string_binaria += "1"
        
            entrada = input()
            #fim do loop do y
        
        #funcao pra converter de binário pra decimal
        decimal = conversor(string_binaria)
        cord_y_esfera = decimal % tamanho_matriz
        print(f"Coordenada y da {qtd_esferas}ª esfera do dragão obtida pelo código binário {string_binaria}: {cord_y_esfera}")
        print(f"As coordenadas da {qtd_esferas}ª esfera do dragão são: ({cord_x_esfera}, {cord_y_esfera})")
        print()
        cord_y.append(cord_y_esfera)

    entrada = input()

print("--------------------------------------------------------------------------")
print()

#criando o mapa
criar_mapa(tamanho_matriz, cord_x_goku, cord_y_goku, qtd_esferas, cord_x, cord_y)
print()

#ordem de esferas mais próximas
trajetoria_oficial = analise_trajetoria(cord_x_goku, cord_y_goku, cord_x, cord_y)

#outputs finais
print(f"Trajetória completa de Goku:", end= " ")

for lista in trajetoria_oficial:
    posicao_final = trajetoria_oficial.index(lista) #para pegar a última posição

for posicao_par in range(len(trajetoria_oficial)):
    x = trajetoria_oficial[posicao_par][0]
    y = trajetoria_oficial[posicao_par][1]
    print(f"({x}, {y})", end= "")
    if posicao_par != posicao_final:
        print(f" -> ", end= "")
print()

print("Missão cumprida! Conseguimos todas as esferas do dragão!🟠🐉")