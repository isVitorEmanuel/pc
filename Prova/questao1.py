n = int(input('Quantos números? '))

qntdModa = 0
valoresModaInicial = []
valoresModa = []
numeros = []

for c in range(0, n):
  numeros.append(int(input('Digite o ' + str(c + 1) + 'o ' + 'valor: '  )))

for i in numeros:
  
  qntdI = (numeros.count(i))
  
  if(qntdI > qntdModa):
    qntdModa = qntdI
    valoresModaInicial = [i]
  elif(qntdI == qntdModa):
    valoresModaInicial.append(i)

for k in valoresModaInicial:
  
  if(valoresModaInicial.count(k) > 1):
    if(k not in valoresModa):
      valoresModa.append(k)
  else:
    valoresModa.append(k)

stringValor = ''

for valor in valoresModa:
  stringValor = stringValor + ' '+ str(valor)
  
print('A moda do conjunto é:' + stringValor )
