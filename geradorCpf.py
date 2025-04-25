import random


nove_digitos = ''.join([str(random.randint(0, 9)) for _ in range(9)])

multiplicadores1 = list(range(10, 1, -1))
soma1 = sum(int(nove_digitos[i]) * multiplicadores1[i] for i in range(9))
resultado1 = (soma1 * 10) % 11
digito1 = 0 if resultado1 == 10 else resultado1


dez_digitos = nove_digitos + str(digito1)
multiplicadores2 = list(range(11, 1, -1))
soma2 = sum(int(dez_digitos[i]) * multiplicadores2[i] for i in range(10))
resultado2 = (soma2 * 10) % 11
digito2 = 0 if resultado2 == 10 else resultado2


cpf_formatado = f"{nove_digitos[:3]}.{nove_digitos[3:6]}.{nove_digitos[6:9]}-{digito1}{digito2}"

print(f"CPF gerado aleatoriamente: {cpf_formatado}")
