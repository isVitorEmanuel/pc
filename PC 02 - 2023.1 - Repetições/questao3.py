"""Um número inteiro positivo,n, é dito triangular se, e somente se, ele é o resultado do produto de três números inteiros 
positivos e consecutivos. Escreva um algoritmo que leia um número inteiro positivo, n, e escreva como saída “é triangular”
se n for triangular e “não é triangular”, caso contrário."""

n = int(input('n?'))

for i in range(1, n):
  if((i * (i + 1) * (i + 2)) == n):
    trian = 'é triangular'
    break
  else:
    trian = 'não é triangular'

print(trian)