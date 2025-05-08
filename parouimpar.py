import random
import time

print('Bem-vindo ao jogo de Par ou Ímpar!')


placar = 0 
placar_pc = 0 

while True:
    while True:
        escolha = input('Escolha par ou ímpar: ').lower()
        if escolha == 'par':
            print('Certo, eu escolho ímpar')
            break
        elif escolha == 'ímpar':
            print('Certo, eu escolho par')
            break
        else:
            print('Digite uma opção válida (par ou ímpar).')
    
    time.sleep(1)

    while True:
        try:
            numero = int(input('Escolha um número de 1 a 10: '))
            if 1 <= numero <= 10:
                break
            else:
                print('Digite um número válido entre 1 e 10.')
        except ValueError:
            print('Digite um número inteiro válido!')

    numero_pc = random.randint(1, 10)
    print(f'O computador escolheu {numero_pc}')
    time.sleep(1)

    soma = numero + numero_pc
    print(f'A soma dos números é {soma}')

    if (soma % 2 == 0 and escolha == 'par') or (soma % 2 != 0 and escolha == 'ímpar'):
        print('🎉 Parabéns, você venceu essa rodada!')
        placar += 1  
    else:
        print('💻 O computador venceu essa rodada!')
        placar_pc += 1  

    print(f'Placar:\nVocê: {placar} || Computador: {placar_pc}\n')

    continuar = input('Você deseja continuar? Sim [s] / Não [n]: ').lower()
    if continuar != 's':
        print('Obrigado por jogar! 👋')
        break
