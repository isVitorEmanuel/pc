n = int(input('Digite N: '))
serie = ''

a1 = 0
a2 = 1
aux = 0

for count in range(1, n + 1):
  aux = a1 + a2
  
  serie = serie + str(aux) + ', '
  
  a2 = a1
  a1 = aux
  
serie = serie[0: len(serie) - 2]

print('Os '+ str(n) + ' primeiros termos da série de Fibonnaci: ' + serie)