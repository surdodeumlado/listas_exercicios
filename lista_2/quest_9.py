# 9. Escreva uma funcao similar a anterior, so que agora considere que a string passada pode ter qualquer tamanho, inclusive menor que x.

def rotacionar_string_esquerda(string: str, x: int) -> str:
    """
    Recebe uma string e um número inteiro x e rotaciona a string x posições para a esquerda.

    Parâmetros:
    - string (str): A string de entrada.
    - x (int): O número de posições a serem rotacionadas para a esquerda.

    Retorna:
    - str: A string resultante após a rotação.

    Exemplo:
    >>> rotacionar_string_esquerda('abcdefg', 3)
    Retorna: 'defgabc'
    """
    x = x % len(
        string)  # Garante que x seja menor ou igual ao comprimento da string
    return string[x:] + string[:x]


# Exemplo de teste
string_original = 'abcdefg'
x = 3
resultado = rotacionar_string_esquerda(string_original, x)
print(resultado)  # Resultado: 'defgabc'
