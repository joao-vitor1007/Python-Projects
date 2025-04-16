import time

soma = 0
quantidade = 0

while True:
    valor = float(input('Insira o valor do produto (ou 0 para finalizar): '))
    
    if valor == 0:
        print('Finalizando programa...')
        time.sleep(0.5)
        break

    soma += valor
    quantidade += 1

valor_medio = soma / quantidade if quantidade > 0 else 0

print(f'Total da compra: R$ {soma:.2f}')
print(f'Total de itens: {quantidade}')
print(f'O valor médio dos produtos é: R$ {valor_medio:.2f}')
