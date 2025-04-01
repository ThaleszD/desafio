def soma_digitos(n):

    if n < 0:
        raise ValueError("O número deve ser um inteiro positivo.")
    
   
    if n == 0:
        return 0
    else:
    
        return (n % 10) + soma_digitos(n // 10)
        
try:
    N = int(input("Digite um número inteiro positivo: "))
    resultado = soma_digitos(N)
    print(f"A soma dos dígitos de {N} é {resultado}.")
except ValueError as e:
    print(e)
