n = int(input('Quantos nomes? '))

alunos = []

for c in range(0, n):
  alunos.append(input(''))
  
print('Você digitou: ')

for c in range(n - 1, -1, -1):
  print(alunos[c])

