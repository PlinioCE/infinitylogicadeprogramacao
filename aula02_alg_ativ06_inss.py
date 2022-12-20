from datetime import date

print('-=' * 20)
print('PLANO DE PREVIDÊNCIA - Atividade 06')
print('-=' * 20)

'''1) Ter 65 anos;
   2) Ter 30 anos de contribuição
   3) Ter 60 anos e 25 anos de contribuição'''

anoAtual = date.today().year
matricula = int(input('Informe a matrícula do empregado: '))
anoNascimento = int(input('Informe o ano de nascimento: '))
anoAdmissao = int(input('Informe o ano de admissão:  '))
idade = anoAtual - anoNascimento
tempoContribuicao = anoAtual - anoAdmissao

if idade >= 60 and tempoContribuicao >= 25:
    print('\nREQUERER APOSENTADORIA.')
elif idade >= 65:
    print('\nREQUERER APOSENTADORIA POR IDADE.')
elif tempoContribuicao >= 30:
    print('\nREQUERER APOSENTADORIA POR TEMPO DE SERVIÇO.')
else:
    print('\nNÃO REQUERER APOSENTADORIA.')
