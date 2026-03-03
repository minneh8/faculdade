prova1 = float(input("Digite a nota da Prova 1: "))
prova2 = float(input("Digite a nota da Prova 2: "))
peso1 = float(input("Digite o valor do peso 1: "))
peso2 = float(input("Digite o valor do peso 2: "))
#Calculo da media
media = ((peso1 * prova1) + (peso2 * prova2)) / (peso1 + peso2)

if media < 5:
    print("REPROVADO")
elif media >= 5 and media < 8:
    print("APROVADO")
elif media  >= 8 and media < 9:
    print("PARABENS O DESEMPENHO FOI MUITO BOM!")
else:
    print("PARABENS, VOCE FOI APROVADO COM LOUVOR!")

print("Sua media é:", media)