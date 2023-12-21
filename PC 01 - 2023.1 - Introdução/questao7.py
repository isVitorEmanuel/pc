"""Escreva um programa que pede ao usuário um número de dias e converte esse número em semanas e dias. Observe que existem
muitos casos específicos a serem tratados, uma vez que faz diferença dizer "dia" ou "dias", bem como "semana" ou "semanas", por exemplo:

Se o usuário digitar 0, o programa deve exibir: 0 dias equivale à nenhum dia.
Se o usuário digitar 7, o programa deve exibir: 7 dias equivalem à 1 semana!
Se o usuário digitar 8, o programa deve exibir: 8 dias equivalem à 1 semana e 1 dia!
Se o usuário digitar 30, o programa deve exibir: 30 dias equivalem à 4 semanas e 2 dias!"""

num_dias = int(input("Digite o número de dias: "))

semanas = num_dias // 7
dias_resto = num_dias % 7

if(num_dias == 0):
  print(str(num_dias) + ' dias equivale à nenhum dia.')
elif(num_dias == 1):
  print(str(num_dias) + ' dia equivale à ' + str(semanas) + ' semanas e ' + str(dias_resto) + ' dia!')
else:
  if(semanas == 1):
    if(dias_resto > 1 ):
      print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semana e ' + str(dias_resto) + ' dias!')
    elif(dias_resto == 1):  
       print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semana e ' + str(dias_resto) + ' dia!')
    else:
      print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semana!')
  else:
    if(dias_resto > 1 ):
      print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semanas e ' + str(dias_resto) + ' dias!')
    elif(dias_resto == 1):  
       print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semanas e ' + str(dias_resto) + ' dia!')
    else:
      print(str(num_dias) + ' dias equivalem à ' + str(semanas) + ' semanas!')

