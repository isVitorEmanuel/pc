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
  