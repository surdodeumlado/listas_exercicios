# 10. Escreva uma funcao que receba duas datas no formato ”DD/MM/AAAA”, sendo a segunda maior que a primeira, e calcule o total de dias passados entre uma data e outra. A frase retornada deve ser ”O total de dias e x”, onde x ́e o total achado. Considere que todo mes tem 30 dias. E que o anotem 365 dias.Exemplo: Se as datas sao ”02/03/1982” e ”01/02/1983”, o total de dias e 334.

def calcular_total_de_dias(data1: str, data2: str) -> str:
    """
    Recebe duas datas no formato "DD/MM/AAAA" e calcula o total de dias passados entre elas.

    Parâmetros:
    - data1 (str): A primeira data no formato "DD/MM/AAAA".
    - data2 (str): A segunda data no formato "DD/MM/AAAA".

    Retorna:
    - str: A frase com o total de dias passados.

    Exemplo:
    >>> calcular_total_de_dias("02/03/1982", "01/02/1983")
    Retorna: 'O total de dias é 334.'
    """
    # Separando dia, mês e ano das datas
    dia1, mes1, ano1 = map(int, data1.split('/'))
    dia2, mes2, ano2 = map(int, data2.split('/'))

    # Calculando o total de dias passados
    total_dias = (ano2 - ano1) * 365 + (mes2 - mes1) * 30 + (dia2 - dia1)

    return f'O total de dias é {total_dias}.'


# Exemplo de teste
data1 = "02/03/1982"
data2 = "01/02/1983"
resultado = calcular_total_de_dias(data1, data2)
print(resultado)  # Resultado: 'O total de dias é 334.'

# Exemplo de teste
data1 = "16/02/2005"
data2 = "16/02/2006"
resultado = calcular_total_de_dias(data1, data2)
print(resultado)  # Resultado: 'O total de dias é 365.'
