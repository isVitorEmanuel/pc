def entradaValores():
  
  n = int(input('N? '))
  valores = []
  
  print('Quais os valores? ')
  
  for x in range(0, n):
    valores.append(int(input('')))
  
  return valores
  
def parproximo(lista):
  
  interMinimo = 1000000000000000000000000000000000000000000000000000
  par = [0, 0]
  
  for x in range(0, len(lista)):
  
    for i in range(x + 1, len(lista)):
      
      if(lista[x] > lista[i]):
        if(lista[x] - lista[i] < interMinimo):
          interMinimo = lista[x] - lista[i]
          par[0] = lista[x]
          par[1] = lista[i]
      elif(lista[x] < lista[i]):
        if(lista[i] - lista[x] < interMinimo):
          interMinimo = lista[i] - lista[x]
          par[0] = lista[x]
          par[1] = lista[i]
      else:
        if(lista[x] - lista[i] < interMinimo):
          interMinimo = lista[x] - lista[i]
          par[0] = lista[x]
          par[1] = lista[i]
        
  return par
        
pares = parproximo(entradaValores())
        
print('Par mais próximo: ' + str(pares[0]) + ' e ' + str(pares[1]))


  
  