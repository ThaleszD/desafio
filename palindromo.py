def eh_palindromo(palavra):
    # Remove espaços e converte para minúsculas
    palavra = palavra.replace(" ", "").lower()
    # Verifica se a palavra é igual à sua reversa
    return palavra == palavra[::-1]

# Solicita ao usuário que insira uma palavra
entrada = input("Digite uma palavra: ")

# Verifica a palavra 
if eh_palindromo(entrada):
    print(f"A palavra '{entrada}' é um palíndromo.")
else:
    print(f"A palavra '{entrada}' não é um palíndromo.")
