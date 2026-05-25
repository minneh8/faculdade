
 # Criar arquivo de exemplo para teste
with open("IPLOG.TXT", "w") as f:
        f.write("200.135.80.9\n192.168.1.1\n8.35.67.246\n252.32.4.5\n")
 
with open("IPLOG.TXT", "r") as arquivo:
        linhas = arquivo.readlines()
 
with open("IPLOG_FORMATADO.TXT", "w") as saida:
        print("=== IPs Formatados ===\n")
        for linha in linhas:
            ip = linha.strip()
            if ip:
                partes = ip.split(".")
                # Cada byte alinhado à direita com 3 caracteres
                formatado = f"{int(partes[0]):>3}.{int(partes[1]):>3}.{int(partes[2]):>3}.{int(partes[3]):>3}"
                print(formatado)
                saida.write(formatado + "\n")
 
print("\nArquivo IPLOG_FORMATADO.TXT gerado com sucesso!")
 