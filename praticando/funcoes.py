
"""def calc_idade(ano_nasc, ano_atual):
    return ano_atual - ano_nasc"""

"""nascimento = int(input("Digite o ano de nascimento: "))
atual = int(input("Digite o ano atual: "))
idade = calc_idade(nascimento, atual)
print("A sua idade é: ",idade)"""

"""def cont_caracteres(palavra):
    return len(palavra)"""

"""texto = input("Digite uma palavra: ")
print("A palavra tem",cont_caracteres(texto),"caracteres")"""


"""def saudacao(hora):
    if hora < 12:
      return "Bom dia"
    elif hora < 18:
        return "Boa tarde"
    else:
        return "Boa noite"
"""
        
""" hora_atual = int(input("Digite a hora atual (0-23): "))
 print(saudacao(hora_atual))"""

"""def convert_tel(lista):
    return [int(telefone) for telefone in lista]
def verif_tipos(lista):
    for num in lista:
        if not isinstance(num, int):
            return "Erro na conversão."
        return "Todos os números foram convertidos"
telefones = ["312443231", "12343231212", "12324322344", "2343551232"]    
tel_convertidos = convert_tel(telefones)
print(verif_tipos(tel_convertidos))"""

"""valores = input('Digite os valores das vendas: ').split()
total = sum(map(float, valores))
print(f"O total de vendas foi: {total}")"""

"""numeros = input('Digite os números separados por espaço: ').split()
pares = filter(lambda x: int(x) % 2 == 0, numeros)
print('Números pares: ', ' '.join(pares))"""

"""produtos = input('Digite os produtos separados por vírgula: ').split(",")
precos = input('Digite os preços separados por vírgula: ').split(",")
for produto, preco in zip(produtos, precos):
    print(f"{produto.strip()}: {preco.strip()}")"""

"""soma = lambda x, y: x + y
subtrai = lambda x, y: x - y
multiplica = lambda x, y: x * y
divide = lambda x, y: x / y if y != 0 else "Erro: divisão por zero."

x = float(input('Digite o primeiro número: '))
y = float(input('Digite o segundo número: '))

operador = input('Escolha um operador: ( +  -  *  / )')
if operador == '+':
    print(f'O resultado da soma é: {soma(x, y)}')
elif operador == '-':
    print(f'O resultado da subtração é: {subtrai(x, y)}')
elif operador == '*':
    print(f'O resultado da multiplicação é: {multiplica(x, y)}')
elif operador == '/':
    print(f'O resultado da divisão é: {divide(x, y)}')
else:
    print('Operador inválido!')"""

"""def criar_desconto(porcentagem):
    def calcular_preco(valor):
        return valor - (valor * (porcentagem/100))
    return calcular_preco
desconto = float(input('Qual a porcentagem do desconto? '))

calcular_preco_final = criar_desconto(desconto)
valor = float(input('Qual o valor da compra? '))
print(f'Preco final com desconto: {calcular_preco_final(valor)}')"""

"""def soma_recursiva(n):
    if n == 1:
        return 1
    return n + soma_recursiva(n-1)
numero = int(input('Digite um número: '))
print(f'A soma de 1 a {numero} é: {soma_recursiva(numero)}')"""