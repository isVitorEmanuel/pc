nome = input('Informe o nome: ')
nomeCrip = ''
nomeMinus = nome.lower()

alfa = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

for letra in nomeMinus:
  
  indice = alfa.index(letra)
  
  if(letra == ' '):
    nomeCrip = nomeCrip + ' '
  else:
    nomeCrip = nomeCrip + str(alfa[indice + 2])

print('Saída: ' + nomeCrip.upper())