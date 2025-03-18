import os
palavra_secreta = 'perfume'
letras_corretas = ''
tentativas = 0
while True:
    
    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len (letra_digitada) > 1:
        print('Digite apenas uma letra: ')
        continue
    
    if letra_digitada in palavra_secreta:
           letras_corretas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
         if letra_secreta in letras_corretas:
              palavra_formada += letra_secreta
         else:
              palavra_formada += '*'

              print('Palavra formada:', palavra_formada)

    if palavra_formada == palavra_secreta:
         os.system('cls')
         print('Você Descobriu a palavra secreta, Parabéns!!')
         print('A palavra era:' , palavra_secreta)
         print(f'Você teve {tentativas} tentativas para descobrir a palavra secreta')
