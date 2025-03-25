nome = input('Insira seu nome: ') 
idade = int(input('Insira sua idade: '))
altura = float(input('Insira sua altura: '))
casa = int(input('Insira o número de casas decimais que deseja: '))
pi: float= 3.141592653589

print(f'Nome: {nome}, idade: {idade}, altura: {altura:.2f}')
print(f'o valor de pi com {casa} casas decimais é {pi:.{casa}f}')
