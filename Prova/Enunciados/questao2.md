Faça um programa que leia 5 números e imprima todos os números inteiros nos intervalors [n1, n2], [n2, n3], [n3, n4] e [n4, n5]. Observe que para imprimir os intervalos é necessário que n1 > n2 > n3 > n4 > n5, se essa condição não for satisfeita, apenas troque a ordem dos números no intervalo a fim de que o primeiro seja menor do que o segundo.

```
Entrada: N? 4
Digite 5 números:
1
3
4
5
6

Digite 5 números:
9
6
10
2
4
```

```
Saída:
intervalo [1, 3] = 1,2,3
intervalo [3, 4] = 3,4
intervalo [4, 5] = 4,5
intervalo [5, 6] = 5,6

intervalo [6, 9] = 6,7,8,9
intervalo [6, 10] = 6,7,8,9,10
intervalo [2, 10] = 2,3,4,5,6,7,8,9,10
intervalo [2, 4] = 2,3,4
```