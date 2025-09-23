"""1 - Crie uma lista para cada informação a seguir:

Lista de números de 1 a 10;
Lista com quatro nomes;
Lista com o ano que você nasceu e o ano atual."""

"""numeros = list(range(1, 11))
nomes = ('Ana', 'Bruno', 'Carlos', 'Diana')
anos = (2002, 2025)

print(f"Números: {numeros}, nomes: {nomes}, anos: {anos}")"""

"""2 - Crie uma lista e utilize um loop for para percorrer todos os elementos da lista."""

"""sportster = ('Iron 883', 'Forty-Eight', 'XL883R', 'XL883 LOW', '883CB')
for moto in sportster:
    print(moto)"""

"""3 - Utilize um loop for para calcular a soma dos números ímpares de 1 a 10."""

"""soma = 0
for numero in range(1, 11):
    if numero % 2 != 0:
        soma += numero  

print(f'A soma dos números ímpares de 1 a 10 é {soma}')"""

"""4 - Utilize um loop for para imprimir os números de 1 a 10 em ordem decrescente."""

"""for numero in range(10, 0, -1):
    print(numero)"""

"""5 - Solicite ao usuário um número e, em seguida, utilize um loop for para imprimir a tabuada desse número, indo de 1 a 10."""

"""numero = int(input('Digite um número para ver a tabuada: '))
for i in range(1, 11):
    resultado = numero * i
    print(f'{numero} x {i} = {resultado}')"""

"""6 - Crie uma lista de números e utilize um loop for para calcular a soma de todos os elementos. Utilize um bloco try-except para lidar com possíveis exceções."""

"""numeros = [10, 20, '40', 55, 50]
soma = 0
try:
    for numero in numeros:
        soma += numero
    print(f'A soma dos números da lista é {soma}')
except TypeError:
    print('Erro: A lista contém um valor não numérico que não pode ser somado.')"""

"""7 - Construa um código que calcule a média dos valores em uma lista. Utilize um bloco try-except para lidar com a divisão por zero, caso a lista esteja vazia."""

"""valores = [10, 20, 30, 40, 50]
try:
    media = sum(valores) / len(valores)
    print(f'A média dos valores da lista é {media}')
except ZeroDivisionError:
    print('Erro: A lista está vazia, não é possível calcular a média.')"""