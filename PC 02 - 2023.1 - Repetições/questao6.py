"""Escreva um programa que peça ao usuário dois números inteiros n1 e n2 (n2 > n1) e imprima quantos números primos 
existem no nintervalo [n1, n2], incluindo esses dois números. Lembre-se que um número é primo se ele é divisivel apenas 
por 1 e por ele mesmo."""

n1 = int(input('n1? '))
n2 = int(input('n2? '))

div = 0
nu_prim = 0

if(n1 > n2):
  n1, n2 = n2, n1

for num in range(n1, n2 + 1):
  
  div = 0

  for i in range(1, num + 1):
    
    if(num % i == 0):
      div += 1
    
  if(div == 2):
    nu_prim = nu_prim + 1
        
print('Existem ' + str(nu_prim) + ' numeros primos entre ' + str(n1) + ' e ' + str(n2))
  