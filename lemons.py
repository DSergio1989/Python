quantidade = (int(input("Quantidade de limoes? ")))
n = 1
resultado = 0

# calcula o maximo de camadas com X limões
while resultado < quantidade-1:
     c = (n*(n+1))/2 # calcula quantos limões tem na camada n
     resultado = resultado + c
     n = n + 1
     camada = c + c
    
if quantidade - resultado <= 1:
  camada = 1
  while quantidade > 0:
    c = (n*(n+1))/2
    quantidade = quantidade - c
    
    if quantidade > 0:
      print ("camada ", camada, "com", c, "limões" )
      n = n - 1
      camada = camada + 1
    else:
      print ("Camada", camada, "com", quantidade+c, "limões")
      camada = camada + 1
