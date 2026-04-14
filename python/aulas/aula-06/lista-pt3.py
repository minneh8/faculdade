#Imprimir nome e idade, Calcular a media
nome = ["Lucas", "João", "Zago", "Vitor", "Bruno"]
idade =[17, 56, 98, 77, 18]

somaidade = 0
pos = 0
nchar = len(nome)
int = len(idade)
while (pos < nchar):
    print(f"O {nome[pos]} tem {idade[pos]} anos")
    somaidade = somaidade + idade[pos]
    pos = pos + 1

media = somaidade / int
print("**********************************************************")
print(f"A Media de idade é {media}")