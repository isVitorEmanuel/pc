a = input('Digite o texto A: ')
b = input('Digite o texto B: ')

a_um = a[0:len(a)//2]
a_do = a[(len(a)//2):len(a)]
b_um = b[0:len(b)//2]
b_do = b[(len(b)//2):len(b)]

print('Texto A dividido em duas partes: ' + a_um + ' e ' + a_do)
print('Texto B dividido em duas partes: ' + b_um + ' e ' + b_do)
print(a_um + ' + ' + b_do + ' = ' + a_um + b_do)
print(a_do + ' + ' + b_um + ' = ' + a_do + b_um)
print(a[0] + ' + ' + b[1] + ' + ' + a[len(a) - 1] +  ' + ' + b[len(b) - 1] + ' = ' + a[0] + b[1] + a[len(a) - 1] + b[len(b) - 1])
