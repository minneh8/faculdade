#Ler nome e idade de 5 Pessoas
#Armazenar os dados em listas 

#Inicializando variaveis 
nome = []
idade = []
vzs = 0
vlnome = ""
vlidade = 0
while vzs <= 5:
    print(f"Participante {vzs + 1}:")
    vlnome = input("Digite o seu nome: ")
    vlidade = int(input("Digite a sua idade: "))
    print("**************************************\n")

    #Cadastrar os dados lidos, em Listas
    nome.append(vlnome)
    idade.append(vlidade)
    vzs = vzs + 1
print(nome, idade)