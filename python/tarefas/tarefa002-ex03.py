#Desenvolver um Software para analizar a porcentagem de espectadores de 5 canais de TV

yt = int(input("Digite o numero de espectadores do canal YUTUBUZ :"))
fb = int(input("Digite o numero de espectadores do canal FAYÇY BUKY:"))
xz = int(input("Digite o numero de espectadores do canal XZ:"))
yg = int(input("Digite o numero de espectadores do canal YNZTAGRAN:"))
yf = int(input("Digite o numero de espectadores do canal YSPOTYFAY:"))

#Cálculo
te = yt + fb + xz + yg + yf
pyt = (yt / te) * 100  
pfb = (fb / te) * 100  
pxz = (xz / te) * 100  
pyg = (yg / te) * 100  
pyf = (yf / te) * 100  

print("O percentual de espectadores do canal YUTUBUZ é:", pyt)
print("O percentual de espectadores do canal FAYÇY BUKY é:", pfb)
print("O percentual de espectadores do canal XZ é:", pxz)
print("O percentual de espectadores do canal YNZTAGRAN é:", pyg)
print("O percentual de espectadores do canal YSPOTYFAY é:", pyf)

