quantidade = (int(input("Quantidade de limoes? ")))
n = 1
resultado = 0

# calcula o maximo de camadas com X limões
while resultado < quantidade:
     c = (n*(n+1))/2 # calcula quantos limões tem na camada n
     resultado = resultado + c
     n = n + 1

if quantidade - resultado <= 1:
  n = n - 1
  camada = 1
  while quantidade > 0:
    c = (n*(n+1))/2
    
    if quantidade - c >= 0:
      quantidade = quantidade - c
      print ("camada ", camada, "com", c, "limões" )
      n = n - 1
      camada = camada + 1
    elif quantidade - c < 0:
      if (c - quantidade) == 1:
        print ("camada ", camada, "com", quantidade, "limões" )
        quantidade = quantidade - c
      else:
        n = n - 1
    else:
      print ()     
