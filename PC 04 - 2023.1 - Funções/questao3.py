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
  

