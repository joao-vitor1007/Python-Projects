
pes = float(input('Insira a medida em pés: '))
conta1 = pes * 12
conta2 = pes / 3
conta3 = pes / 5280
metros = pes * 0.3048

print(f'O valor {pes} pés, é equivalente a: \n {conta1:.0f} polegadas\n {conta2:.0f} jardas\n {conta3:.2f} milhas \n {metros:.2f} metros')
