import random
cpf = input("Digite o CPF sem os números de verificação (somente números): ")

if len(cpf) != 9 or not cpf.isdigit():
    print("CPF inválido. Digite exatamente 9 números.")
else:
    nove_digitos = cpf[:9]
    multiplicadores = list(range(10, 1, -1))

    soma = 0
    for i in range(9):
        soma += int(nove_digitos[i]) * multiplicadores[i]

    resultado = (soma * 10) % 11
    digito1 = 0 if resultado == 10 else resultado

    print(f'O primeiro dígito de verificação do seu CPF é: {digito1}')

    cpf2 = input('Digite o CPF com o primeiro número de verificação (somente números): ')
    if len(cpf2) != 10 or not cpf2.isdigit():
        print('CPF inválido, insira exatamente 10 números.')
    else:
        dez_digitos = cpf2[:10]
        multiplicadores2 = list(range(11, 1, -1))

        soma2 = 0
        for i in range(10):
            soma2 += int(dez_digitos[i]) * multiplicadores2[i]
        
        resultado = (soma2 * 10) % 11
        digito2 = 0 if resultado == 10 else resultado
        bloco1 = cpf[0:3]
        bloco2 = cpf[3:6]
        bloco3 = cpf[6:9]

        print(f'O segundo dígito de verificação do seu CPF é: {digito2}')
        print(f'Para finalizar, seu cpf completo ficou assim: {bloco1}.{bloco2}.{bloco3}-{digito1}{digito2}')
