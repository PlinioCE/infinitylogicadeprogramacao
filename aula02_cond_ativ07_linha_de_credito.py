print('-=' * 15)
print('BANCO INFINITY - Atividade 07')
print('-=' * 15)

nome = str(input('Informe seu nome: '))
salario = float(input('Informe sua renda mensal: R$ '))
emprestimo = float(input('Informe o valor do crédito: R$ '))
numeroParcela = int(input('Informe o número de parcelas: '))
juros = (emprestimo * 0.03 * numeroParcela)
valorParcela = (emprestimo + juros) / numeroParcela

if valorParcela <= (salario * 0.3):
    credito = 'APROVADO!'
else:
    credito = 'REPROVADO!'
print(f'\nSr(a). {nome}, o empréstimo com valor'
      f'\nde R${emprestimo:.2f} em {numeroParcela}x de R${valorParcela:.2f} foi {credito}')
