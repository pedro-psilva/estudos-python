import os

restaurantes = []

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
   
def finalizar_app():
    os.system('cls')
    print('Encerrando o aplicativo\n')     

def opcao_invalida():
    print('Opção inválida!\n')
    input('Digite qualquer tecla para voltar ao menu principal\n')
    main()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do novo restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    input('Digite qualquer tecla para voltar ao menu principal\n')
    main()

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escoha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            print('Listar restaurantes')
        elif opcao_escolhida == 3:
            print('Ativar restaurante')
        elif opcao_escolhida ==4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()