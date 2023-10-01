# 3. Escreva uma funcao que receba duas strings de no mınimo 15 caracteres e retorne a concatenacao da primeira, sem os cinco primeiros caracteres, com a segunda, sem os ́ultimos dez caracteres.

def concatenacao(a, b):
    """
    Recebe dois valores a e b, converte-os para strings, remove espaços em branco, verifica o comprimento das strings
    sem espaços e, se ambos forem maiores ou iguais a 15 caracteres, retorna a concatenação das duas strings
    após remover os primeiros 5 caracteres de 'a' e os últimos 10 caracteres de 'b'.

    Parâmetros:
    - a (qualquer): O primeiro valor.
    - b (qualquer): O segundo valor.

    Retorna:
    - str: A concatenação das strings após as remoções.

    Exemplo:
    >>> concatenacao('123456789012345', '123456789012345')
    Retorna: '6789012345'

    >>> concatenacao(123456789012345, 123456789012345)
    Retorna: '6789012345'

    >>> concatenacao(1234567890, 'Erro')
    Retorna: 'Strings inválidas. Digite strings maiores que 15 caracteres'
    """
    a_sem_espaco = ''.join(str(a).strip(' '))
    b_sem_espaco = ''.join(str(b).strip(' '))

    if len(a_sem_espaco) < 15 or len(b_sem_espaco) < 15:
        return 'Strings inválidas. Digite strings maiores que 15 caracteres'

    a_str = str(a)
    b_str = str(b)

    return a_str[5:] + b_str[:(len(b_str) - 10)]


# Exemplos de teste
resultado1 = concatenacao('123456789012345', '123456789012345')
print(resultado1)  # Resultado: '6789012345'

resultado2 = concatenacao(123456789012345, 123456789012345)
print(resultado2)  # Resultado: '6789012345'

resultado3 = concatenacao(1234567890, 'Erro')
# Resultado: 'Strings inválidas. Digite strings maiores que 15 caracteres'
print(resultado3)
