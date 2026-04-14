#Ler nome e idade de 5 Pessoas
#Armazenar os dados em listas 
#Calcular a idade media dos Cadastros e indicar a pessoa mais nova e a mais velha 
nome = []
idade = []
somaidade = 0
idademin = 1000
idademax = -1000
posidademin = 0
posidademax = 0
pos = 0
while pos < 5:
    print(f"Participante {pos + 1}:")
    vlnome = input("Digite o seu nome: ")
    vlidade = int(input("Digite a sua idade: "))
    print(f"O(a) Participante {pos + 1}, nome: {vlnome} e idade: {vlidade}")
    print("**************************************\n")
    somaidade = somaidade + vlidade
    if idademin > vlidade:
        idademin = vlidade
        posidademin = pos
    if idademax < vlidade:  
        idademax = vlidade
        posidademax = pos
    nome.append(vlnome)
    idade.append(vlidade)
    pos = pos + 1
    

tam = len(nome)
media = somaidade / tam
if idademin > vlidade:
    idademin = vlidade
if idademax < vlidade:
    idademax = vlidade


print(f"Participante 1 : {nome[0]} tem {idade[0]} anos \nParticipante 2 : {nome[1]} tem {idade[1]} anos \nParticipante 3 : {nome[2]} tem {idade[2]} anos \nParticipante 4 : {nome[3]} tem {idade[3]} anos\nParticipante 5 : {nome[4]} tem {idade[4]} anos\n")
print("************************************************************")
print(f"A idade Media é {media}")
print(f"A Pessoa mais nova é o(a) {nome[posidademin]} com {idademin} anos")
print(f"A Pessoa mais velha é o(a) {nome[posidademax]} com {idademax} anos")