numerocomputador = 74
numerojogador = -1
while (numerojogador != numerocomputador):    
    numerojogador = int(input("Digite seu numero: "))
    if (numerojogador > numerocomputador):
        print("Seu numeroi é mairo, tente novamente")
    elif (numerojogador < numerocomputador):
        print("Seu numeroi é menor, tente novamente")
    elif (numerojogador == numerocomputador):
        print("Parabens, vocé acertou")