listaUsuarios = []#lista
novoUsuario = {}#dicionário


def PesquisaNome (listaUsuarios,Nome):
    for Cadastro in listaUsuarios:
        if Cadastro == Nome:
            print("Cadastro procurado:\n {}".format(Nome))
            return
    print('Cadastro procurado:\n "{}" não existe'.format(Nome))


def ordemAlfabetica (y):
    return y['nome']

#-----------------------------------------------------------

menu = int(input('\nDigite 1 para cadastrar um novo usuário: '))
while menu != 1:
    menu = int(input('\nOpção inválida.\nDigite 1 para cadastrar um novo usuário: '))
while menu >= 1 and menu <= 6:
    if menu == 1: # para cadastrar um novo usuário
        novoUsuario.clear()
        novoUsuario ['nome'] = input('\nInsira o nome completo do usuário: ')#add nome
        novoUsuario['email'] = input('Insira o email do usuário: ') #add email
        listaUsuarios.append(novoUsuario.copy())
        ordemCad = listaUsuarios.copy()
        menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))

        #--------------------------------------------------------
    elif menu == 2: # para exibir todos os usuários cadastrados em ordem de cadastro
        print('\nUsuários por ordem de cadastro:\n')
        for umUsuario in ordemCad:
            print(umUsuario)
        menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))

        #--------------------------------------------------------
    elif menu == 3: # para exibir todos os usuários cadastrados em ordem alfabética
        ordemAlf = listaUsuarios.copy()
        ordemAlf.sort(key=ordemAlfabetica)
        print('\nUsuários por ordem alfabética:\n')
        for umUsuario in ordemAlf:
            print(umUsuario)
       # print(listaUsuarios) 
        menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))

        #---------------------------------------------------------
    elif menu == 4: #para procurar usuario buscando por nome
       Nome = input("inserir nome desejado: ")
       
       Resultados = [p for p in listaUsuarios if p['nome'] == Nome]
       print(Resultados)

       menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))

      #------------------------------------------------------
    elif menu == 5: #remover usuário cadastrado usando email
       Excluindo = input('\ninsira o email para excluir o usuario: ')
       contagem = 0
       Confirmacao = input('\ntem certeza?\n '\
       'Se sim digite "S"\n'\
       'Se não digite qualquer outra coisa: ')
       if Confirmacao == 'S' or 's':
         listaUsuarios = [p for p in listaUsuarios if p['email'] != Excluindo]
         ordemCad = listaUsuarios.copy()
         ordemAlf = listaUsuarios.copy()

          

       print(listaUsuarios)
       menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))

      #-----------------------------------------------------
    elif menu == 6: #alterar Usuario
      Excluindo = input('\ninsira o email para alterar o usuario: ')
      Confirmacao = input('\ntem certeza?\n '\
      'Se sim digite "S"\n'\
      'Se não digite qualquer outra coisa: ')
      listaUsuarios = [p for p in listaUsuarios if p['email'] != Excluindo]
      #---------------------
      novoUsuario.clear()
      novoUsuario ['nome'] = input('\nInsira o nome alterado completo do usuário: ')#add nome
      novoUsuario['email'] = input('Insira o email alterado do usuário: ') #add email
      listaUsuarios.append(novoUsuario.copy())
      ordemCad = listaUsuarios.copy()
      menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))
    elif menu == 7:
        break
    while menu <1 or menu >7:
        menu = int(input('\nMenu:\nDigite 1 para cadastrar um novo usuário.\nDigite 2 para exibir todos os usuários cadastrados em ordem de cadastro.\nDigite 3 para exibir todos os usuários cadastrados em ordem alfabética.\nDigite 4 para buscar um participante pelo nome.\nDigite 5 para remover um participante pelo email.\nDigite 6 para alterar o nome de um usuário cadastrado no sistema, buscando-o por seu e-mail.\nDigite 7 para encerrar.\nDigite o número da sua escolha: '))