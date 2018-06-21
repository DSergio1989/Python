from random import randint
numero = randint(0,10)
contador = 1
guess = int(input("Adivinhe o meu numero: "))
while guess != numero:
    guess = int(input("Tente novamente: "))   
    contador = contador + 1
print ()"Isso! Acertou na", contador, "ª tentativa!")
