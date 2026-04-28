#Desenvolver uma aplicação CRUD (Create, Read, Update, Delete) para gerenciar uma lista de listas
#TEMA: Agenda de Contatos
#CAMPOS: Nome, Sexo, Celular, Email, Idade
#Desenvolver um menu de Opcoes para o usuário escolher a opção desejada
#Software Timão. Agenda Timão

#1- Cadastrar
#2- Listar
#3- Alterar   
#4- Deletar
#5- Consultar
#0- Sair

dados= []
opcao = 0
continuar = "S"
print("Bem Vindo ao Software Timão - Agenda de Contatos\n")
while True:
    print("Escolha a opção desejada: \n1- Cadastrar \n2- Listar \n3- Alterar \n4- Deletar \n5- Consultar \n0- Sair\n")
    opcao = int(input("Digite a opção desejada: "))

    match opcao:
        case 1:
            print("-----------/ Opção Cadastrar /----------")
            while ( continuar == "S" or continuar == "s"):
                nome = input("Digite o seu Nome:")
                sexo = input("Digite o seu Sexo:")
                celular = input("Digite o seu Celular:")
                email = input("Digite o seu Email:")
                idade = input("Digite a sua Idade:")
                aux = [nome, sexo, celular, email, idade]
                dados.append(aux)

                print("")
                continuar = input("Deseja cadastrar mais um contato? (S/N)")
        case 2:
            print("-----------/ Opção Listar /----------")
            pos = 0
            tam = len(dados)
            while pos < tam:
                aux = dados[pos]
                nome = aux[0]
                sexo = aux[1]
                celular = aux[2]
                email = aux[3]
                idade = aux[4]
                print(f"\nNome: {nome} / Sexo: {sexo} / Celular: {celular} / Email: {email} / Idade: {idade}\n")
                pos += 1
        case 3:
            print("-----------/ Opção Alterar /----------")
        case 4:
            print("-----------/ Opção Deletar /----------")
        case 5:
            print("-----------/ Opção Consultar /----------")
            if len(dados) == 0:
                print("Não há contatos cadastrados para consultar\n")
                continue
            nomeconsulta = input("Digite o nome do contato que deseja consultar: ")
            pos = 0
            encontrado = False
            while pos < len(dados):
                aux = dados[pos]
                nome = aux[0]
                sexo = aux[1]
                celular = aux[2]
                email = aux[3]
                idade = aux[4]
                if nomeconsulta == nome:
                    print(f"\nNome: {nome} / Sexo: {sexo} / Celular: {celular} / Email: {email} / Idade: {idade}\n")
                    encontrado = True
                    break
                pos += 1
            if encontrado == False:
                print("Contato não encontrado\n")
        case 0:
            print("Saindo do Software Timão")
            break
        case _:
            print("Opção Inválida\n")
            continue