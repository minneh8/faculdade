def classificar_ip(ip):
    primeiro_byte = int(ip.split(".")[0])
    if 0 <= primeiro_byte <= 127:
        return "A"
    elif 128 <= primeiro_byte <= 191:
        return "B"
    elif 192 <= primeiro_byte <= 223:
        return "C"
    elif 224 <= primeiro_byte <= 239:
        return "D"
    elif 240 <= primeiro_byte <= 255:
        return "E"
    return "?"
 
def main():
    # Criar arquivo de exemplo para teste
    with open("IPLOG.TXT", "w") as f:
        f.write("200.135.80.9\n192.168.1.1\n8.35.67.246\n252.32.4.5\n10.0.0.1\n172.16.5.100\n224.5.3.2\n")
 
    contagem = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}
 
    with open("IPLOG.TXT", "r") as arquivo:
        for linha in arquivo:
            ip = linha.strip()
            if ip:
                classe = classificar_ip(ip)
                contagem[classe] += 1
 
    print("=== Contagem de IPs por Classe ===\n")
    for classe, total in contagem.items():
        print(f"Classe {classe}: {total} IP(s)")
 
main()