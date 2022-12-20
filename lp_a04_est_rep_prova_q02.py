print('-' * 12)
print('Infinityntas')
print('-' * 12)
area = float(input('Qual a área(m²) a ser pintada? '))

constante = area / 18

if constante % 3 == 0:
    lata_tinta = constante // 3
    print(f'\nQUANTIDADE: {lata_tinta:.0f} lata(s) de 18l.')
else:
    lata_tinta = (constante // 3) + 1
    print(f'\nQUANTIDADE: {lata_tinta:.0f} lata(s) de 18l.')
preco_lata = 80

total_tinta = lata_tinta * preco_lata
print(f'TOTAL: R$ {total_tinta:.2f}')
