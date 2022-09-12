"""
Entrada de dados
"""

nome = input("Qual é o seu nome ? ")
print(  f"O nome do usuário é {nome}."
        f" O tipo de variavel é {type(nome)}")

# Se colocarmos um numero no input ele vai continuar falando que é uma string.
# Para especificar devemos usar numero = int(input("Número"))


numero1 = int(input("Digite um número: "))
numero2 = input("Digite outro número: ")
numero2 = int(numero2)

print(numero1 ** numero2)