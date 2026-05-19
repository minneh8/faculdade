dados = open("dados-prova.txt", "w", encoding="utf-8")
continuar = "S"
lista = []
aux = []
somaidade = 0
controle = 0
maior = 0
menor = 0
while continuar == "S" or continuar == "s":
    nome = input("Digite o nome: ")
    idade = input("Digite a idade: ")
    nota = input("Digite a nota qualidade de vida: ")
    dados.write(f"{nome} , {idade} , {nota}\n")
    aux = [nome, idade, nota]
    lista.append(aux)
    continuar = input("Deseja cadastrar mais um contato? (S/N) ")
    if continuar == "N" or continuar == "n":
        break
controle = len(lista)
for i in range(controle):
    idade = int(lista[i][1])
    nota = int(lista[i][2])
    somaidade += idade
    if nota > 8:
        maior += 1
    else:
        menor += 1
media = somaidade / controle
porcentagemMaior = (maior / controle) * 100
porcentagemMenor = (menor / controle) * 100

print(f"A media das idades dos contatos cadastrados foi: {media}")
print(f"A porcentagem de pessoas com nota maior que 8 foi: {porcentagemMaior}%")
print(f"A porcentagem de pessoas com nota menor que 8 foi: {porcentagemMenor}%")
dados.close()




        