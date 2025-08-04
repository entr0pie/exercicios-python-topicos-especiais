
def eh_palindromo(palavra: str) -> bool:
    tamanho = len(palavra)
    maximo_esquerda = tamanho

    for letra_esquerda in range(0, maximo_esquerda):
        letra_direita = tamanho - letra_esquerda - 1
        caracter_a_esquerda, caracter_a_direita = palavra[letra_esquerda], palavra[letra_direita]
        
        if caracter_a_esquerda != caracter_a_direita:
            return False

    return True

palavra = input('? Digite uma palavra para checar se é palíndromo: ')
print(f"É palíndromo? {eh_palindromo(palavra)}")