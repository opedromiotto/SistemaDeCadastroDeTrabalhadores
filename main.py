from datetime import date
import os

def valida_ano_nasc(ano_nascimento):
    ano_atual = date.today().year

    if str(ano_nascimento).isdigit(): 
        if ano_atual - ano_nascimento < 14 or ano_nascimento < 1900:
            return False
        return True
    return False

def valida_ctps(ctps, dados_trabalhador):
    for t in dados_trabalhador:
        for v in t.values():
            if ctps == v:
                return False
    if str(ctps).isdigit() and len(ctps) == 11:
        return True
    return False

def valida_contratacao(ano_contratacao, ano_nascimento):
    if str(ano_contratacao).isdigit():
        if int(ano_contratacao) > date.today().year or int(ano_contratacao) <= int(ano_nascimento) or int(ano_contratacao) - int(ano_nascimento) < 14:
            return False
        return True
    return False

def valida_resposta(resposta):
    if resposta not in ["1", "2"]:
        return False
    return True

def mostra_dados(dados_trabalhador):
    os.system('cls')
    print(f"=-=-=-=-=-=- TRABALHADORES CADASTRADOS =-=-=-=-=-=-")
    for t in dados_trabalhador:
        for k, v in t.items():
                if k == "CTPS" and v != "0":
                    print(f"{k} = {'***' + '.' + v[3:6] + '.' + v[6:9] + '-' + '**'}")
                else:
                    print(f"{k} = {v}")
        print("-" * 51)
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

def visualizar_trabalhador(dados_trabalhador, ctps):
    os.system('cls')
    encontrado = False
    for t in dados_trabalhador:
        if ctps == t["CTPS"]:
            print(f"=-=-=-=-=-=- DADOS DO TRABALHADOR =-=-=-=-=-=-")
            for k, v in t.items():
                if  k == "CTPS" and v != "0":
                    print(f"{k} = {'***' + '.' + v[3:6] + '.' + v[6:9] + '-' + '**'}")
                else:
                    print(f"{k} = {v}")
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
            encontrado = True
            break
    if not encontrado:
        print("Trabalhador não encontrado.")

def menu():
    print('''
\tMENU
Digite 1 - Para ver todos os trabalhadores
Digite 2 - Para ver um trabalhador específico
Digite 3 - Para sair''')

def valida_resposta_menu(resposta):
    if resposta not in ["1", "2", "3"]:
        return False
    return True

trabalhador = {}
dados_trabalhador = []

while True:
    nome = input("Nome: ").strip().title()
    while True:
        ano_nascimento = int(input("Ano de nascimento: "))
        if valida_ano_nasc(ano_nascimento):
            idade = date.today().year - ano_nascimento
        else:
            print("Ano da nascimento inválido, tente novamente")
            continue
        while True:
            ctps = str(input("Informe o número de sua carteira de trabalho (apenas números): "))
            if ctps == "0":
                trabalhador["Nome"] = nome
                trabalhador["Idade"] = idade
                trabalhador["CTPS"] = ctps
                dados_trabalhador.append(trabalhador.copy())
                trabalhador.clear()
                break
            elif valida_ctps(ctps, dados_trabalhador):
                while True:
                    ano_contratacao = int(input("Ano de contratação: "))
                    if valida_contratacao(ano_contratacao, ano_nascimento):
                        break
                    continue
                while True:
                    salario = float(input("Salário: "))
                    if salario < 1:
                        print("Salário inválido, tente novamente")
                        continue
                    break

                trabalhador["Nome"] = nome
                trabalhador["Idade"] = idade
                trabalhador["CTPS"] = ctps
                trabalhador["Ano de contratação"] = ano_contratacao
                trabalhador["Salário"] = salario
                trabalhador["Aposentadoria"] = ano_contratacao + 35
                dados_trabalhador.append(trabalhador.copy())
                trabalhador.clear()
                break
            else:
                print("Número de carteira de trabalho inválido")
                continue
        break

    while True:
        resposta = input("Deseja informar mais uma pessoa?\nPressione 1 - Para sim\nPressione 2 - Para não\nSua escolha: ")
        if valida_resposta(resposta):
            break
        print("Opção inválida, tente novamente")
        continue
    if resposta == "1":
        continue
    else:
        break

while True:
    while True:
        menu()
        resposta = input("Sua escolha: ")
        if valida_resposta_menu(resposta):
            break
        print("Opção inválida, tente novamente")
        continue

    if resposta == "1":
        mostra_dados(dados_trabalhador)
        continue
    elif resposta == "2":
        busca = input("Informe o CTPS procurado: ")
        visualizar_trabalhador(dados_trabalhador, busca)
        continue
    else:
        print("Saindo do programa...")
        break
