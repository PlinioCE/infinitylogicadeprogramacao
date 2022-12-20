print('-=' * 15)
print('LÍNGUA DO P - Atividade 05')
print('-=' * 15)

nome = str(input('Informe um nome para traduzir para língua do "P": ')).upper()
print()
for i in nome:
    if i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U':
        print(i + 'P' + i, end='')
    else:
        print(i, end='')
print('\n')


meuCarrinho = {"camisa": 50.0, "vestido": 80.5, "bolsa": 70.0}
for peca, valor in meuCarrinho.items():
    break
    print(peca, ":", valor)
    continue
print('Volte sempre!')
