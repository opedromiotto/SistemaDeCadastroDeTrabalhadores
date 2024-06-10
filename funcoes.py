import os
from datetime import date

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
    #verifica se o cpf contém apenas digitos
    if not ctps.isdigit():
        return False
    
    #verifica se o cpf possui 11 dígitos
    if len(ctps) != 11:
        return False
        
    # Verifica se todos os dígitos são iguais
    if ctps == ctps[0] * 11:
        return False

    #calcula o primeiro dígito verificador  
    soma = sum(int(ctps[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - soma % 11
    if primeiro_digito >= 10:
        primeiro_digito = 0
    if primeiro_digito != int(ctps[9]):
        return False

    #calcula o segundo dígito verificador 
    soma = sum(int(ctps[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - soma % 11
    if segundo_digito >= 10:
        segundo_digito = 0
    if segundo_digito != int(ctps[-1]):
        return False
        
    return True

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