print("Conversor de Unidade de medidas de temperatura. Selecione uma das Opções abaixo:")
print("1 - Fahrenheit para Celsius")
print("2 - Kelvin para Celsius")
print("3 - Rankine para Celsius")
print("4 - Réaumur para Celsius")

opcao = int(input("Digite a opção desejada: "))

if opcao == 1:
    f = float(input("Digite o valor em Fahrenheit: "))
    c = (f - 32) * 5 / 9
    print("O valor em Celsius é:", c)
elif opcao == 2:
    k = float(input("Digite o valor em Kelvin: "))
    c = k - 273.15
    print("O valor em Celsius é:", c)
elif opcao == 3:
    r = float(input("Digite o valor em Rankine: "))
    c = (r - 491.67) * 5 / 9
    print("O valor em Celsius é:", c)
elif opcao == 4:
    re = float(input("Digite o valor em Réaumur: "))
    c = re * 5 / 4
    print("O valor em Celsius é:", c)
else:
    print("Opção inválida")