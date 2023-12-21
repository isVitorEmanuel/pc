"""Crie um programa que lê um valor numérico N e que em seguida lê N números. Armazene esses números em uma lista. Em 
seguida, leia do usuário 3 números inteiros (OP, A e B). O primeiro número (OP) representa uma operação matemática 
(0 é soma, 1 é multiplicação) que deve ser realizada em cima dos dois números cujas posições (1 a N) na lista são A e B. O
programa deve então apresentar a operação e seu resultado."""

n = int(input('Qual o N? '))

numeros = []

print('Digite os valores: ')
for c in range(0, n):
  numeros.append(int(input('')))

op = int(input('Qual a op? '))
a = int(input('Qual o A? '))
b = int(input('Qual o B? '))

if(op == 1):
  valor = numeros[a - 1] * numeros[b - 1]
  print(str(numeros[a - 1]) + ' * ' + str(numeros[b - 1]) + ' = ' + str(valor))
elif(op == 0):
  valor = numeros[a - 1] + numeros[b - 1]
  print(str(numeros[a - 1]) + ' + ' + str(numeros[b - 1]) + ' = ' + str(valor))
else:
  print('Erro na Entrada de Dados!')
  