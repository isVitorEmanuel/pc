"""Escreva um programa que recebe do usuário dois textos, A e B, e imprime os resultados das operações tamanho(A) - 
tamanho(B), A + B, A contém B, B contém A, primeira letra de A, primeira letra de B, última letra de A, última letra de B."""

a = input('Digite o texto A: ')
b = input('Digite o texto B: ')

print('tamanho(A) - tamanho(B) = ' + str(len(a) - len(b)))
print('A + B = ' + a + b)
print('A contém B = ' + str(b in a))
print('B contém A = ' + str(a in b))
print('Primeira letra de A = ' + a[0])
print('Primeira letra de B = ' + b[0])
print('Última letra de A = ' + a[len(a) - 1])
print('Última letra de B = ' + b[len(b) - 1])