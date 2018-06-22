from random import randint
vitoria1 = 0
vitoria2 = 0
rodadas = int(input("Numero de rodadas: "))
for i in range(rodadas):
    minha_escolha = input("pedra, papel ou tesoura? ")
    computador = randint(1,3)
    if minha_escolha == 'pedra':
        if computador == 1:
            print ("Empate")
        elif computador == 2:
            print ("Jogador 2")
            vitoria2 += 1
        else:
            print ("Jogador 1")
            vitoria1 += 1
            
    if minha_escolha == 'papel':
        if computador == 1:
            print ("JOgador 1")
            vitoria1 += 1
        elif computador == 2:
            print ("Empate")
        else:
            print ("Jogador 2")
            vitoria2 += 1
            
    if minha_escolha == 'tesoura':
        if computador == 1:
            print ("Jogador 1")
            vitoria1 += 1
        elif computador == 2:
            print ("Jogador 2")
            vitoria2 += 1
        else:
            print ("Empate")
                
print ("Placar final: ", vitoria1, "X", vitoria2)

if vitoria1 == vitoria2:
  print ("Opa, deu empate.")
elif vitoria1 > vitoria2:
    print ("Partida vencida pelo jogador 1")
else:
    print ("Partida vencida pelo jogador 2")
 


