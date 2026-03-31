codigo = input("Digite seu Codigo para verificação: ")
nchar = len(codigo)

try:
    while nchar == 7:
        c1 = int(codigo[0])
        c2 = int(codigo[1])
        c3 = int(codigo[2])
        c4 = int(codigo[3])
        c5 = int(codigo[4])
        c6 = int(codigo[5])
        c7 = int(codigo[6])
        cv = (c1 + c2 + c3 + c4 + c5 + c6) % 10
        if cv == c7:
            print("Codigo Valido!")
            break
        else:
            print("Codigo invalido! ")
            break
except: 
    print("Opss, Erro...")
