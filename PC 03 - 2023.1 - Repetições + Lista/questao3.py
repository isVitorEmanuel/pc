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
    