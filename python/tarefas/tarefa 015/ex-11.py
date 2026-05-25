import random
 
FORCA = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
========="""
]
 
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
 
    letras_erradas = []
    letras_certas = []
    max_erros = len(FORCA) - 1
    log = open("LOG_FORCA.TXT", "w")
 
    print("=" * 45)
    print("         JOGO DA FORCA - YUNITY TECH")
    print("=" * 45)
    print(f"\nDica: {dica}\n")
 
    while True:
        erros = len(letras_erradas)
        print(FORCA[erros])
 
        # Mostrar palavra com letras descobertas
        exibir = " ".join(l if l in letras_certas else "_" for l in palavra)
        print(f"\nPalavra: {exibir}")
        print(f"Letras erradas: {', '.join(letras_erradas) if letras_erradas else '-'}")
        print(f"Erros: {erros}/{max_erros}\n")
 
        if "_" not in exibir:
            print("🎉 Parabéns! Você venceu!")
            log.write(f"Jogada final | Palavra: {palavra} | Status: VENCEU\n")
            break
 
        if erros >= max_erros:
            print(f"\n💀 Você perdeu! A palavra era: {palavra}")
            log.write(f"Jogada final | Palavra: {palavra} | Status: PERDEU\n")
            break
 
        letra = input("Digite uma letra: ").strip().upper()
 
        if not letra.isalpha() or len(letra) != 1:
            print("Por favor, digite apenas uma letra.")
            continue
 
        if letra in letras_certas or letra in letras_erradas:
            print("Letra já tentada!")
            continue
 
        if letra in palavra:
            letras_certas.append(letra)
            status = f"CERTA"
        else:
            letras_erradas.append(letra)
            status = f"ERRADA"
 
        log.write(f"Letra: {letra} | Status: {status} | Erros: {len(letras_erradas)}\n")
 
    log.close()
    print("\nLog da partida salvo em LOG_FORCA.TXT")
 
main()