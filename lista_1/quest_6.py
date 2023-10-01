def tem_direito_meia_entrada(idade, carteira_estudante):
    """
    Verifica se uma pessoa tem direito à meia-entrada com base na idade e na posse de carteira de estudante.

    Parâmetros:
    - idade (int): A idade da pessoa.
    - carteira_estudante (bool): True se a pessoa possui carteira de estudante, False caso contrário.

    Retorna:
    - bool: True se a pessoa tem direito à meia-entrada, False caso contrário.
    """
    if idade >= 65 or (idade <= 21 and not carteira_estudante):
        return True
    elif carteira_estudante:
        return True
    else:
        return False


# Exemplos de teste
idade1 = 18
carteira1 = False
resultado1 = tem_direito_meia_entrada(idade1, carteira1)
print(resultado1)  # Resultado: True (idade <= 21)

idade2 = 25
carteira2 = True
resultado2 = tem_direito_meia_entrada(idade2, carteira2)
print(resultado2)  # Resultado: True (carteira de estudante)

idade3 = 70
carteira3 = True
resultado3 = tem_direito_meia_entrada(idade3, carteira3)
print(resultado3)  # Resultado: True (idade >= 65 e carteira de estudante)
