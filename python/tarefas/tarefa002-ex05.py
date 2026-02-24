#Desenvolver um Software para inverter os valores das variaveis

# Entrada
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))


z = x
x = y
y = z

# Resultado
print("Após a troca:")
print("X =", x)
print("Y =", y)