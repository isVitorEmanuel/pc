Escreva um programa que pede ao usuário um texto e dois números inteiros i1 e i2. Após lidas as entradas o programa faz as seguintes verificações:
    * Se i1 > i2 troque os valores de i1 e i2
    * Se i1 ou i2 forem maiores ou iguais ao tamanho do texto lido, finalize o programa avisando ao usuário que os valores tem que ser menores do que o tamanho do texto.
Após feitas as verificações, o programa deverá imprimir partes do texto conforme as especificações abaixo:
    * Parte 1: equivale à parte do texto que vai da primeira letra até o índice i1
    * Parte 2: equivale à parte do texto que vai da primeira letra até o índice i2 
    * Parte 3: equivale à parte do texto que vai da letra de índice i1 letra até o índice i2
    * Parte 4: equivale à parte do texto que vai da letra de índice i1 até o final do texto
    * Parte 5: equivale à parte do texto que vai da letra de índice i2 até o final do texto

```
Entrada:
texto? teste_texto
i1? 1
i2? 5

texto? teste_texto
i1? 5
i2? 1

texto? teste_texto
i1? 1
i2? 11

texto? Lorem ipsum dolor sit amet, consectetur adipiscing elit.
i1? 20
i2? 50
```

```
Saída:
Partes
Parte 1: t
Parte 2: teste
Parte 3: este
Parte 4: este_texto
Parte 5: _texto

Partes
Parte 1: t
Parte 2: teste
Parte 3: este
Parte 4: este_texto
Parte 5: _texto

Erro! índices precisam ser menores do que o tamanho do texto (11)

Partes
Parte 1: Lorem ipsum dolor si
Parte 2: Lorem ipsum dolor sit amet, consectetur adipiscing
Parte 1: t amet, consectetur adipiscing
Parte 1: t amet, consectetur adipiscing elit.
Parte 1:  elit.
```