senha_correta = "swordfish"
while True:
    senha = input("Informe sua senha: ")
    if senha == senha_correta:
        break
    else:
        print("Senha incorreta!")
