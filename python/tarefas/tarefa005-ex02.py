#Desenvolver um Software para o cálculo de IMC
p = float(input("Digite o peso: "))
a = float(input("Digite a altura: "))

#Cálculo
imc = p / (a ** 2)
print(f"o cálculo do seu Indice de Massa Corporal (IMC) é: {imc}")