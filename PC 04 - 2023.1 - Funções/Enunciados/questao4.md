O exemplo abaixo mostra que o input() retorna o texto digitado pelo usuário e o split() atua sobre ele quebrando-o 
(separando-o) em partes. No exemplo, como o split() não recebe parâmetro algum, ele utiliza o espaço em branco como 
elemento separador.

```
lista = input("digite os valores: ").split()
print(lista)  # se o usuário digitar "45 62 34 95", será gerada a lista ["45", "62", "34", "95"]
```

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
a função imprimePartes, para imprimir as partes resultantes da separação.

```
Entrada:
N? 9
Qual a sequência?
2
7
3
6
1
2
3
4
8
5
Qual o elemento separador? 3

N? 9
Qual a sequência?
2
7
3
3
3
3
3
4
8
5
Qual o elemento separador? 3

N? 8
Qual a sequência?
3
3
3
4
8
5
3
3
Qual o elemento separador? 3

N? 5
Qual a sequência?
3
3
3
3
3
Qual o elemento separador? 3
```

```
Saída:
Sequências resultantes:
2 7
6 1 2
4 8 5

Sequências resultantes:
2 7
4 8 5

Sequências resultantes:
4 8 5

Sequências resultantes:
Nenhuma
```