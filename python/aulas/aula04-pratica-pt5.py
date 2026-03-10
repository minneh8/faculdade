try: 
    nota1 = float(input("Digite a Nota 1: "))
    nota2 = float(input("Digite a Nota 2: "))

    media = (nota1 + nota2) / 2
    print("MEDIA :", media)
except:
    print("Ops, ERRO: Por favor, digitar somente valores numericos!")