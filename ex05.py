# armazena um número pequeno
maior_numero = -9999999

# entra com o primeiro número
number = int(input("Entre com um número ou digite -1 para parar: "))

# Se o número não for igual a -1 continua
while number != -1:
    # O número é maior que o maior_numero
    if number > maior_numero:
    # Sim, atualiza maior_numero
        maior_numero = number
    # Entre com o proximo número.
    number = int(input("Entre com um número ou digite -1 para parar> "))
    
    #print the largest number.
    print("O maior número é: ", maior_numero)