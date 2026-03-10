try:
    print("Sistema para o calculo do Indice de Massa Corporal (IMC)")

    print("-------------------------------------------------------")
    peso = float(input("Digite o seu peso: "))
    print("-------------------------------------------------------")
    altura = float(input("Digite a sua altura: "))
    print("-------------------------------------------------------")

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("A sua classificação de IMC é: Baixo Peso")
    elif imc >= 18.5 and imc < 25:
        print("A sua classificação de IMC é: Normal")
    elif imc >= 25 and imc < 30:
        print("A sua classificação de IMC é: Sobrepeso")
    elif imc >= 30 and imc < 35:
        print("A sua classificação de IMC é: Obesidade")
    elif imc >= 35 and imc < 40:
        print("A sua classificação de IMC é: Obesidade 2")
    elif imc >= 40:
        print("A sua classificação de IMC é: Obesidade 3")
except ValueError:
    print("-------------------------------------------------------")
    print("ERRO: O peso e a altura precisa ser um valor numerico!")

except ZeroDivisionError:
    print("-------------------------------------------------------")
    print("ERRO: O valor da altura nao pode ser ZERO!")