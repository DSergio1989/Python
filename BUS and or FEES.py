for numero in range(-25,50):
    if numero%2==0 and numero%3==0:
        print(numero, "BUS e FEES")
    elif numero%2==0:
        print(numero, "BUS")
    elif numero%3==0:
        print(numero, "FEES")
    else:
        print (numero, "")
