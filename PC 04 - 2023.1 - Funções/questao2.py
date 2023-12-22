def saldo(valorSaldo):
  print(str('O seu saldo atual é de: ') + str(valorSaldo)) 
  
def saque(valorSaldo):
  
  valor_sacado = float(input('Qual valor você deseja sacar?'))
  
  if valor_sacado <= valorSaldo:
    valorSaldo =  valorSaldo - valor_sacado
    print('Saque autorizado.' + 'Agora o seu saldo atual é de: ' + str(valorSaldo) )
  else:
    print('Saldo insuficiente.')
  
  return valorSaldo

def deposito(valorSaldo):
  
  valor_deposito = float( input('Qual o valor que você quer depositar?') )
   
  if valor_deposito > 0:
    valorSaldo =  valorSaldo + valor_deposito
    print(str('O seu saldo agora é de: ') + str(valorSaldo) )
  else:
    print('Valor inválido')
  
  return valorSaldo
  
def exibeOpcoes():
  
  print('Qual operacao voce deseja realizar?')
  print('1 - SAQUE')
  print('2 - DEPOSITO')
  print('3 - SALDO')
  print('4 - SAIR')
  opcao = int(input('Escolha:'))
  
  return opcao
  
def processaOpcoes(opcao, valorSaldo):

  if(opcao == 1):
    valorSaldo = saque(valorSaldo)
  elif(opcao == 2):
    valorSaldo = deposito(valorSaldo)
  elif(opcao == 3):
    saldo(valorSaldo)
  else:
    print('Obrigado por usar os serviços do Caixa Eletrônico')
    
  return valorSaldo
  
def principal():
  opcao = 0
  saldo = 1000

  while opcao != 4:
    
    opcao = exibeOpcoes()
    saldo = processaOpcoes(opcao, saldo)
    
    
principal()

