cadeia = str(input("Digite uma cadeia de numeros: "))
nchar = len(cadeia)
pos = 0
int1 = 0
int2 = 0
i = 0
while pos != nchar : 
    try: 
        vl = int(cadeia[pos])
        if ((vl >= 0) and (vl <= 5)):
            int1 = int1 + 1      
        elif ((vl >= 6) and (vl <= 9)):
            int2 = int2 + 1
        pos = pos + 1
    except ValueError:
        print("Algo deu errado...")
print(f"O quantidade de numeros que estao no intervalo entre 0 e 5 são: {int1}")
print(f"A quantidade de numeros que estao no intervalo de 6 a 9 são: {int2}")