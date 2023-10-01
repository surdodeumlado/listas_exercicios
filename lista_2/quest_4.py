# 4. Escreva uma funcao que receba uma string, um caractere x e um numero inteiro i entre 0 e o comprimento da string menos 1, e retorne uma string igual as, exceto que o elemento da posicao i deve ser substituıdo pelo caractere x.

def substituir_caractere(string: str, caractere: str, indice: int) -> str:
    """
    Recebe uma string, um caractere x e um número inteiro i entre 0 e o comprimento da string menos 1.
    Retorna uma nova string igual à original, exceto que o elemento na posição i é substituído pelo caractere x.

    Parâmetros:
    - string (str): A string de entrada.
    - caractere (str): O caractere a ser inserido na posição i.
    - indice (int): O índice da posição a ser substituída.

    Retorna:
    - str: A string resultante após a substituição.

    Exemplo:
    >>> substituir_caractere('abcdef', 'x', 2)
    Retorna: 'abxde'
    """
    if 0 <= indice < len(string):
        return string[:indice] + caractere + string[indice+1:]
    return 'Índice fora dos limites.'


# Exemplo de teste
string_original = 'abcdef'
caractere_substituto = 'x'
indice_substituicao = 2
resultado = substituir_caractere(
    string_original, caractere_substituto, indice_substituicao)
print(resultado)  # Resultado: 'abxde'

# Exemplo de teste 2
string_original2 = 'Daniel Alexandre'
caractere_substituto2 = '4'
indice_substituicao2 = 9
resultado2 = substituir_caractere(
    string_original2, caractere_substituto2, indice_substituicao2)
print(resultado2)  # Resultado: 'Daniel Al4xandre'
