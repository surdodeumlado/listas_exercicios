# 6. Escreva uma funcao que receba uma string e insira o caractere ”#” no inıcio, no meio e no final dela.Por exemplo, se a entrada for ”abcd”, a saıda deve ser ”#ab#cd#”. Outro exemplo: se receber ”abcde”,a fun ̧cao deve retornar ”#ab#cde#”.

def inserir_hashtags(string):
    meio = len(string) // 2  # Calcula o índice do meio da string
    string_com_hashtags = "#" + string[:meio] + "#" + string[meio:] + "#"
    return string_com_hashtags


# Exemplos de uso da função
string1 = "abcd"
resultado1 = inserir_hashtags(string1)
print(resultado1)  # Saída: "#ab#cd#"

string2 = "abcde"
resultado2 = inserir_hashtags(string2)
print(resultado2)  # Saída: "#ab#cde#"
