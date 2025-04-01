def eh_primo(n):
    # Números menores ou iguais a 1 não são primos
    if n <= 1:
        return False
    # Verifica se n é divisível por algum número entre 2 e a raiz quadrada de n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Solicita ao usuário um número inteiro
try:
    N = int(input("Digite um número inteiro: "))
    if eh_primo(N):
        print(f"{N} é um número primo.")
    else:
        print(f"{N} não é um número primo.")
except ValueError:
    print("Por favor, digite um número inteiro válido.")
