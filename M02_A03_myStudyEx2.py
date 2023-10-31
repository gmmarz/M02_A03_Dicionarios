#Leia 4 notas de um aluno, calcule sua média, armazene em um dicionário as seguintes informações:
#a = Nome b=as 4 notas, c - maior nota , d- menor nota , e - media, f-situação

print('Programa de nota')
aluno_status = {'nome':'', 'notas': [], 'maior':0,'menor':0,'media':0,'situacao':''}

aluno_status['nome'] = input('Digite o nome do aluno: ')
i = 1
lst_notas = []
for i in range(4):
    nota = float(input(f'Digite a {i+1}º nota: '))
    lst_notas.append(nota)
aluno_status['notas'] = lst_notas
aluno_status['maior'] = max(lst_notas)
aluno_status['menor'] = min(lst_notas)
aluno_status['media'] = sum(lst_notas)/len(lst_notas)
if aluno_status['media'] >= 6:
    aluno_status['situacao'] = 'Aprovado'
else:
    aluno_status['situacao'] = 'Reprovado'

for i,(item,valor) in enumerate(aluno_status.items()):
    print(f'')

