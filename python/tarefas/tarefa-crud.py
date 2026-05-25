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

dados=[ 
       ["ADAMASTHOR","M","19 912345678","adm@gmail.com",18],
       ["MARISMENIA","F","19 956776564","mari@gmail.com",76],
       ["ONLAYNY","F","19 934786523","onlayny@gmail.com",22],
       ["OFFYLAYNY","F","19 945123278","offylayny@gmail.com",35],
       ["HORKUTYZ","M","19 990091237","hkt@gmail.com",27]
       ]
opcao = 0
continuar = "S"
print("Bem Vindo ao Software Timão - Agenda de Contatos\n")
while True:
    print("Escolha a opção desejada: \n1- Cadastrar \n2- Listar \n3- Alterar \n4- Deletar \n5- Consultar \n6- Gravar dados em um Arquivo \n7- Ler dados de um Arquivo \n0- Sair\n")
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
            if len(dados) == 0:
                print("Não há contatos cadastrados para alterar\n")
                continue
            nomealtera = input("Digite o nome do contato que deseja alterar: ")
            pos = 0
            encontrado = False
            while pos < len(dados):
                if nomealtera == dados[pos][0]:
                    print(f"Contato encontrado: {dados[pos]}")
                    print("Digite os novos dados (Enter para manter o atual):")
                    novo_nome = input(f"Nome [{dados[pos][0]}]: ")
                    novo_sexo = input(f"Sexo [{dados[pos][1]}]: ")
                    novo_celular = input(f"Celular [{dados[pos][2]}]: ")
                    novo_email = input(f"Email [{dados[pos][3]}]: ")
                    novo_idade = input(f"Idade [{dados[pos][4]}]: ")
                    if novo_nome: dados[pos][0] = novo_nome
                    if novo_sexo: dados[pos][1] = novo_sexo
                    if novo_celular: dados[pos][2] = novo_celular
                    if novo_email: dados[pos][3] = novo_email
                    if novo_idade: dados[pos][4] = novo_idade
                    print("Contato alterado com sucesso!\n")
                    encontrado = True
                    break
                pos += 1
            if not encontrado:
                print("Contato não encontrado\n")
        case 4:
            print("-----------/ Opção Deletar /----------")
            if len(dados) == 0:
                print("Não há contatos cadastrados para deletar\n")
                continue
            nomedel = input("Digite o nome do contato que deseja deletar: ")
            pos = 0
            encontrado = False
            while pos < len(dados):
                if nomedel == dados[pos][0]:
                    print(f"Contato encontrado: {dados[pos]}")
                    continuar = input("Tem certeza que deseja deletar? (S/N): ")
                    if continuar == "S" or continuar == "s":
                        dados.pop(pos)
                        print("Contato deletado com sucesso!\n")
                    else:
                        print("Operação cancelada\n")
                    encontrado = True
                    break
                pos += 1
            if not encontrado:
                print("Contato não encontrado\n")
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
        case 6: 
            print("-----------/ Gravar dados em um Arquivo /----------")
            print("Voce deseja gravar os dados do cadrastro em um arquivo? (S/N)")
            continuar = input("Digite S ou N: ")
            for continuar in "S" or "s":
                arq = open("agenda.txt", "w")
                for aux in dados:
                    nome = aux[0]
                    sexo = aux[1]
                    celular = aux[2]
                    email = aux[3]
                    idade = aux[4]
                    arq.write(f"Nome: {nome} / Sexo: {sexo} / Celular: {celular} / Email: {email} / Idade: {idade}\n")
                arq.close()

        case 7:
            print("-----------/ Ler dados de um Arquivo /----------")
            arq = open("agenda.txt", "r")
            print(arq.read())
            arq.close()
        case 0:
            print("Saindo do Software Timão")
            break
        case _:
            print("Opção Inválida\n")
            continue