print('-=' * 15)
print('TAXA DE CRESCIMENTO POPULACIONAL - Atividade 14')
print('-=' * 15)

print('''Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3% e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que
calcule e escreva o número de anos necessários para que a população do
país A ultrapasse ou iguale a população do país B, mantidas as taxas de
crescimento.''')
paisA = 80000
taxaPaisA = 0.03
paisB = 200000
taxaPaisB = 0.015

contador = 0

while paisA < paisB:
    contador += 1
    paisA += paisA * taxaPaisA
    paisB += paisB * taxaPaisB
print(f'\nPaís A: {paisA:.0f} habitantes'
      f'\nPaís B: {paisB:.0f} habitantes'
      f'\nTEMPO: {contador} anos')
