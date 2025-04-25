lista_cpfs = []

while True:
    print('\n--- MENU PRINCIPAL ---')
    print('1 - Adicionar CPF')
    print('2 - Validar CPF')
    print('3 - Listar todos os CPFs')
    print('4 - formatar CPF')
    print('5 - Sair')
    resposta = input('Escolha uma opção: ')

    if resposta == '1':
        cpf = input('Informe o CPF (apenas números): ')
        if len(cpf) != 11 or not cpf.isdigit():
            print('CPF inválido. Digite exatamente 11 números.')
        else:
            lista_cpfs.append(cpf)
            print('CPF adicionado com sucesso!')

    elif resposta == '2':
        cpf = input('Informe o CPF que deseja validar (apenas números): ')
        if len(cpf) != 11 or not cpf.isdigit():
            print('CPF inválido. Digite exatamente 11 números.')
        else:
            nove_digitos = cpf[:9]
            multiplicadores1 = list(range(10, 1, -1))
            soma1 = sum(int(nove_digitos[i]) * multiplicadores1[i] for i in range(9))
            resultado1 = (soma1 * 10) % 11
            digito1 = 0 if resultado1 == 10 else resultado1

            if int(cpf[9]) == digito1:
                dez_digitos = cpf[:10]
                multiplicadores2 = list(range(11, 1, -1))
                soma2 = sum(int(dez_digitos[i]) * multiplicadores2[i] for i in range(10))
                resultado2 = (soma2 * 10) % 11
                digito2 = 0 if resultado2 == 10 else resultado2

                if int(cpf[10]) == digito2:
                    print('✅ CPF válido!')
                else:
                    print('❌ CPF inválido (segundo dígito incorreto).')
            else:
                print('❌ CPF inválido (primeiro dígito incorreto).')

    elif resposta == '3':
        print('\n--- Lista de CPFs adicionados ---')
        if not lista_cpfs:
            print('Nenhum CPF foi adicionado ainda.')
        else:
            for i, cpf in enumerate(lista_cpfs, start=1):
                print(f'{i}. {cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}')

    elif resposta == '4':
        cpf = input('Insira o CPF que você deseja formatar(somente números): ')
        bloco1 = cpf[0:3]
        bloco2 = cpf[3:6]
        bloco3 = cpf[6:9]
        verificadores = cpf[9:]
        print(f'CPF fomatado: {bloco1}.{bloco2}.{bloco3}-{verificadores}')

    elif resposta == '5':
        print('Finalizando programa...')
        break

    else:
        print('Selecione uma operação válida.')
