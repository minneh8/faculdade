l1 = int(input("Digite o lado um do triangulo: "))
l2 = int(input("Digite o lado dois do triangulo: "))
l3 = int(input("Digite o lado tres triangulo: "))

if l1 == l2 and l1 == l3:
    print("É um Triangulo equilatero")
elif l1 == l2 or l2 == l3 or l1 == l3:
    print("É um Triangulo Isosceles") 
else:
    print("É um Triangulo Escaleno")