def papel_suficiente(competidores, quantidade_papel, folhas_por_competidor):
    """
    Determina se a quantidade de folhas de papel especial compradas pela Diretora é suficiente.

    Parâmetros:
    - competidores (int): O número de competidores.
    - quantidade_papel (int): A quantidade de folhas de papel especial compradas pela Diretora.
    - folhas_por_competidor (int): A quantidade de folhas de papel especial que cada competidor deve receber.

    Retorna:
    - str: 'Suficiente' se a quantidade de folhas é suficiente, 'Insuficiente' caso contrário.
    """
    total_folhas_necessarias = competidores * folhas_por_competidor

    if quantidade_papel >= total_folhas_necessarias:
        return 'Suficiente'
    return 'Insuficiente'


# Exemplos de teste
print(papel_suficiente(10, 100, 10))  # Resultado: 'Suficiente'
print(papel_suficiente(10, 90, 10))   # Resultado: 'Insuficiente'
print(papel_suficiente(5, 40, 2))    # Resultado: 'Suficiente'
