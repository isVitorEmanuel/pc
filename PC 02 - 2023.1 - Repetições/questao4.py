n1 = int(input('Digite n1: '))
n2 = int(input('Digite n2: '))

if(n1 >= 1 and n1 <= n2 and n2 <= 10):
  
  for par1 in range(n1, n2 + 1):
    
    print('=-=-=-= Tabuada de ' + str(par1) + ' =-=-=-=')
    
    for par2 in range(1, 11):
      
      print(str(par1) + ' x ' + str(par2) + ' = ' + str(par1 * par2))
      
else:
  
  print('Erro na Entrada dos Dados!')
  