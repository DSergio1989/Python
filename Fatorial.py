n = int(input("Digite um numero: "))
produto = 1
for i in range(n,1,-1):
    produto = produto*i
print ("Fatorial de ", n, "= ", produto)
