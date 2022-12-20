print('-=' * 20)
print('VEREJÃO - Questão 07')
print('-=' * 20)

total = 0
while True:
    produto = str(input('Informe o produto: ')).strip().lower()
    valor_kg = float(input(f'Informe o valor do quilo de {produto}: R$ '))
    quantidade_kg = float(input(f'Informe quantos quilos de {produto} deseja comprar: '))
    preco = valor_kg * quantidade_kg
    print(f'{produto.upper()}: {quantidade_kg}Kg x R$ {valor_kg:.2f} = R$ {preco:.2f}')
    total += preco
    saida = ' '
    while saida not in 'SN':
        saida = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
        print()
    if saida == 'N':
        if 200 < total <= 500:
            total = total - (total * 0.05)
        elif total > 500:
            total = total - (total * 0.1)
        else:
            total = total
        print(f'TOTAL: R$ {total:.2f}')
        print('\n*** FINALIZANDO SISTEMA ***')
        break
