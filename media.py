nota1 = float(input('isira a primeira nota: '))
nota2 = float(input('insira a segunda nota: '))
nota3 = float(input('insira a terceira nota: '))
conta = (nota1 + nota2 + nota3)/3
print(f'A média é: {conta}')
if conta >= 6:
    print('aprovado')
    
else:
    print('reprovado')
