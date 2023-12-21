"""Crie um programa que leia um número N (0<N<10) e que imprima uma sequência de números conforme mostrado no exemplo:"""

n = int(input('n? '))


if(0 < n < 10):
  
  tex = ''
  
  for l in range(1, n + 1):
    
    for c in range(1, l + 1):
      tex = tex + str(l)
    
    tex = tex + '\n \n'
  
  print(tex)
  
else:
  
  print('Erro na Entrada dos Dados')
