
cpf = input("Digite o CPF (somente números): ")

if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido. Digite exatamente 11 números.")
else:
    nove_digitos = cpf[:9]
    multiplicadores = list(range(10, 1, -1))

    soma = 0
    for i in range(9):
        soma += int(nove_digitos[i]) * multiplicadores[i]

    resultado = (soma * 10) % 11
    digito1 = 0 if resultado == 10 else resultado

    if int(cpf[9]) == digito1:
        dez_digitos = cpf[:10]
        multiplicadores2 = list(range(11, 1, -1))

        soma2 = 0
        for i in range(10):
            soma2 += int(dez_digitos[i]) * multiplicadores2[i]
        
        resultado = (soma2 * 10) % 11
        digito2 = 0 if resultado == 10 else resultado

        if int(cpf[10]) == digito2:
            print("CPF válido!")
        else:
            print("CPF inválido.")
    else:
        print("CPF inválido.")
