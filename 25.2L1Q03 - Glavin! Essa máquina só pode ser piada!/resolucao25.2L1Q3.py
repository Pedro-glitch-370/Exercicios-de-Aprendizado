#QUESTÃO DE NÍVEL FÁCIL PARA LISTA DE COMANDOS CONDICIONAIS PARA TURMA DE 2025.2

#print inicial
print("Ativando a máquina…")

#dois tipos de entrada (string e inteiro)
nome = input()
ano = int(input())

#uso de len() para pegar a quantidade de caracteres
letras = len(nome)

#uso de if e else para dar o output correto, além do módulo (%)
if ano % letras == 0:
    if nome.lower() == "frink": #uso possível de lower()
        print("Professor Frink irá inventar o rebigulador?! A máquina deve estar com defeito! Glavin!")
    else:
        print(f"Previsão confiável! O rebigulador será real em {ano}!") #uso de f-string
else:
    if nome.lower() == "frink": #poderia ser também: if nome == 'frink' or nome == 'Frink'
        print("Nem precisava colocar os dados! O rebigulador jamais existiria em qualquer universo!")
    else:
        print(f"Previsão instável! {nome.capitalize()} também deve achar que o rebigulador é ridículo...") #uso de capitalize()