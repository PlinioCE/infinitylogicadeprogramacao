print('-=' * 15)
print('INFINITY SCHOOL - Atividade 12'
      '\nPORTAL DO ALUNO')
print('-=' * 15)

usuario = str(input('USUÁRIO: '))
senha = str(input('SENHA: '))

if usuario == 'INFINITY' and senha == 'school':
    acesso = 'LIBERADO'
else:
    acesso = 'NEGADO'
print(f'\nACESSO {acesso}!')
