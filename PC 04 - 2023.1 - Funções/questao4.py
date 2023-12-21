"""O exemplo abaixo mostra que o input() retorna o texto digitado pelo usuário e o split() atua sobre ele quebrando-o 
(separando-o) em partes. No exemplo, como o split() não recebe parâmetro algum, ele utiliza o espaço em branco como 
elemento separador.

lista = input("digite os valores: ").split()
print(lista)  # se o usuário digitar "45 62 34 95", será gerada a lista ["45", "62", "34", "95"]
O que o split() faz é buscar o elemento separador no texto e utilizar as posições em que ele se encontra como posição de 
separação, gerando uma lista de valores. Alguns algoritmos de Bioinformática realizam um procedimento semelhante, 
inclusive sobre listas numéricas. Faz-se uma busca de padrões sobre uma sequência e quebra-se a sequência em menores, sem 
o padrão utilizado. Por exemplo, realizar a quebra da sequência [ 2, 7, 3, 6, 1, 2, 3, 4, 8, 5 ] usando o 3 como elemento 
separador irá resultar nas subsequências [ 2, 7 ], [ 6, 1, 2 ] e [ 4, 8, 5 ].

Implemente uma função semelhante ao split(), porém sobre listas numéricas. Sua função deve se chamar imprimePartes e 
receber dois parâmetros, a lista e o elemento separador. A função então deve imprimir as listas geradas durante o processo
de quebra. Caso haja mais de uma ocorrência consecutiva do elemento separador, não devem ser geradas listas vazias. Por 
exemplo, na quebra da sequência [ 2, 7, 3, 3, 3, 3, 3, 4, 8, 5 ] pelo valor 3, apenas as sequências [ 2, 7 ] e [ 4, 8, 5 ]
são geradas. O mesmo vale no caso do elemento separador se encontrar no início ou no final da sequência. Por exemplo, a 
quebra de [ 3, 3, 3, 4, 8, 5, 3, 3 ] irá gerar apenas a sequência [ 4, 8, 5 ].

Escreva então um programa que lê do usuário um valor N, uma sequência numérica com N valores e o valor dor separador. Use 
a função imprimePartes, para imprimir as partes resultantes da separação."""

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

