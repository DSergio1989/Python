n = int(input("Quantidade de unidades: "))
soma = 0
for contador in range(n):
    nota = float(input("Digite a nota: "))
    soma = soma + nota
media = soma / n
print (media)
