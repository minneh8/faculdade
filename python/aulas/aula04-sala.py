#Aula de if e else
bs = float(input("Digite o valor da base de calculo: "))

if bs <= 1903.98:
    print(" isento de imposto")
elif bs >= 1903.99 and bs <=2826.65:
    print("Imposto de 7.5%")
elif 2826.66 <= bs <= 3751.05:
    print("Imposto de 15%")
elif 3751.06 <= bs <= 4664.68:
    print("Imposto de 22.5%")
else:
    print("Imposto de 27.5%")..