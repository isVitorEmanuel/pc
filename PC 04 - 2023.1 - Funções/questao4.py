def imprimePartes(separador, numeros):
  
  sublistas = [[]]
  result = ''
    
  for i in numeros:
    if(i == separador):
        sublistas.append([])
    else:
        sublistas[-1].append(i)
  
  for x in sublistas:
    if(x != []):
      for i in x:
        result = result + str(i) + ' '
      result = result + ' \n'
  
  if(result == ''):
    result = 'Nenhuma'
  
  return result 

n = int(input('N? '))
lista = []

print('Qual a sequência? ')

for x in range(0, n):
  lista.append(int(input('')))
  
sep = int(input('Qual o elemento separador?'))

print('Sequências resultantes: ')

print(imprimePartes(sep, lista))

