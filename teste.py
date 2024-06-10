def valida_cpf(cpf):

    #verifica se o cpf contém apenas digitos
    if not cpf.isdigit():
        return False
    
    #verifica se o cpf possui 11 dígitos
    if len(cpf) != 11:
        return False
        
    # Verifica se todos os dígitos são iguais
    if cpf == cpf[0] * 11:
        return False

    #calcula o primeiro dígito verificador  
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    primeiro_digito = 11 - soma % 11
    if primeiro_digito >= 10:
        primeiro_digito = 0
    if primeiro_digito != int(cpf[9]):
        return False

    #calcula o segundo dígito verificador 
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    segundo_digito = 11 - soma % 11
    if segundo_digito >= 10:
        segundo_digito = 0
    if segundo_digito != int(cpf[-1]):
        return False
        
    return True

while True:
    cpf = str(input("CPF (apenas números): ")).strip()
    if valida_cpf(cpf):
        print("CPF válido")
        break
    else:
        print("CPF inválido, tente novamente")

