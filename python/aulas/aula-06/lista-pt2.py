#Calcular a media de idade dos valores cadastrados na lista 
idade =[17, 56, 98, 77, 18]

print (f"\n {idade} \n")
pos = 0
int = len(idade)
media = (idade[0] + idade[1] + idade[2] + idade[3] + idade[4]) / int
while(pos < int):
    print(f"{pos} \t {idade[pos]} anos")
    pos = pos + 1
print("\n *************************************************\n")
print (f"A Media é {media}\n")