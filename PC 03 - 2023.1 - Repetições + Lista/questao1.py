"""Escreva um programa que lê a quantidade dos alunos de uma turma. Em seguida, o programa deve ler os nomes de cada aluno
e imprimí-los na ordem inversa."""

n = int(input('Quantos nomes? '))

alunos = []

for c in range(0, n):
  alunos.append(input(''))
  
print('Você digitou: ')

for c in range(n - 1, -1, -1):
  print(alunos[c])

