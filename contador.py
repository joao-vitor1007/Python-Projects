import time
numero = int(input('Digite um número '))
contador = 0

while contador < numero:
    contador = contador + 1

    if contador % 2:
        
        continue

    if contador == numero:
        print(f'Esses são todos os números pares até {numero}')
        break
    time.sleep (0.5)
    print(contador)
