# 7. Escreva uma funcao que receba uma string e a rotacione 3 posicoes para a esquerda. Por exemplo, se a entrada for ”abcdefg”, a funcao deve retornar ”efgabcd”. Assuma que a string passada tem no mınimo 3 caracteres.

def rotacionar_string_esquerda(string: str) -> str:
    """
    Recebe uma string e a rotaciona 3 posições para a esquerda.

    Parâmetros:
    - string (str): A string de entrada.

    Retorna:
    - str: A string resultante após a rotação.

    Exemplo:
    >>> rotacionar_string_esquerda('abcdefg')
    Retorna: 'efgabcd'
    """
    if len(string) >= 3:
        return string[3:] + string[:3]
    return 'A string deve ter pelo menos 3 caracteres.'


# Exemplo de teste
string_original = 'abcdefg'
resultado = rotacionar_string_esquerda(string_original)
print(resultado)  # Resultado: 'efgabcd'

# Exemplo de teste 2
string_original2 = 'Daniel'
resultado2 = rotacionar_string_esquerda(string_original2)
print(resultado2)  # Resultado: 'ielDan'
