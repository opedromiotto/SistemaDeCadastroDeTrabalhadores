from datetime import date
import funcoes
import os

trabalhador = {}
dados_trabalhador = []

continuar = True
while continuar:
    nome = input("Nome: ").strip().title()

    #verifica se o ano de nascimento é válido através da função valida_ano_nasc
    ano_valido = False
    while not ano_valido:
        ano_nasc = int(input("Ano de nascimento: "))
        if funcoes.valida_ano_nasc(ano_nasc):
            idade = date.today().year - ano_nasc
            ano_valido = True
        else:
            print("Ano da nascimento inválido, tente novamente")

    #verifica se o o ctps informado é igual a 0, se for, vamos direto p menu
    ctps_valido = False
    while not ctps_valido:
        ctps = str(input("Informe o número de sua carteira de trabalho, apenas números: "))
        if ctps == "0":
            trabalhador["Nome"] = nome
            trabalhador["Idade"] = idade
            trabalhador["CTPS"] = ctps
            dados_trabalhador.append(trabalhador.copy())
            trabalhador.clear()
            ctps_valido = True

    #verifica se o ctps é válido
        elif funcoes.valida_ctps(ctps, dados_trabalhador):
            ctps_valido = True

    #se for, pedimos e verificamos se o ano de contratação é válido através da função valida_contratacao
            ano_contratacao_valido = False
            while not ano_contratacao_valido:
                ano_contratacao = int(input("Ano de contratação: "))
                if funcoes.valida_contratacao(ano_contratacao, ano_nasc):
                    ano_contratacao_valido = True
                else:
                    print("Ano de contratação inválido, tente novamente")
                    continue

    #pedimos o salário e verificamos se é menor qur R$ 1,00
                salario_valido = False
                while not salario_valido:
                    salario = float(input("Salário: R$ "))
                    if salario < 1:
                        print("Salário inválido, tente novamente")
    #se tudo estiver correto, adicionamos os dados do usuário em um dicionário e depois em uma lista composta de dicionários
                    else:
                        trabalhador["Nome"] = nome
                        trabalhador["Idade"] = idade
                        trabalhador["CTPS"] = ctps
                        trabalhador["Ano de contratação"] = ano_contratacao
                        trabalhador["Salário"] = salario
                        trabalhador["Aposentadoria"] = ano_contratacao + 35
                        dados_trabalhador.append(trabalhador.copy())
                        trabalhador.clear()
                        salario_valido = True
        else:
            print("CTPS inválido, tente novamente")

    resposta = input("\nDeseja informar mais uma pessoa?\nPressione 1 - Para sim\nPressione 2 - Para não\nSua escolha: ")
    if funcoes.valida_resposta(resposta):
        if resposta == "2":
            continuar = False
        else:
            os.system('cls')

os.system('cls')
continuar = True
while continuar:
    funcoes.menu()
    resposta = input("Informe sua escolha: ")
    if funcoes.valida_resposta_menu(resposta):
        if resposta == "1":
            funcoes.mostra_dados(dados_trabalhador)
            continue
        elif resposta == "2":
            os.system('cls')
            busca = input("Informe o CTPS procurado: ")
            funcoes.visualizar_trabalhador(dados_trabalhador, busca)
            continue
        else:
            print("Saindo do programa\n")
            continuar = False


    