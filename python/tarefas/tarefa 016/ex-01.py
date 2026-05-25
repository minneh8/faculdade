
print("\nGRAVANDO DADOS DE UM ARQUIVO")

arquivo = open('EXEMPLOTXTSEEK001.txt', 'w')

for i in range(10):
    print(format(i, "05d"))
    arquivo.write(format(i, "05d"))

arquivo.close()

print("\nConteúdo gravado no arquivo:")
with open('EXEMPLOTXTSEEK001.txt', 'r') as f:
    conteudo = f.read()

print(f"\nPOSIÇÃO: 1111111111222222222233333333334444444444")
print(f"          01234567890123456789012345678901234567890123456789")
print(f"DADOS   : {conteudo}")

print("\nCada valor ocupa 5 caracteres.")
print("Para localizar o número N, basta multiplicar por 5:")
print("  número 3: inicia na posição 5 * 3 = 15 e termina na posição 19")