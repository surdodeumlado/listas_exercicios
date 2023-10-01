def repetir_palavra(palavra):
    """
    Retorna uma sequência de caracteres composta por três repetições da palavra fornecida.

    Parâmetros:
    - palavra (str): A palavra a ser repetida.

    Retorna:
    - str: A sequência composta por três repetições da palavra.
    """
    return palavra * 3


# Exemplo de teste
entrada = "Python"
resultado = repetir_palavra(entrada)
print(resultado)  # Resultado: 'PythonPythonPython'
