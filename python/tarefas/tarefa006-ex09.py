print("Sistema para o calculo do Indice de Massa Corporal (IMC)")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

imc = peso / (altura ** 2)

if imc < 18.5:
    print("A sua classificação de IMC é: Baixo Peso")
elif imc >= 18.5 and imc < 25:
    print("A sua classificação de IMC é: Normal")
elif imc >= 25 and imc < 30:
    print("A sua classificação de IMC é: Sobrepeso")
elif imc >= 30:
    print("A sua classificação de IMC é: Obesidade")