print('-=' * 18)
print('LOJAS PINTOU PINTANDO - Atividade 07')
print('-=' * 18)

comprimento = float(input('Informe o comprimento(m) da área: '))
largura = float(input('Informe a largura(m) da área: '))
area = comprimento * largura
quantidadeGalaoGrande = area / 18
quantidadeGalaoPequeno = area / 3.6
precoGalaoGrande = 80 * quantidadeGalaoGrande
precoGalaoPequeno = 25 * quantidadeGalaoPequeno

print(f'\nORÇAMENTO:'
      f'\nGALÃO 18l ====='
      f'\nQTD: {quantidadeGalaoGrande:.1f}'
      f'\nR$ {precoGalaoGrande:.2f}'
      f'\n---------------'
      f'\nGALÃO 3.6l ===='
      f'\nQTD: {quantidadeGalaoPequeno:.1f}'
      f'\nR$ {precoGalaoPequeno:.2f}')
