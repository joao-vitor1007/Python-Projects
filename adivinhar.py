import random
import time

print('Olá, bem vindo ao jogo de adivinhação de números, irei escolher um número aleatório de 1 a 50 e você tenta adivinhar qual é')
time.sleep(1.5)

numero_secreto = random.randint(1, 50)


print('Já escolhi, vença-me se for capaz...')

while True:
    escolha = int(input('Escolha um número: '))
    diferenca = abs(numero_secreto - escolha)

    if diferenca == 0:
        print(f'🎉 Parabéns, você acertou! O número secreto era {numero_secreto}')
        break

    elif diferenca <= 5:
        if escolha > numero_secreto:
            print('🔥 Você está perto... o número é um pouco menor do que o escolhido')
        else:
            print('🔥 Você está perto... o número é um pouco maior do que o escolhido')

    elif escolha > numero_secreto:
        print('⬇️ O número secreto é menor do que o escolhido')

    else:
        print('⬆️ O número secreto é maior do que o escolhido')
