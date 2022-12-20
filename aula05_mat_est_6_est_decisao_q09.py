print('-=' * 20)
print('CONSULTA ON-LINE - Questão 09')
print('-=' * 20)

print('QUESTIONÁRIO')
print('Por favor responda as perguntas com "S" para SIM ou "N" para NÃO.')
print()
febre = str(input('O paciente tem febre alta? ')).strip().upper()[0]
dor_cabeca = str(input('O paciente tem dor de cabeça? ')).strip().upper()[0]
dor_muscular = str(input('O paciente tem dores musculares? ')).strip().upper()[0]
manchas_vermelhas =str(input('O paciente tem manchas vermelhas no corpo? ')).strip().upper()[0]
print()
contador = 0
if febre == 'S':
    contador += 1
if dor_cabeca == 'S':
    contador += 1
if dor_muscular == 'S':
    contador += 1
if manchas_vermelhas == 'S':
    contador += 1
if contador >= 3:
    print('ALERTA! SUSPEITA DE DENGUE. PROCUPRE UM MÉDICO IMEDIATAMENTE.')
else:
    print('PERMANEÇA EM REPOUSO, OBSERVANDO A EVOLUÇÃO DOS SINTOMAS.')
