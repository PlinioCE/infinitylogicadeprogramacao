valor_compra = float(input('Digite o valor da compra: R$ '))
desconto = vezes_desc = valor_desc = 0
if valor_compra >= 500:
    r = int(valor_compra // 100)
    print()
    if r <= 29:
        for d in range(4, r):
            vezes_desc += 1
            desconto = 0.01 * vezes_desc
            valor_desc = valor_compra * desconto
    elif r >= 30:
        desconto = 0.25
        valor_desc = valor_compra * desconto
    valor_total = valor_compra - valor_desc
else:
    valor_desc = 0
    valor_total = valor_compra
print('----- RECIBO -----')
print(f'VALOR COMPRA    DESC.(%)       VALOR TOTAL'
      f'\nR$ {valor_compra:.2f}       {desconto * 100:.0f}              R$ {valor_total:.2f}')
