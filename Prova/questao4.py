def primos(numero):
  
  tot = []
  div = 0
  nprim = ''
  
  for i in range(1, numero + 1):
      
    if(numero % i == 0):
      div += 1
      tot.append(i)
      
  if(div == 2):
    
    nprim = 'Primo'
    
  else:
    
    nprim = 'Não primo'
    
  return nprim

def par(numero):
  
  if((numero % 2) == 0):
    nPar = 'Par'
  else: 
    nPar = 'Ímpar'
  return nPar
for x in range(0, 3):
  n = int(input('Entrada: '))
  
  resPri = primos(n)
  
  print('Resposta: ' + resPri)
  
  resPar = par(n)
  
  print('Resposta: ' + resPar)