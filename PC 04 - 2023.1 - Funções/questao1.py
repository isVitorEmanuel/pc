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