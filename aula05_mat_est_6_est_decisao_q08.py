print('-=' * 20)
print('CADASTRO DESCONTOS - Questão 08')
print('-=' * 20)

empresa1 = str(input('Informe o nome da empresa: ')).strip().upper()
desconto1 = int(input(f'Informe o desconto(%) da {empresa1}: '))
empresa2 = str(input('Informe o nome da empresa: ')).strip().upper()
desconto2 = int(input(f'Informe o desconto(%) da {empresa2}: '))
print()
funcionario = str(input('Informe o nome do(a) funcionário(a): ')).strip().title()
empresa = str(input(f'Informe o nome da empresa do(a) {funcionario}: ')).strip().upper()
valor_compra = float(input(f'Informe o valor da compra do(a) {funcionario}: R$ '))
print()
if empresa == empresa1:
    desconto = desconto1
    valor_desconto = valor_compra * (desconto / 100)
elif empresa == empresa2:
    desconto = desconto2
    valor_desconto = valor_compra * (desconto / 100)
else:
    desconto = 0
    valor_desconto = valor_compra * 0
print(f'Como {funcionario} é funcionário da empresa {empresa},'
      f'\nterá um desconto de {desconto}% no total de suas compras.'
      f'\n----------------------'
      f'\nCOMPRAS:   R$ {valor_compra:.2f}'
      f'\nDESCONTOS: R$ {valor_desconto:.2f}'
      f'\nTOTAL:     R$ {valor_compra - valor_desconto:.2f}')
