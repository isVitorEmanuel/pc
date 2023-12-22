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