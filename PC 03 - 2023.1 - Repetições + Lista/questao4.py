"""Um treinador de voleibol gostaria de manter estatísticas sobre sua equipe. A cada jogo, seu auxiliar anota quantas 
tentativas de saques, bloqueios e ataques cada um de seus jogadores fez, bem como quantos desses saques, bloqueios e 
ataques tiveram sucesso (resultaram em pontos). Seu programa deve mostrar qual o percentual de saques, bloqueios e ataques
do time todo tiveram sucesso.

Formato de entrada

A primeira entrada é o número de jogadores N (N >= 1). Em seguida, para cada jogador, deve-se se ler uma linha com as 
seguintes informações: nome do jogador, os valores S, B e A, representam a quantidade de tentativas de saques, bloqueios e
ataques; os valores S1, B1 e A1, representando o número de saques, bloqueios e ataques deste jogador que tiveram sucesso.

Formato de saída

A saída deve mostrar o percentual total de saques, bloqueios e ataques do time todo que resultaram em pontos, conforme 
mostrado no exemplo."""

qntd = int(input('Quantidade de Jogadores? '))
jogadores = []
ps, ts, aas = 0, 0, 0
pb, tb, ab = 0, 0, 0
pa, ta, aa = 0, 0, 0

print('Digite os dados para cada jogador: ')

for count in range(0, qntd):
  jogadores.append(input(''))
  jogadores[count] = jogadores[count].split(' ')
  
for i in range(0, len(jogadores)):
  
  ts = ts + int(jogadores[i][1])
  aas = aas + int(jogadores[i][4])
  
  tb = tb + int(jogadores[i][2])
  ab = ab + int(jogadores[i][5])
  
  ta = ta + int(jogadores[i][3])
  aa = aa + int(jogadores[i][6])

ps = (aas/ts) * 100
pb = (ab/tb) * 100
pa = (aa/ta) * 100

print('As estatísticas do jogo são as seguintes: ')
print('Pontos de Saque: ' + str(round(ps, 2)) + '%')
print('Pontos de Bloqueio: ' + str(round(pb, 2)) + '%')
print('Pontos de Ataque: ' + str(round(pa, 2)) + '%')
