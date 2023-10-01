# 1. Escreva uma função que receba duas strings a e b, e retorne a concatenação delas no formato abba.

def concatenacao_abba(a: str, b: str) -> str:
    """
    Recebe duas strings a e b e retorna a concatenação delas no formato abba.

    Parâmetros:
    - a (str): A primeira string.
    - b (str): A segunda string.

    Retorna:
    - str: A concatenação das strings no formato abba.

    Exemplo:
    >>> concatenacao_abba("Hello", "World")
    Retorna: 'HelloWorldWorldHello'
    """
    return str(a) + str(b) + str(b) + str(a)


# Solicita ao usuário as duas strings
string_a = input('String 1: ')
string_b = input('String 2: ')

# Chama a função e imprime o resultado
resultado = concatenacao_abba(string_a, string_b)
print(resultado)
