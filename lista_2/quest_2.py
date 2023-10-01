# 2. Escreva um funcao que receba o nome e a idade de uma pessoa e retorne a frase: ”Parabens fulano!  seu numero da sorte e x!”, onde fulano ́e o nome da pessoa, e x ́e o numero da sorte encontrado.

def frase_numero_da_sorte(nome: str, idade: int) -> str:
    """
    Recebe o nome e a idade de uma pessoa e retorna a frase: "Parabéns fulano! Seu número da sorte é x!",
    onde fulano é o nome da pessoa, e x é o número da sorte calculado.

    Parâmetros:
    - nome (str): O nome da pessoa.
    - idade (int): A idade da pessoa.

    Retorna:
    - str: A frase com o nome da pessoa e o número da sorte.

    Exemplo:
    >>> frase_numero_da_sorte('Daniel', 18)
    Retorna: 'Parabéns Daniel! Seu número da sorte é 24.0!'
    """
    try:
        if not isinstance(nome, str) or not isinstance(idade, int):
            raise TypeError(
                'Nome deve ser uma string e idade deve ser um número inteiro.')

        numero_da_sorte = ((idade * 4 + 8) * 60 / 240 + 22 - idade)

    except TypeError:
        return 'Por favor, insira valores válidos.'

    return f'Parabéns {nome}! Seu número da sorte é {numero_da_sorte:.1f}!'


# Exemplos de teste
# Resultado: 'Parabéns Daniel! Seu número da sorte é 24.0!'
print(frase_numero_da_sorte('Daniel', 18))
# Resultado: 'Por favor, insira valores válidos.'
print(frase_numero_da_sorte('Daniel', '18'))
# Resultado: 'Por favor, insira valores válidos.'
print(frase_numero_da_sorte(18, 18))
# Resultado: 'Parabéns Daniel! Seu número da sorte é 24.0!'
print(frase_numero_da_sorte('Daniel', 24))
# Resultado: 'Parabéns Daniel! Seu número da sorte é 24.0!'
print(frase_numero_da_sorte('Daniel', 26))
