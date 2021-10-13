novoUsuario = {}
listaUsuarios = []


def criarUsuario (): ## Função para o cadastro de usuário com nome e email
    novoUsuario ['nome'] = input('\nInsira o nome completo do usuário: ')
    novoUsuario['email'] = input('Insira o email do usuário: ')
    return novoUsuario
 #algo aqui está reescrevendo os ultimos cadastros


def main (): ## Função para adicionar os usuários a uma lista
    menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.' \
    '\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.'\
    '\nDigite 4 para buscar um participante pelo nome\nDigite 5 para remover um participante pelo email.'\
    '\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail'\
    '\nDigite o número da sua escolha: '))
    while menu == 1:
      listaUsuarios.append(criarUsuario())
      main ()
    if menu == 2:
        for Cadastro in listaUsuarios:
           print('Lista por ordem de cadastro:', listaUsuarios)
        main()
    elif menu == 3:
       for CadastroAlfabetico in listaUsuarios: 
            print('Lista por ordem alfabetica:', listaUsuarios.sort)
       main()
    elif menu == 4:
       print('Busca por nome:', listaUsuarios)
       main()
    elif menu == 5:
       print('excluindo por email:', listaUsuarios)
    elif menu != [1,2,3,4,5]:
      print("resposta não existente")
      main()

main()
