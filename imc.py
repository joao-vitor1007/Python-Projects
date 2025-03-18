altura = float(input('Insira sua altura (em metros): '))
peso = float(input('Insira seu peso (em kg): '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.2f}')
