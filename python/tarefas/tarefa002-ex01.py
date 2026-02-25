#Software para o cálculo do volume dos solidos 

# Cubo: *******************************************
vl = float(input("DIgite o valor da aresta do cubo:"))

#Cálculo
vc = vl ** 3
print("O volume do cubo é:", vc)

# Esfera  *******************************************
vr = float(input("Digite o valor do raio da esfera:"))

#Cálculo
ve = 4 * (vr ** 3)  #Considerando PI = 3
print("O volume da esfera é:", ve)

#Cilindro *******************************************
ac = float(input("Digite o valor da altura do cilindro:"))
rc = float(input("Digite o valor do raio do cilindro:"))

#Cálculo
vc = 3 * (rc ** 2) * ac    #Considerando PI = 3
print("O volume do cilindro é:", vc)

#Paralelepipedo *******************************************
cp = float(input("Digite o valor da comprimento do paralelepipedo:"))
lp = float(input("Digite o valor da largura do paralelepipedo:"))
ap = float(input("Digite o valor da altura do paralelepipedo:"))

#Cálculo
vp = cp * lp * ap
print("O volume do paralelepipedo é:", vp) 

#Piramide de base retangular *******************************************
ap = float(input("Digite o valor da altura da piramide:"))
cb = float(input("Digite o comprimento da base da piramide: "))
lb = float(input("Digite a largura da base da piramide: "))

#Cálculo
ab = cb * lb
vp = ab * ap / 3
print("O volume da piramide de base retangular é:", vp)

#Piramide de base triangular *******************************************
ap = float(input("Digite o valor da altura da piramide:"))
ab = float(input("Digite a altura da base da piramide: "))
lb = float(input("Digite o valor do lado da base da piramide: "))

#Cálculo
vp = ab * ap * lb / 6
print("O volume da piramide de base triangular é:", vp)

#Piramide de base circular *********************************************
ap = float(input("Digite o valor da altura da piramide:"))
rb = float(input("Digite o valor do raio da base da piramide: "))

#Cálculo
vc = (rb ** 2) * ap #Considerando PI = 3
print("O volume da piramide de base circular é:", vc)

#Tronco de Cone *********************************************
at = float(input("Digite o valor do tronco:"))
rb = float(input("Digite o valor do raio da base maior: "))
rm = float(input("Digite o valor do raio da base menor: "))

#Cálculo
vt = at * ((rb ** 2) + (rm ** 2) + (rb * rm))     #Considerando PI = 3
print("O volume da piramide de base circular é:", vt)