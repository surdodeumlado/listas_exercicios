def valor_absoluto(numero):
    """
    Calcula o valor absoluto de um número.

    Parâmetros:
    - numero (float ou int): O número para o qual deseja calcular o valor absoluto.

    Retorna:
    - float ou int: O valor absoluto do número fornecido.
    """
    return abs(numero)


# Exemplos de teste
numero1 = -5
resultado1 = valor_absoluto(numero1)
print(resultado1)  # Resultado: 5 (valor absoluto de -5)

numero2 = 10
resultado2 = valor_absoluto(numero2)
print(resultado2)  # Resultado: 10 (valor absoluto de 10)
