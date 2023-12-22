n = int(input('n?'))

for i in range(1, n):
  if((i * (i + 1) * (i + 2)) == n):
    trian = 'é triangular'
    break
  else:
    trian = 'não é triangular'

print(trian)