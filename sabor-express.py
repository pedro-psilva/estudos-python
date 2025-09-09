import os

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


def escolher_opcao():
    opcao_escolhida = int(input('Escoha uma opção: '))

    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    elif opcao_escolhida ==4:
        finalizar_app()
    else:
        print('Opção inválida!')


def main():
    exibir_nome_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()