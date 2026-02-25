ll = float(input("Digite o valor da largura da local: "))
cl = float(input("Digite o valor da comprimento da local: "))
la = float(input("Digite o valor da largura do azulejo: "))
ca = float(input("Digite o valor da comprimento do azulejo: "))

#Cálculo
al = ll * cl
aa = la * ca
qa = al // aa
print("A quantidade de azulejos para ultilizar no  local é:", qa)