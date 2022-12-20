print('-=' * 15)
print('CALCULADORA IMC - Atividade 01')
print('-=' * 15)
nome = str(input('Digite seu nome: ')).strip()
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

print('{}, seu IMC = {:.1f}'.format(nome, imc))
print()
print('-=' * 20)
print('VERIFIQUE A TABELA ABAIXO:\n'
      '\nIMC menor que 18.5 - MAGREZA'
      '\nIMC de 18.5 a 24.9 - SAUDÁVEL'
      '\nIMC de 25 a 29.9 - SOBREPESO'
      '\nIMC de 30 a 34.9 - OBESIDADE GRAU I'
      '\nIMC de 35 a 39.9 - OBESIDADE GRAU II'
      '\nIMC maior que 40 - OBESIDADE GRAU III')
print('-=' * 20)
