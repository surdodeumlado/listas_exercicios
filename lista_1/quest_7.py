def classificacao_campeonato(C, Ce, Cs, Fv, Fe, Fs):
    """
    Determina qual time está melhor classificado no campeonato ou se eles estão empatados.

    Parâmetros:
    - C (int): Número de vitórias do Cormengo.
    - Ce (int): Número de empates do Cormengo.
    - Cs (int): Saldo de gols do Cormengo.
    - Fv (int): Número de vitórias do Flaminthians.
    - Fe (int): Número de empates do Flaminthians.
    - Fs (int): Saldo de gols do Flaminthians.

    Retorna:
    - str: O nome do time melhor classificado ("Cormengo" ou "Flaminthians") ou "Empate" se houver empate.
    """
    pontos_cormengo = 3 * C + Ce
    pontos_flaminthians = 3 * Fv + Fe

    if pontos_cormengo > pontos_flaminthians:
        return "Cormengo"
    elif pontos_flaminthians > pontos_cormengo:
        return "Flaminthians"
    else:  # Pontos iguais, verificar saldo de gols
        if Cs > Fs:
            return "Cormengo"
        elif Fs > Cs:
            return "Flaminthians"
        else:  # Saldo de gols igual, retorna "Empate"
            return "Empate"


# Exemplos de teste
print(classificacao_campeonato(10, 5, 18, 11, 2, 18))  # Resultado: 'Empate'
print(classificacao_campeonato(10, 5, 18, 11, 1, 18))  # Resultado: 'Cormengo'
# Resultado: 'Flaminthians'
print(classificacao_campeonato(9, 5, -1, 10, 2, 10))
