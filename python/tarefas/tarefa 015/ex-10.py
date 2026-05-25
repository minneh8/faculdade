
import random
 
def embaralhar(palavra):
    letras = list(palavra)
    random.shuffle(letras)
    while "".join(letras) == palavra:
        random.shuffle(letras)
    return "".join(letras)
 
def main():
    # Criar arquivo de palavras de exemplo
    with open("PALAVRAS.TXT", "w") as f:
        f.write("PYTHON.Linguagem de programação muito popular\n")
        f.write("ALGORITMO.Sequência de passos para resolver um problema\n")
        f.write("COMPUTADOR.Máquina capaz de processar dados\n")
        f.write("ARQUIVO.Conjunto de dados armazenados em disco\n")
        f.write("VARIAVEL.Espaço de memória para guardar um valor\n")
 
    with open("PALAVRAS.TXT", "r") as f:
        linhas = [l.strip() for l in f.readlines() if l.strip()]
 
    linha_escolhida = random.choice(linhas)
    palavra, dica = linha_escolhida.split(".")
    embaralhada = embaralhar(palavra)
 
    log = open("LOG_ADIVINHE.TXT", "w")
    tentativa = 1
    max_tentativas = 5
    acertou = False
 
    print("=" * 45)
    print("       ADIVINHE A PALAVRA - YUNITY TECH")
    print("=" * 45)
    print(f"\nDica: {dica}")
    print(f"Letras embaralhadas: {embaralhada}")
    print(f"Número de letras: {len(palavra)}")
    print(f"Você tem {max_tentativas} tentativas.\n")
 
    while tentativa <= max_tentativas:
        resposta = input(f"Tentativa {tentativa}/{max_tentativas}: ").strip().upper()
        letras_certas = sum(1 for a, b in zip(resposta, palavra) if a == b) if len(resposta) == len(palavra) else 0
        status = ""
 
        if resposta == palavra:
            acertou = True
            status = "ACERTOU"
            print(f"\n🎉 Parabéns! Você acertou na tentativa {tentativa}!")
            log.write(f"Tentativa {tentativa} | Jogada: {resposta} | Status: ACERTOU\n")
            break
        else:
            if len(resposta) == len(palavra):
                print(f"❌ Errou! Letras na posição correta: {letras_certas}/{len(palavra)}")
            else:
                print(f"❌ A palavra tem {len(palavra)} letras.")
            status = f"ERROU ({letras_certas} letras corretas)"
            log.write(f"Tentativa {tentativa} | Jogada: {resposta} | Status: {status}\n")
            tentativa += 1
 
    if not acertou:
        print(f"\n💀 Fim de jogo! A palavra era: {palavra}")
        log.write(f"Resultado final: PERDEU | Palavra: {palavra}\n")
 
    log.close()
    print("\nLog da partida salvo em LOG_ADIVINHE.TXT")
 
main()
 