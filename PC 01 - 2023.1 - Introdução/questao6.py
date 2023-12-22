t1 = input("Texto 1? ")
t2 = input("Texto 2? ")
t3 = input("Texto 3? ")

str1 = t1.lower()
str2 = t2.lower()
str3 = t3.lower()

print('Seguem os textos em ordem: ')

if (str1 <= str2 and str1 <= str3):
    print('1o. ' + str1)
    if str2 <= str3:
        print('2o. ' + str2)
        print('3o. ' + str3)
    else:
        print('2o. ' + str3)
        print('3o. ' + str2)
elif str2 <= str1 and str2 <= str3:
    print('1o. ' + str2)
    if str1 <= str3:
        print('2o. ' + str1)
        print('3o. ' + str3)
    else:
        print('2o. ' + str3)
        print('3o. ' + str1)
else:
    print('1o. ' + str3)
    if str1 <= str2:
        print('2o. ' + str1)
        print('3o. ' + str2)
    else:
        print('2o. ' + str2)
        print('3o. ' + str1)
