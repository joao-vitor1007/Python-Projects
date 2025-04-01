import time


def obter_nota(nome):
    while True:
        try:
            nota = float(input(f'Insira {nome}: '))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Nota inválida! A nota deve ser entre 0 e 10.")
        except ValueError:
            print("Por favor, insira um número válido.")


nota1 = obter_nota('a primeira nota')
time.sleep(0.5)
nota2 = obter_nota('a segunda nota')
time.sleep(0.5)
nota3 = obter_nota('a terceira nota')
time.sleep(0.5)

aula = float(input('Insira o número total de aulas: '))
time.sleep(0.5)
falta = float(input('Insira o número de faltas: '))
time.sleep(0.5)

presenca = aula - falta

conta = (nota1 + nota2 + nota3) / 3
conta2 = (presenca / aula) * 100

print(f'A média das notas é: {conta:.2f} e sua presença é de {conta2}%')
time.sleep(0.5)

if conta >= 6 and conta2 >= 75:
    print('Aprovado')
    time.sleep(0.5)
elif conta <= 5 and conta2 >= 75:
    print('Recuperação')    
    time.sleep(0.5)
else:
    print('Reprovado')
    time.sleep(0.5)
