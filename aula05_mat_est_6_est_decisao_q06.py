print('-=' * 20)
print('IMPOSTO - Questão 06')
print('-=' * 20)

nome = str(input('Informe o nome do contribuinte: ')).strip().title()
salario = float(input('Informe a renda mensal do contribuinte: R$ '))
rendimentos = salario * 13
print()
if rendimentos > 100000:
    imposto = rendimentos * 0.15
elif 60000 <= rendimentos < 100000:
    imposto = rendimentos * 0.125
elif 30000 <= rendimentos < 60000:
    imposto = rendimentos * 0.1
else:
    imposto = rendimentos * 0
print(f'O contribuinte, {nome}, obteve R$ {rendimentos:.2f} em\nrendimentos no ano conrrente e deverá pagar R$ {imposto:.2f} de imposto.')
