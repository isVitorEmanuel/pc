"""Escreva um programa que peça ao usuário um numero inteiro N e depois um conjunto de N números. O programa deverá 
armazenar todos os números lidos numa lista, e então imprimir todos os números, classificando se cada número é primo ou 
não, no caso se não ser primo o programa também deve imprimir a lista de divisores do número.

Para verificar se um número é primo ou não, escreva uma função que recebe um número inteiro como parâmetro e retorna a sua
lista de divisores. Use o retorno da função para imprimir a saída do programa no formato abaixo:"""

def primos(numero):
  
  tot = []
  div = 0
  nprim = ''
  
  for i in range(1, numero + 1):
      
    if(numero % i == 0):
      div += 1
      tot.append(i)
      
  if(div == 2):
    
    nprim = str(numero) + ' é primo'
    
  else:
    
    nprim = str(numero) + ' não é primo, os divisores são: ' + str(tot)
    
  return nprim

n = int(input('Qual o valor de N? '))

print('Digite os valores: ')

valores = []

for v in range(0, n):
  valores.append(int(input('')))

print('A classificação é: ')

for x in valores:
  print(primos(x))
  

