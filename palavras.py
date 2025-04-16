while True:

    frase = input('Insira seu texto ')

    caracter = input('Insira a palavra ou caractér que deseja contar ')

    print('Sua palavra ou caráter aparece', frase.count(caracter), 'vezes')

    sair = input('Você deseja sair? [s]im: ').lower().startswith('s')

    if sair is True:
        break
