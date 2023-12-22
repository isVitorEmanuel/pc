n1 = int(input('n1? '))
n2 = int(input('n2? '))
n3 = int(input('n3? '))

if (n1 == n2 and n2 == n3):
  print('Todos são iguais à ' + str(n1))
elif (n1 == n2 and n1 != n3):
  if (n1 > n3):
    print('Maiores: ' + str(n1))
    print('Menor: ' + str(n3))
    print('Não há elementos do meio')
  else:
    print('Maior: ' + str(n3))
    print('Menores: ' + str(n1))
    print('Não há elementos do meio')
elif (n1 != n2 and n2 == n3):
  if(n1 > n2):
    print('Maior: ' + str(n1))
    print('Menores: ' + str(n2))
    print('Não há elementos do meio')
  else:
    print('Maiores: ' + str(n2))
    print('Menor: ' + str(n1))
    print('Não há elementos do meio')
elif (n1 == n3 and n1 != n2):
  if(n1 > n2):
    print('Maiores: ' + str(n1))
    print('Menor: ' + str(n2))
    print('Não há elementos do meio')
  else:
    print('Maior: ' + str(n2))
    print('Menores: ' + str(n1))
    print('Não há elementos do meio')
else:
  if(n1 > n2 and n1 > n3):
    if(n2 > n3):
      print('Maior: ' + str(n1))
      print('Menor: ' + str(n3))
      print('Meio: ' + str(n2))
    else:
      print('Maior: ' + str(n1))
      print('Menor: ' + str(n2))
      print('Meio: ' + str(n3))
  elif(n2 > n1 and n2 > n3):
    if(n1 > n3):
      print('Maior: ' + str(n2))
      print('Menor: ' + str(n3))
      print('Meio: ' + str(n1))
    else:
      print('Maior: ' + str(n2))
      print('Menor: ' + str(n1))
      print('Meio: ' + str(n3))
  else:
    if(n1 > n2):
      print('Maior: ' + str(n3))
      print('Menor: ' + str(n2))
      print('Meio: ' + str(n1))
    else:
      print('Maior: ' + str(n3))
      print('Menor: ' + str(n1))
      print('Meio: ' + str(n2))
      
    
