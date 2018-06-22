from random import randint
computador = randint(2,11)
jogador = randint (2,21)
while jogador < 21:
  print ("Jogador:", jogador, "/ computador:", computador)
  continuar = input("Continuar? s/n")
  if continuar == "n":
    break
  else:
    jogador += randint(2,11)
    if jogador >= 21:
      break
print ("Parou")

if jogador > 21 or computador > jogador:
  print ("Perdeu!")
else:
  while computador <= jogador:
    computador += randint(2,11)
    print ("Jogador:", jogador, "/ Computador", computador)
  if computador > jogador and computador <= 21:
    print ("Perdeu!")
  elif computador == jogador:
    print ("Empate.")
  else:
    print ("Venceu!")
