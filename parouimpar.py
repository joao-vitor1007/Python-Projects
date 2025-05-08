import random
import time

while True:
    escolha = input('Escolha par ou ímpar: ').lower()  
    time.sleep(1.5)

    if escolha == 'par':
        print('Certo, eu escolho ímpar')
        break  

    elif escolha == 'ímpar':
        print('Certo, eu escolho par')
        break  

    else:
        print('Digite uma opção válida (verifique se você digitou corretamente).')
        
while True:
    numero = int(input('Escolha um número de 1 a 10: '))
    if numero <= 10:
        break
    else:
        print('Digite um número válido')

while True:
    numero_pc = random.randint(1, 10)
    print(f'O computador escolheu {numero_pc}')
    time.sleep(1.5)
    
    if numero % numero_pc == 2 and escolha == "par":
        print('Parabéns, você venceu essa rodada')
    else:
        print('O computador venceu essa rodada')
        time.sleep(1.5)
        continuar = input('Você deseja continuar? Sim[s] Não[n]').lower()

    
