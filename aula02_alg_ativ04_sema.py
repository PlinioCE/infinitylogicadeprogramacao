print('-=' * 20)
print('SEMA - CONTROLE DE POLUENTES - Atividade 04')
print('-=' * 20)

indice = float(input('Informe o índice de poluição medido: '))

if indice >= 0.5:
    print('\nNOTIFICAÇÃO'
          '\nDevido ao alto índice de poluição, TODOS os grupos das indústrias deverão suspender suas atividades!')
elif indice >= 0.4:
    print('\nNOTIFICAÇÃO'
          '\nDevido ao alto índice de poluição, os grupos 1 e 2 das indústrias deverão suspender suas atividades!')
elif indice >= 0.3:
    print('\nNOTIFICAÇÃO'
          '\nDevido ao alto índice de poluição, o grupo 1 das indústrias deverá suspender suas atividades!')
else:
    print('\nÍNDICE DE POLUIÇÃO DENTRO DOS PARÂMETROS.')
