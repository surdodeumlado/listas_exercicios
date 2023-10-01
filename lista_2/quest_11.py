# 11. Escreva uma funcao que, dados dois retangulos, determine se eles se interceptam ou nao.

def verifica_interseccao_retangulos(retangulo1X1, retangulo1Y1, retangulo1X2, retangulo1Y2, retangulo2X1, retangulo2Y1, retangulo2X2, retangulo2Y2):
    """
    Verifica se dois retângulos se intersectam com base nas coordenadas de seus cantos.

    Parâmetros:
    - retangulo1X1 (int): Coordenada X do canto superior esquerdo do primeiro retângulo.
    - retangulo1Y1 (int): Coordenada Y do canto superior esquerdo do primeiro retângulo.
    - retangulo1X2 (int): Coordenada X do canto inferior direito do primeiro retângulo.
    - retangulo1Y2 (int): Coordenada Y do canto inferior direito do primeiro retângulo.
    - retangulo2X1 (int): Coordenada X do canto superior esquerdo do segundo retângulo.
    - retangulo2Y1 (int): Coordenada Y do canto superior esquerdo do segundo retângulo.
    - retangulo2X2 (int): Coordenada X do canto inferior direito do segundo retângulo.
    - retangulo2Y2 (int): Coordenada Y do canto inferior direito do segundo retângulo.

    Retorna:
    - bool: True se os retângulos se intersectam, False caso contrário.
    """
    # Verifica se há interseção horizontal entre os retângulos
    if retangulo1X2 < retangulo2X1 or retangulo2X2 < retangulo1X1:
        return False

    # Verifica se há interseção vertical entre os retângulos
    if retangulo1Y2 < retangulo2Y1 or retangulo2Y2 < retangulo1Y1:
        return False

    # Se nenhuma das condições acima for atendida, os retângulos se intersectam
    return True


# Exemplos de teste
print(verifica_interseccao_retangulos(0, 0, 1, 1, 0, 0, 1, 1))  # Saída: True
print(verifica_interseccao_retangulos(0, 0, 2, 2, 1, 1, 3, 3))  # Saída: True
print(verifica_interseccao_retangulos(0, 0, 1, 1, 2, 2, 3, 3))  # Saída: False
