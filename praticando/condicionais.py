#1 - Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.
"""numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else:
    print(f'O número {numero} é ímpar!')"""

#2 - Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições: Criança: 0 a 12 anos;Adolescente: 13 a 18 anos;Adulto: acima de 18 anos.
"""idade = int(input('Digite a sua idade: '))

if idade >= 0 and idade <= 12:
    print('Categoria: criança')
elif idade > 12 and idade <= 18:
    print('Categoria: adolescente')
elif idade >= 18:
    print('Categoria: adulto')
else:
    print('Valor inválido')"""

#3 - Solicite um nome de usuário e uma senha e use uma estrutura if else para verificar se o nome de usuário e a senha fornecidos correspondem aos valores esperados determinados por você.

"""login = 'admin'
senha = '12345'

usuario = input('Digite seu login: ')
senha_usuario = input('Digite sua senha: ')

if login == usuario and senha == senha_usuario:
    print('Acesso autorizado!')
else:
    print('Acesso negado!')"""

#4 - Solicite ao usuário as coordenadas (x, y) de um ponto qualquer e utilize uma estrutura if elif else para determinar em qual quadrante do plano cartesiano o ponto se encontra de acordo com as seguintes condições:

#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

"""x = float(input('Digite o valor de x :'))
y = float(input('Digite o valor de y :'))

if x > 0 and y > 0:
    print('Primeiro quadrante')
elif x < 0 and y > 0:
    print('Segundo quadrante')
elif x < 0 and y < 0:
    print('Terceiro quadrante')
elif x > 0 and y < 0:
    print('Quarto quadrante')
else:
    print('O ponto está localizado no eixo ou origem.')"""