ano = int(input("Digite o ano que seu imovel foi construido: "))

idade = 2026 - ano

if idade < 5: 
    print("Seu imovel não tem desconto no IPTU")
elif idade >= 5 and idade < 20:
    print("O valor do desconto no IPTU do seu imovel é de 15%")
elif idade >= 20 and idade < 40:
    print("O valor do desconto no IPTU do seu imovel é de 25%")
elif idade >= 40:
    print("O valor do desconto no IPTU do seu imovel é de 30%")