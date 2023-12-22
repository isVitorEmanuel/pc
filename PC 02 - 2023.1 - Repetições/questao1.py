n1 = int(input('n1? '))
n2 = int(input('n2? '))
num_primos = ''
div = 0

if(n1 > n2):
  n1, n2 = n2, n1

for num in range(n1, n2 + 1):
  div = 0
  if(num % 2 != 0):
    
    for i in range(1, num + 1):
      if(num % i == 0):
        div += 1
    
    if(div != 2):
      num_primos = num_primos + str(num) + ', '
      
num_primos = num_primos[0:len(num_primos) - 2]

print('números ímpares não primos [' + str(n1) + '-' + str(n2) +']: ' + num_primos)
