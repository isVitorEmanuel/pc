def text_prompt(msg):
  try:
    return raw_input(msg)
  except NameError:
    return input(msg)

def upRange(start, stop, step):
  while start <= stop:
    yield start
    start += abs(step)

def downRange(start, stop, step):
  while start >= stop:
    yield start
    start -= abs(step)


intervalo = ''
numerosLista = []
print('Digite 5 valores:')
for i in range(1, 6):
  numero = float(text_prompt(''))
  numerosLista.append(int(numero))
for k in range(1, 5):
  
  if numerosLista[int(k - 1)] < numerosLista[int((k + 1) - 1)]:
    j_start = float(numerosLista[int(k - 1)])
    j_end = float(numerosLista[int((k + 1) - 1)])
    for j in (j_start <= j_end) and upRange(j_start, j_end, 1) or downRange(j_start, j_end, 1):
      if j == numerosLista[int((k + 1) - 1)]:
        intervalo = str(intervalo) + str(int(j))
      else:
        intervalo = str(intervalo) + str(str(int(j)) + str(','))
    print(''.join([str(x) for x in ['Intervalo: [', numerosLista[int(k - 1)], ',', numerosLista[int((k + 1) - 1)], ']', ' = ', intervalo]]))
    intervalo = ''
  else:
    j_start2 = float(numerosLista[int((k + 1) - 1)])
    j_end2 = float(numerosLista[int(k - 1)])
    for j in (j_start2 <= j_end2) and upRange(j_start2, j_end2, -1) or downRange(j_start2, j_end2, -1):
      if j == numerosLista[int((k + 1) - 1)]:
        intervalo = str(intervalo) + str(int(j))
      else:
        intervalo = str(intervalo) + str(str(',') + str(int(j)))
    print(''.join([str(x2) for x2 in ['Intervalo: [', numerosLista[int((k + 1) - 1)], ',', numerosLista[int(k - 1)], ']', ' = ', intervalo]]))
    intervalo = ''