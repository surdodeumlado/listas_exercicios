# 8. Escreva uma funcao que receba uma string e um numero inteiro x e rotacione a string x posicoes para a esquerda. Assuma que a string tem pelo menos x caracteres.

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
    if len(string) >= x:
        return string[x:] + string[:x]
    return f'A string deve ter pelo menos {x} caracteres.'


# Exemplo de teste
string_original = 'abcdefg'
x = 3
resultado = rotacionar_string_esquerda(string_original, x)
print(resultado)  # Resultado: 'defgabc'

# Exemplo de teste 2
string_original2 = 'Daniel Alexandre Pinho'
y = 7
resultado2 = rotacionar_string_esquerda(string_original2, y)
print(resultado2)  # Resultado: 'Alexandre PinhoDaniel '

# Exemplo de teste 3
string_original3 = 'Daniel'
z = 7
resultado3 = rotacionar_string_esquerda(string_original3, z)
print(resultado3)  # Resultado: 'A string deve ter pelo menos 7 caracteres.'
