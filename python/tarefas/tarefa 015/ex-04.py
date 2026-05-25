with open("IPLOG.TXT", "w") as f:
        f.write("200.135.80.9\n192.168.1.1\n8.35.67.246\n252.32.4.5\n10.0.0.1\n172.16.5.100\n224.5.3.2\n")
 
print("=== IPs registrados no servidor ===\n")
with open("IPLOG.TXT", "r") as arquivo:
        for linha in arquivo:
            ip = linha.strip()
            if ip:
                print(ip)
 