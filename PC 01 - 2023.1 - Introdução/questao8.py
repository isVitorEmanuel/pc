texto = input('texto? ')

i1 = int(input('i1? '))
i2 = int(input('i2? '))

if (i1 > i2):
  
  i1, i2 = i2, i1
  
if (i1 >= len(texto) or i2 >= len(texto)):
    print('Erro! Índices precisam ser menores que o tamanho do texto (' + str(len(texto)) + ')')
else:
  
  print('Partes')
  
  parte1 = texto[ : i1]
  parte2 = texto[ : i2]
  parte3 = texto[i1 : i2]
  parte4 = texto[i1 : ]
  parte5 = texto[i2 : ]
  
  print('Parte 1: ' + parte1)
  print('Parte 2: ' + parte2)
  print('Parte 3: ' + parte3)
  print('Parte 4: ' + parte4)
  print('Parte 5: ' + parte5)
