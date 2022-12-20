print('-=' * 15)
print('COMPARA PREÇO - Atividade 07')
print('-=' * 15)

print('INFORME OS PREÇOS DA COTAÇÃO')
preco1 = float(input('Fornecedor 1: '))
preco2 = float(input('Fornecedor 2: '))
preco3 = float(input('Fornecedor 3: '))

if preco1 < preco2 and preco1 < preco3:
    compra = preco1
elif preco2 < preco1 and preco2 < preco3:
    compra = preco2
else:
    compra = preco3
print(f'\nESCOLHER FORNECEDOR COM PREÇO R$ {compra:.2f}')
