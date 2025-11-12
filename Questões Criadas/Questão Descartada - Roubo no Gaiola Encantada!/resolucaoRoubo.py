#função pra rastrear as movimentações
def desvendar_ladrao(registros_restantes, presentes_no_salao, horario_atual):
    #caso base de não ter encontrado o ladrão
    if not registros_restantes:
        return False
  
    #organiza os dados a serem analisados
    grupo_atual = registros_restantes[0]
    proximos_registros = registros_restantes[1:]
    presentes_no_salao = presentes_no_salao[:]

    #processa monstros que entraram e saíram no salão
    for inicial_monstro in grupo_atual:
        presentes_no_salao.remove(inicial_monstro) if inicial_monstro in presentes_no_salao else presentes_no_salao.append(inicial_monstro)
            
    #caso de ter encontrado o ladrão
    if len(presentes_no_salao) == 1:
        return [presentes_no_salao[0], horario_atual]
    else:
        print(f"O relógio bate {horario_atual} horas... A bruma de mistério ainda paira sobre o Gaiola.")

    return desvendar_ladrao(proximos_registros, presentes_no_salao, horario_atual+1)

#função principal (escolha possível de função, mas meramente opcional)
def executar_investigacao(registros):
    print("Há um impostor entre nós... Que a investigação comece!")

    #lista pra mapeamento dos nomes
    mapeamento_nomes = [
        ['Z', 'Zumbi'], ['G', 'Gárgula'], ['L', 'Lobisomem'], ['F', 'Fantasma'],
        ['V', 'Vampiro'], ['M', 'Múmia'], ['B', 'Bruxa'], ['C', 'Ciclope'],
        ['O', 'Ogro'], ['S', 'Sereia'], ['T', 'Troll'], ['E', 'Espírito'],
        ['P', 'Palhaço'], ['H', 'Homem do Saco']
    ]
    
    resultado = desvendar_ladrao(registros, [], horario_atual=0) 

    if resultado:
        inicial_ladrao = resultado[0]
        horario_crime = resultado[1]

        achou = False
        for par in mapeamento_nomes:
            if par[0] == inicial_ladrao and not achou:
                nome_ladrao = par[1]
                achou = True

        print(f"Elementar, meu caro programa! O criminoso, afinal, é o(a) {nome_ladrao}, que roubou sozinho(a) os doces às {horario_crime} horas dessa madrugada!")
    
    else:
        print("Somente com essas informações, não posso deduzir qual a mente obscura por trás desse caso... São os fatos, madame, apenas os fatos...")

#PROGRAMA COMEÇA AQUI
entrada = eval(input())
executar_investigacao(entrada)