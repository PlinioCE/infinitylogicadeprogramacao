print('-=' * 15)
print('CONTROLE CARGAS - Atividade 02')
print('-=' * 15)

meses = ('MES', 'JAN', 'FEV', 'MAR', 'ABR', 'MAI', 'JUN', 'JUL', 'AGO', 'SET', 'OUT', 'NOV', 'DEZ')

valorTonelada = float(input('Qual o valor fixo da tonelada? R$ '))
quantidadeMeses = int(input('Quantos meses deseja registrar? '))
somaToneladas = contagem = 0

while contagem < quantidadeMeses:
    contagem += 1
    quantidadeToneladas = float(input('Quantas toneladas saíram por mês? '))
    somaToneladas += quantidadeToneladas
totalFaturado = somaToneladas * valorTonelada
print(f'\nSaíram {somaToneladas} toneladas, em {quantidadeMeses} meses.'
      f'\nTotal de faturamento: R$ {totalFaturado:.2f}')
