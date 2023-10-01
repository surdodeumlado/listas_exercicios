def min_max(val1, val2):
    """
    Retorna o valor mínimo e máximo entre dois valores fornecidos.

    Parâmetros:
    - val1 (float ou int): O primeiro valor.
    - val2 (float ou int): O segundo valor.

    Retorna:
    - tuple: Uma tupla contendo o valor mínimo e o valor máximo.
    """
    return (min(val1, val2), max(val1, val2))

# Exemplo de teste
valor1 = 10
valor2 = 5
resultado = min_max(valor1, valor2)
print(resultado)  # Resultado: (5, 10) - Valor mínimo e máximo entre 5 e 10
