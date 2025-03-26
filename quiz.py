import time
time.sleep (0.5)
print('Bem vindo ao nosso quiz')
resposta = input('Você deseja começar? [S]sim [N]não: ')
time.sleep (0.5)
if resposta != 'S' and resposta != 's':
    time.sleep (0.5)
    print('Encerrando programa...')
    quit()  

else:
    print('Vamos lá!')
    time.sleep (1.5)
      
print('Quem escreveu "Dom Casmurro"?\n a) Machado de Assis\n b) Clarice Lispector\n c) Jorge Amado\n d) Graciliano Ramos\n')
time.sleep (0.5)
resposta1 = input('Resposta: ')
time.sleep (0.5)

if resposta1 == 'a' or resposta1 == 'A':
    print('Resposta correta, Parabéns')
    time.sleep (0.5)

else:
    print('Resposta incorreta!')
    time.sleep (0.5)

print('Qual é o maior continente do mundo?\n a) África\n b) Ásia\n c) Europa\n d) América\n')
resposta2 = input('Resposta: ')
time.sleep (0.5)


if resposta2 == 'b' or resposta2 == 'B':
    print('Resposta correta, Parabéns')
    time.sleep (0.5)

else:
    print('Resposta incorreta!')


print('Qual é o valor de π (pi) até a segunda casa decimal?\n a) 3.13 \n b) 3.15\n c) 3.16\n d) 3.14\n')
resposta3 = input('Resposta: ')
time.sleep (0.5)


if resposta3 == 'd' or resposta3 == 'D':
    print('Resposta correta, Parabéns')
    time.sleep (0.5)

else:
    print('Resposta incorreta!')


print('Quem foi o primeiro presidente do Brasil?\n a) Getúlio Vargas\n b) Juscelino Kubitschek\n c) Marechal Deodoro da Fonseca\n d) Dom Pedro II\n')
resposta3 = input('Resposta: ')
time.sleep (0.5)


if resposta3 == 'c' or resposta3 == 'C':
    print('Resposta correta, Parabéns')
    time.sleep (0.5)

else:
    print('Resposta incorreta!')
   














    
