"""Não consegui completar essa!"""

n = int(input('Qual o valor de N?'))

#verification of data
dados = input('Digite os dados: ')
dados_list = dados.split(' ')
valores = []

mi = -9999999999999999999999999999999999999999999999

for x in range(0, n):
  
  if(int(dados_list[x]) >= mi):
    
    valores.append(int(dados_list[x]))
    mi = int(dados_list[x])
    
  else:
    
    print('Erro! Conjunto tem de estar em ordem crescente')
    break

#first q (q1)
index_q1 = int(n * (1/4))
q1 = valores[index_q1]

#there q (q3)
index_q3 = int(n * (3/4))
q3= valores[index_q3]

#media
if(n % 2 == 0):
    index_mediana = (n // 2)
    mediana = (valores[index_mediana - 1] + valores[index_mediana]) / 2
else:
    index_mediana = ((n - 1) // 2)
    mediana = valores[index_mediana]
    
#limite inferior e superior

indexLimiteSup = q3 + 1.5 * (q3 - q1)
indexLimiteInf = q1 - 1.5 * (q3 - q1)

limiteSuperior = dados_list[0]
limiteInferior = dados_list[0]

for i in range(0, n):
  if (dados_list[i] < limiteInferior and dados_list[i] > indexLimiteInf):
    limiteInferior = dados_list[i]
  if (dados_list[i] > limiteSuperior and dados_list[i] < indexLimiteSup):
    limiteSuperior = dados_list[i]

print('Limite inferior: ' + str(limiteInferior))
print('1o quartil: ' + str(int(q1)))
print('Mediana: ' + str(mediana))
print('3o quartil: ' + str(int(q3)))
print('Limite superior: ' + str(limiteSuperior))

