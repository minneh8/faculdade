

print("=" * 50)
print("PARTE 1 - LEITURA COM SEEK")
print("=" * 50)

# Abrir o arquivo para leitura
arquivo = open('EXEMPLOTXTSEEK001.txt', 'r')

# Reposicionar o ponteiro: 3 * 5 = 15
arquivo.seek(3 * 5, 0)

# Leitura de 5 caracteres
caracteres = arquivo.read(5)
print("CARACTERES LIDOS: ", caracteres)

valor = int(caracteres)
print("VALOR: ", valor)

arquivo.close()


print("\n" + "=" * 50)
print("PARTE 2 - ESCRITA COM SEEK (substituição)")
print("=" * 50)

# Mostrar conteúdo ANTES da substituição
with open('EXEMPLOTXTSEEK001.txt', 'r') as f:
    print("ANTES: ", f.read())

# Abrir o arquivo para leitura e escrita
arquivo = open('EXEMPLOTXTSEEK001.txt', 'r+')

# Reposicionar o ponteiro: 3 * 5 = 15
arquivo.seek(3 * 5, 0)

# Escrever o valor 123 sobre 00003
arquivo.write(format(123, "05d"))

arquivo.close()

# Mostrar conteúdo DEPOIS da substituição
with open('EXEMPLOTXTSEEK001.txt', 'r') as f:
    print("DEPOIS:", f.read())