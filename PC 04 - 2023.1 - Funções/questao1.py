"""Escreva um programa que faça a criptografia de uma palavra, da seguinte forma:

Letras de "a" até "e" - 1

Letras de "f" até "j" - 2

Letras de "k" até "o" - 3

Letras de "p" até "z" - 4

Espaço ou qualquer outro caracter - 5

O programa deve ter uma função que recebe, como parâmetro de entrada, uma palavra e retorne o valor encriptado 
correspondente. Seu programa deve realizar a leitura do texto fora da função e usá-la bem como seu retorno para imprimir a
saída como os exemplos mostram."""

def encript(nome):
  
  criptografia = ''
  
  for letra in nome:
    
    if letra in ['a', 'b', 'c', 'd', 'e']:
      criptografia = criptografia + '1'
    elif letra in ['f', 'g', 'h', 'i', 'j']:
      criptografia = criptografia + '2'
    elif letra in ['k', 'l', 'm', 'n', 'o']:
      criptografia = criptografia + '3'
    elif letra in ['p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']:
      criptografia = criptografia + '4'
    else:
      criptografia = criptografia + '5'
    
  return criptografia 
  
nome = input('Digite o texto: ')

print('Encriptado: ' + encript(nome.lower()))