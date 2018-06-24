def divisao_inteira():
    print("---DIVISAO DE DOIS NUMEROS INTEIROS---")
    numero1 = int(input("Digite um numero: "))
    numero2 = int(input("Digite outro numero: "))
    divisao = int(numero1/numero2)
    if numero1%numero2 == 0:
        print()
        print(numero1, "/", numero2, ":", divisao)
    else:
        print()
        print(numero1, "/", numero2, ":", divisao, "com resto", numero1%numero2)
        
divisao_inteira()
