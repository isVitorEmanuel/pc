"""Faça um programa que leia dois números n1 e n2, onde 1 <= n1 <= n2 <= 10, e que imprima a tabuada dos números entre 
n1 e n2, conforme exemplo."""

n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))

if(n1 >= 1 and n1 <= n2 and n2 <= 10):
  
  for par1 in range(n1, n2 + 1):
    
    print('=-=-=-= Tabuada de ' + str(par1) + ' =-=-=-=')
    
    for par2 in range(1, 11):
      
      print(str(par1) + ' x ' + str(par2) + ' = ' + str(par1 * par2))
      
else:
  
  print('Erro na Entrada dos Dados!')
  