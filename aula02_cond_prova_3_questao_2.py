print('Informe sua idade em ANOS, MESES e DIAS')
anos = int(input('ANOS: '))
meses = int(input('MESES: '))
dias = int(input('DIAS: '))
dia_anos = anos * 365
dia_meses = meses * 30
idade = dia_anos + dia_meses + dias
print(f'\nIdade em dias: {idade}')
