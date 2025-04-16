#✅ Requisitos:
#Ler o arquivo vendas.csv.

#Calcular o total vendido por cada vendedor.

#Calcular qual foi o produto mais vendido em quantidade.

#Calcular o total geral de vendas (quantidade × preço).

#Indicar o vendedor com maior total em R$ vendido


import csv


vendas_por_vendedor = {}

with open("vendas.csv", newline="", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)
    
    for linha in leitor:
        vendedor = linha["vendedor"]
        quantidade = int(linha["quantidade"])
        preco = float(linha["preco_unitario"])
        total_venda = quantidade * preco

       
        if vendedor in vendas_por_vendedor:
            vendas_por_vendedor[vendedor] += total_venda
        else:
            vendas_por_vendedor[vendedor] = total_venda


print("Total de vendas por vendedor:")
for vendedor, total in vendas_por_vendedor.items():
    print(f"{vendedor}: R$ {total:.2f}")
