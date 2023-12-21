"""Em uma turma de alunos que conversavam muito, um professor montou a seguinte estratégia. Após os alunos se sentarem, 
ele mandava os alunos trocarem de lugar. Para ajudar esse processo, crie um programa para ajudar esse professor. O 
programa deve ler um valor N, que representa a quantidade de alunos. Em seguida, deve ler os nomes de cada aluno. 
Considere a sequência lida como a ordem das cadeiras dos alunos. O programa deve então imprimir os nomes em uma nova ordem, 
trocando os alunos sentados em cadeiras de número par (o da primeira cadeira par vai para a última par, o da segunda para 
a antepenúltima, etc.).

Se houver uma quantidade ímpar de cadeiras pares (em uma turma de 7 alunos, vão haver 3 cadeiras pares), o aluno da cadeira
central não terá seu local trocado."""

qntd = int(input('Quantos alunos: '))
alunos = []

print('Digite os nomes dos alunos: ')
for a in range(0, qntd):
  alunos.append(input(''))

print('Nova lista: ')

for x in range(0, len(alunos)//2):
  if(x % 2 != 0):
    alunos[x], alunos[len(alunos) - x - 1] = alunos[len(alunos) - x - 1], alunos[x]

for a in alunos:
  print(a)
    