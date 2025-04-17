while True:
    resposta = input('Você deseja formatar um CPF? [1] Sim ou [2] Não: ')

    if resposta == '1':
        cpf = input('Insira seu CPF (somente números): ')
        
        if len(cpf) != 11 or not cpf.isdigit():
            print('CPF inválido, digite os 11 números.')
        else:
            bloco1 = cpf[0:3]
            bloco2 = cpf[3:6]
            bloco3 = cpf[6:9]
            verificadores = cpf[9:]
            central = cpf[5]

            print(f'CPF formatado: {bloco1}.{bloco2}.{bloco3}-{verificadores}')
            print(f'Seis primeiros dígitos: {bloco1}.{bloco2}')
            print(f'Dígitos verificadores: {verificadores}')
            print(f'Dígito central: {central}')
    
    elif resposta == '2':
        print("Encerrando o programa. Até mais!")
        break

    else:
        print("Opção inválida. Digite 1 para sim ou 2 para não.")
