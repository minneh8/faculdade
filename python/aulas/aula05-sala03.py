xmax = -1000
ymax = -1000
x = 0
while (x <= 10):
    y = -4 * x ** 2 + 40 * x 
    if( y > ymax):   # Usar IF para identificar, para cada valor de y(x), qual é o maior [Y]
        ymax = y
        xmax = x
    x = x + 1
print(f" x maior = {xmax} e y maior = {ymax}")
    
