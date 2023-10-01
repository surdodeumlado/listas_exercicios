import math

def calcular_raizes_quadraticas(a, b, c):
    """
    Calcula e retorna as raízes reais de uma equação de segundo grau (ax² + bx + c = 0).

    Parâmetros:
    - a (float ou int): Coeficiente a.
    - b (float ou int): Coeficiente b.
    - c (float ou int): Coeficiente c.

    Retorna:
    - str: Uma string que descreve as raízes da equação.

    Exemplo:
    >>> calcular_raizes_quadraticas(1, -3, 2)
    Retorna: 'Duas raízes reais: 2.0 e 1.0'
    
    >>> calcular_raizes_quadraticas(1, 2, 1)
    Retorna: 'Uma raiz real: -1.0'
    
    >>> calcular_raizes_quadraticas(1, -4, 5)
    Retorna: 'Nenhuma raiz real'
    """
    discriminante = b**2 - 4*a*c

    if discriminante > 0:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return f'Duas raízes reais: {raiz1} e {raiz2}'
    elif discriminante == 0:
        raiz = -b / (2*a)
        return f'Uma raiz real: {raiz}'
    else:
        return 'Nenhuma raiz real'

# Exemplos de teste
print(calcular_raizes_quadraticas(1, -3, 2))  # Resultado: 'Duas raízes reais: 2.0 e 1.0'
print(calcular_raizes_quadraticas(1, 2, 1))   # Resultado: 'Uma raiz real: -1.0'
print(calcular_raizes_quadraticas(1, -4, 5))  # Resultado: 'Nenhuma raiz real'
