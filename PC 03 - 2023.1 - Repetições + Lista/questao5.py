"""Para analisar dados coletados (amostras) por estudos científicos, é bastante comum o uso de boxplots, elementos gráficos 
que exibem os seguintes dados sobre uma amostra:

limite superior
limite inferior
1º quartil (valor que se encontra na posição 1/4 do conjunto, considerando o conjunto em ordem crescente)
2o quartil/mediana (valor que se encontra na metade do conjunto, considerando o conjunto em ordem crescente)
3º quartil (valor que se encontra na posição 3/4 do conjunto, considerando o conjunto em ordem crescente)
Veja uma ilustração de Boxplot em https://www.monolitonimbus.com.br/wp-content/uploads/2019/11/boxplot_vert.png

Nesse contexto, crie um programa que lê um conjunto de N números (N > 2). Para isso, o programa deve primeiro ler o valor 
de N e depois a lista de N números reais (float). Os dados devem ser informados na ordem crescente, ou seja, do menor 
valor para o maior, podendo haver elementos repetidos. Em seguida, o programa deve realizar a análise dos dados mostrando 
as informações presentes em um boxplot (limite inferior, o 1º quartil, a mediana, o 3º quartil e o limite superior), 
considerando o seguinte:

Em qualquer iteração do laço de leitura dos N valores, se o valor lido for menor que o anterior, exiba a mensagem: "Erro! 
Conjunto tem de estar em ordem crescente" e pare o programa.
O 1º quartil é o valor na i-ésima posição, onde i == round(N * 1/4).
O 3º quartil é o valor na i-ésima posição, onde i == round(N * 3/4).
A mediana é o elemento central dos dados. Há, porém, dois casos para o "centro". Se N for ímpar, haverá um único "elemento
do meio" (ex: em [1, 3, 5], 3 é central), mas se N for par haverá dois "elementos do meio" (ex: em [1, 3, 4, 6], 3 e 4 são 
centrais). Nesse caso, a mediana será a média dos dois valores do meio.
Como os dados são informados de maneira ordenada, seus valores mínimos e máximos seriam naturalmente considerados como os 
limites inferior e superior. Porém, o boxplot não considera valores extremos (outliers) como limites. Um valor é 
considerado extremo se ele está afastado da mediada por mais de 1,5 o valor do intervalo interquartílico (Terceiro Quartil
 – Primeiro Quartil)."""

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

