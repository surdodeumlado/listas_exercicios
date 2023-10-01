# 5. Escreva uma funcao que receba uma string e retorne essa string no meio dela mesma. Por exemplo, ao receber a string ”abcd”, a funcao deve retornar ”ababcdcd”. Outro exemplo: se receber ”abcde”, a funçao deve retornar ”ababcdecde”

def string_no_meio(s: str) -> str:
    """
    Recebe uma string s e retorna essa string no meio dela mesma, ou seja, a concatenação
    entre a primeira metade, a string original e a segunda metade.

    Parâmetros:
    - s (str): A string de entrada.

    Retorna:
    - str: A string resultante.

    Exemplos:
    >>> string_no_meio('abcd')
    Retorna: 'ababcdcd'

    >>> string_no_meio('abcde')
    Retorna: 'ababcdecde'

    >>> string_no_meio('Daniel')
    Retorna: 'DanDanieliel'
    """
    meio = len(s) // 2
    return s[:meio] + s + s[meio:]

# Exemplos de teste
string1 = 'abcd'
resultado1 = string_no_meio(string1)
print(resultado1)  # Resultado: 'ababcdcd'

string2 = 'abcde'
resultado2 = string_no_meio(string2)
print(resultado2)  # Resultado: 'ababcdecde'

string3 = 'Daniel'
resultado3 = string_no_meio(string3)
print(resultado3)  # Resultado: 'DanDanieliel'
