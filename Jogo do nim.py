import os
J1PONTOS = 0
J2PONTOS = 0
ganhador = True
print("SEJA BEM-VENDO AO JOGO DO NIM !!!")
print("DIGITE O NOME DO JOGADOR 1")
j1NOME = input()
print("DIGITE O NOME DO JOGADOR 2")
j2NOME = input()
os.system('cls' if os.name == 'nt' else 'clear')
print("No total o jogo tem 33 palitos")
print("o jogo tem 5 rodadas")
for c in range(5):
  os.system('cls' if os.name == 'nt' else 'clear')
  print(f"{j1NOME} {J1PONTOS} vs {J2PONTOS} {j2NOME}")
  enter = input("Presione enter para continuar")
  os.system('cls' if os.name == 'nt' else 'clear')
  palitoTotal = 33
  if ganhador == True:
    while palitoTotal > 0:
     print(f"vez do {j1NOME}")
     print("pode retirar no maximo 5 palitos")
     print(f"palitos restante: {palitoTotal}")
     jogadas = int(input())
     while jogadas!=1 and jogadas!=2 and jogadas!=3 and jogadas!=4 and jogadas!=5:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("NUMERO ERRADO SO PODE RETIRAR NO MAXIMO 5 PALITOS")
       print(f"palitos restante: {palitoTotal}")
       jogadas = int(input())
     if palitoTotal - jogadas <= 0:
       J2PONTOS += 1
       ganhador = False
       break    
     os.system('cls' if os.name == 'nt' else 'clear')
     palitoTotal = palitoTotal - jogadas
     print(f"vez do {j2NOME}")
     print("pode retirar no maximo 5 palitos")
     print(f"palitos restante: {palitoTotal}")
     jogadas = int(input())
     while jogadas!=1 and jogadas!=2 and jogadas!=3 and jogadas!=4 and jogadas!=5:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("NUMERO ERRADO SO PODE RETIRAR NO MAXIMO 5 PALITOS")
       print(f"palitos restante: {palitoTotal}")
       jogadas = int(input())
     if palitoTotal - jogadas <= 0:
      J1PONTOS += 1
      break
     os.system('cls' if os.name == 'nt' else 'clear')
     palitoTotal = palitoTotal - jogadas
  else:
    while palitoTotal > 0:
     print(f"vez do {j2NOME}")
     print("pode retirar no maximo 5 palitos")
     print(f"palitos restante: {palitoTotal}")
     jogadas = int(input())
     while jogadas!=1 and jogadas!=2 and jogadas!=3 and jogadas!=4 and jogadas!=5:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("NUMERO ERRADO SO PODE RETIRAR NO MAXIMO 5 PALITOS")
       print(f"palitos restante: {palitoTotal}")
       jogadas = int(input())
     if palitoTotal - jogadas <= 0:
       J1PONTOS += 1
       ganhador = True
       break    
     os.system('cls' if os.name == 'nt' else 'clear')
     palitoTotal = palitoTotal - jogadas
     print(f"vez do {j1NOME}")
     print("pode retirar no maximo 5 palitos")
     print(f"palitos restante: {palitoTotal}")
     jogadas = int(input())
     while jogadas!=1 and jogadas!=2 and jogadas!=3 and jogadas!=4 and jogadas!=5:
       os.system('cls' if os.name == 'nt' else 'clear')
       print("NUMERO ERRADO SO PODE RETIRAR NO MAXIMO 5 PALITOS")
       print(f"palitos restante: {palitoTotal}")
       jogadas = int(input())
     if palitoTotal - jogadas <= 0:
      J2PONTOS += 1
      break
     os.system('cls' if os.name == 'nt' else 'clear')
     palitoTotal = palitoTotal - jogadas
os.system('cls' if os.name == 'nt' else 'clear')
print("FIM DE JOGO")
print(f"{j1NOME} {J1PONTOS} vs {J2PONTOS} {j2NOME}")
if J1PONTOS>J2PONTOS:
  print(f"{j1NOME} É GRANDE GANHADOR")
else:
 print(f"{j2NOME} É GRANDE GANHADOR")
