import os

restaurantes = ['Doja', 'Cerrano', 'Jordania']

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

def menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    menu_principal()

def cadastrar_restaurante():
    os.system('cls')
    print('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do novo restaurante: ')
    restaurantes.append(nome_restaurante)
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    menu_principal()

def listar_restaurantes():
    os.system('cls')
    print('Listando os restaurantes\n')
    for restaurante in restaurantes:
        print(f'. {restaurante}')
    menu_principal()   

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escoha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
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