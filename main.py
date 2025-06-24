from util import carregar_palavras
from forca import jogar_uma_partida

def main():
    palavras = carregar_palavras()
    if not palavras:
        return

    while True:
        jogar_uma_partida(palavras)
        jogar_novamente = input("\nDeseja jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Até a próxima!")
            break

if __name__ == "__main__":
    main()
    