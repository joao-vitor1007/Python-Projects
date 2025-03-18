import random  # Importa o módulo random

lista = []
while True:
    print('Adicione elementos para serem sorteados')
    adc = input('[i]inserir e [a]apagar [m]mostrar [s]sortear: ')

    if adc == 'i':
        valor = input('Valor: ')
        lista.append(valor)
    
    elif adc == 'a':
        indice_str = input('Escolha o indice que deseja apagar: ')

        try:
            indice = int(indice_str)
            del lista[indice]

        except ValueError:
            print('Por favor digite um valor real')

        except IndexError:
            print('Índice não existe na lista')

        except Exception:
            print('Erro desconhecido')

    elif adc == 'm':
        if len(lista) == 0:
            print('Não existe nada para mostrar')

        else:
            for i, valor in enumerate(lista):
                print(i, valor)

    elif adc == 's':  # Quando o usuário escolher 's' para sortear
        if len(lista) == 0:
            print('A lista está vazia, adicione elementos primeiro!')
        else:
            sorteado = random.choice(lista)  # Sorteia um valor aleatório da lista
            print(f'O valor sorteado é: {sorteado}')
    else:
        print('Por favor, escolha i, a, m ou s.')
