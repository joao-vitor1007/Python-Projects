# 901.118.970-17
# 90111897017
# 9  0  1  1  1  8  9  7  0 
# 10 9  8  7  6  5  4  3  2  

# 90 0  8  7  6  40 36 21 0 = Vamos somar esses números:


# 90 + 0 + 8 + 7 + 6 + 40 + 36 + 21 + 0 = 208 * 10 = 2080 resto divisivel por 11 é 1

cpf = input("Digite o CPF (somente números): ")


if len(cpf) != 11 or not cpf.isdigit():
    print("CPF inválido. Digite exatamente 11 números.")
else:
    
    nove_digitos = cpf[:9]

    print("\nDígitos do CPF:")
    print(" ".join(nove_digitos))

    multiplicadores = list(range(10, 1, -1))  
    print("Multiplicadores:")
    print(" ".join(str(m) for m in multiplicadores))

    soma = 0
    print("\nMultiplicações:")
    for i in range(9):
        d = int(nove_digitos[i])
        m = multiplicadores[i]
        mult = d * m
        soma += mult
        print(f"{d} x {m} = {mult}")

    print(f"\nSoma: {soma}")
    resultado = (soma * 10) % 11
    digito1 = 0 if resultado == 10 else resultado
    print(f"({soma} * 10) % 11 = {resultado} → Primeiro dígito verificador: {digito1}")

   
    if int(cpf[9]) == digito1:
        print("Primeiro dígito verificador está CORRETO!")
    else:
        print("Primeiro dígito verificador está INCORRETO!")
