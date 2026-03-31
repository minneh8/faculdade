i = 0
quant = 0
while i < 100:
    try:
        if i % 3 == 0:
            print(f"{i} É Divisivel por 3")
            quant = quant + 1
        i = i + 1
    except ZeroDivisionError:
        print("Divisão por Zero") 
print(f"A quantidade de numeros que são divisiveis por 3 nesse intervalo é de: {quant} ")

