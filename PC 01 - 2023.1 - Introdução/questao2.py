import math

x = int(input('x?'))
y = int(input('y?'))
z = int(input('z?'))

cal_one = (x**2 + y**2 + z**2)**(1/3)
cal_two = (x**y + y**z)
cos_sen = math.sin(x**2 + y**2) + math.cos(y**2 + z**2)
log =(math.log(x) + math.log(y) + math.log(z))**(2 + 3 + 2)

print('(' + str(x) + '^2 + ' + str(y) + '^2 + ' + str(z) + '^2)^1/3 = ' + str(cal_one))
print(str(x) + '^' + str(y) + ' + ' + str(y) + '^' + str(z) + ' = ' + str(cal_two))
print('cos(' + str(x) + '^2' + ' + ' + str(y) + '^2)' ' + sin(' + str(y) + '^2' + ' + ' + str(z) + '^2)'  + ' = ' + str(cos_sen))
print('(log ' + str(x) + ' + log ' + str(y) + ' log ' + str(z) + ') ^ (' + str(x) + ' + ' + str(y) + ' + ' + str(z) + ') = ' + str(log))

