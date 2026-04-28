dados= []
opcao = "s"
while ( opcao == "S" or opcao == "s"):
    nome = input("Digite o seu Nome:")
    celular = input("Digite o seu Celular:")
    email = input("Digite o seu Email:")
    aux = [nome, celular, email]
    dados.append(aux)

    print("")
    opcao = input("Deseja cadastrar mais um contato? (S/N)")
pos = 0
tam = len(dados)
while pos < tam:
    aux = dados[pos]
    nome = aux[0]
    celular = aux[1]
    email = aux[2]
    print(f"Nome: {nome} / Celular: {celular} / Email: {email} \n")
    pos += 1