import random

CAMINHO_PALAVRAS = r"C:\Users\barro\OneDrive\Documentos\Python\jogo_da_forca\palavras.txt"

def carregar_palavras():
    try:
        with open(CAMINHO_PALAVRAS, "r", encoding="utf-8") as arquivo:
            return [linha.strip().lower() for linha in arquivo if linha.strip()]
    except FileNotFoundError:
        print(f"Arquivo '{CAMINHO_PALAVRAS}' não encontrado.")
        return []

def escolher_palavra(palavras):
    return random.choice(palavras)

