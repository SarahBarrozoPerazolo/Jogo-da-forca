import unicodedata
from util import escolher_palavra

def remover_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def mostrar_estado(palavra, letras_certas, letras_erradas, erros_restantes, tentativas_palavra):
    exibicao = ''
    for letra in palavra:
        if letra == ' ':
            exibicao += '  '  # mostrar espaços visivelmente entre palavras
        elif remover_acentos(letra) in letras_certas:
            exibicao += letra + ' '
        else:
            exibicao += '_ '
    print(f"\nPalavra: {exibicao.strip()}")
    print(f"Letras erradas: {' '.join(letras_erradas)}")
    print(f"Erros restantes: {erros_restantes}")
    print(f"Tentativas de chute da palavra restantes: {2 - tentativas_palavra}")

def jogar_uma_partida(palavras):
    palavra = escolher_palavra(palavras)
    palavra_sem_acentos = remover_acentos(palavra)

    letras_certas = set()
    letras_erradas = set()
    erros = 0
    limite_erros = 6
    tentativas_palavra = 0

    print("\n=== JOGO DA FORCA ===")

    while True:
        mostrar_estado(palavra, letras_certas, letras_erradas, limite_erros - erros, tentativas_palavra)
        tentativa = input("\nDigite uma letra ou chute a palavra: ").lower().strip()

        if not tentativa:
            print("⚠️ Entrada vazia. Tente novamente.")
            continue

        if len(tentativa) == 1:
            if tentativa in letras_certas or tentativa in letras_erradas:
                print("Você já tentou essa letra!")
            elif tentativa in palavra_sem_acentos:
                letras_certas.add(tentativa)
                print("✅ Letra correta!")
            else:
                letras_erradas.add(tentativa)
                erros += 1
                print("❌ Letra errada!")
        else:
            tentativa_sem_acentos = remover_acentos(tentativa)
            if tentativas_palavra >= 2:
                print("❗ Você já usou as 2 tentativas de chute.")
            elif tentativa_sem_acentos == palavra_sem_acentos:
                print(f"\n🎉 Parabéns! Você acertou a palavra: {palavra}")
                break
            else:
                tentativas_palavra += 1
                erros += 1
                print("❌ Palavra errada!")

        if erros >= limite_erros:
            print(f"\n💀 Fim de jogo! A palavra era: {palavra}")
            break

        if all(remover_acentos(letra) in letras_certas or letra == ' ' for letra in palavra):
            print(f"\n🎉 Parabéns! Você acertou a palavra: {palavra}")
            break

