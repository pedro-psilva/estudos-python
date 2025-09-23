import os

restaurantes = [{'nome':'Terraço Mineiro', 'categoria':'Mineira', 'ativo':False}
                ,{'nome':'Pizzaria do Zé', 'categoria':'Italiana', 'ativo':True}
                ,{'nome':'Sushi Yama', 'categoria':'Japonesa', 'ativo':True}
                ,{'nome':'Churrascaria Boi na Brasa', 'categoria':'Churrasco', 'ativo':False}]

def exibir_nome_programa():
    print("Sabor Express\n")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')
   
def finalizar_app():
    exibir_subtitulo('Encerrando o aplicativo\n')     

def menu_principal():
    input('\nDigite uma tecla para voltar ao menu ')
    main()

def opcao_invalida():
    print('Opção inválida!\n')
    menu_principal()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()    

def cadastrar_restaurante():
    exibir_subtitulo('Cadastro de novos restaurantes\n')
    nome_restaurante = input('Digite o nome do novo restaurante: ')
    categria_restaurante = input(f'Digite a categoria do restaurante {nome_restaurante}: ')
    ativo_restaurante = input('O restaurante está ativo? (s/n): ').lower()
    restaurantes.append({
    'nome': nome_restaurante,
    'categoria': categria_restaurante,
    'ativo': (ativo_restaurante == 's')
})
    print(f'O restaurante {nome_restaurante} foi cadastrado com sucesso!\n')
    menu_principal()

def listar_restaurantes():
    exibir_subtitulo('Listando os restaurantes\n')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria_restaurante = restaurante['categoria']
        ativo_restaurante = restaurante['ativo']
        print(f'- {nome_restaurante} | {categoria_restaurante} | {"Ativo" if ativo_restaurante else "Inativo"}')
    menu_principal()   

def alterar_status_restaurante():
    exibir_subtitulo('Alterar status do restaurante\n')
    
    for restaurante in restaurantes:
        print(f'- {restaurante["nome"]} | {"Ativo" if restaurante["ativo"] else "Inativo"}')
    
    nome_restaurante = input('\nDigite o nome do restaurante que deseja alterar o status: ').strip()
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante.lower() == restaurante['nome'].lower():
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            print(f'\nO restaurante {restaurante["nome"]} agora está {"Ativo" if restaurante["ativo"] else "Inativo"}.\n')
            break

    if not restaurante_encontrado:
        print(f'\nO restaurante "{nome_restaurante}" não foi encontrado.\n')

    menu_principal()



def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escoha uma opção: '))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status_restaurante()
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