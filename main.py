from operacoesbd import *

conexaoComBD = abrirBancoDados("localhost","root","hugobezerra2005","sistemadeouvidoria")

print('Seja bem-vindo(a) ao Sistema de Ouvidoria. Segue abaixo suas opções : ')

opcao = 0

while opcao != 4 :

    print() #Espaço

    menuPrincipal = ('1) Reclamações', '2) Elogios', '3) Sugestões', '4) Sair')
    for item in menuPrincipal:
        print(item)
    print() #Espaço

    opcao = int(input('Digite aqui sua opção : '))


    if opcao == 1 :

        opcaoReclamacoes = 0

        while opcaoReclamacoes != 5 :

            print() #Espaço
            menuReclamacoes = ('1) Listar reclamações', '2) Adicionar reclamação', '3) Remover reclamação', '4) Pesquisar reclamação por código', '5) Voltar ao menu anterior ')
            for item in menuReclamacoes:
                print(item)
            print() #Espaço


            opcaoReclamacoes = int(input('Digite aqui sua opção : '))


            sqlReclamacoes = "SELECT * FROM reclamação;"
            listagemDasReclamacoes = listarBancoDados(conexaoComBD, sqlReclamacoes)


            if opcaoReclamacoes == 1 :

                print() #Espaço

                if len(listagemDasReclamacoes) == 0:
                    print('Nenhuma reclamação cadastrada no sistema')
                else:
                    print('As reclamações cadastradas no sistema são :')
                    for item in listagemDasReclamacoes:
                        print(item[0],')',item[1])


            elif opcaoReclamacoes == 2 :

                print() #Espaço

                novaReclamacao = input('Digite aqui sua reclamação : ')
                sqlNovaReclamacao = "INSERT INTO reclamação (Reclamação) values (%s);"
                dados = (novaReclamacao,)
                codigoNovaReclamacao = insertNoBancoDados(conexaoComBD, sqlNovaReclamacao, dados)

                print() #Espaço
                print('Reclamação cadastrada com suscesso. O código da reclamação é ',codigoNovaReclamacao)


            elif opcaoReclamacoes == 3 :

                if len(listagemDasReclamacoes) == 0:
                    print() #Espaço
                    print('Nenhuma reclamação cadastrada no sistema')
                else:
                    print() #Espaço
                    print('As reclamações cadastradas no sistema são :')
                    for item in listagemDasReclamacoes:
                        print(item[0],')',item[1])

                    print() #Espaço
                    codigoRemocao = int(input('Digite o código da reclamação ao qual você deseja remover : '))
                    print() #Espaço
                    sqlRemocao = "DELETE FROM reclamação WHERE Código = (%s);"
                    dados = (codigoRemocao,)
                    validarExclusao = excluirBancoDados(conexaoComBD,sqlRemocao,dados)

                    if validarExclusao == 1 :
                        print('Reclamação removida com suscesso.')
                    else :
                        print('Código inválido')


            elif opcaoReclamacoes == 4 :

                if len(listagemDasReclamacoes) == 0:
                    print() #Espaço
                    print('Nenhuma reclamação cadastrada no sistema')

                else :
                    print() #Espaço
                    codigoPesquisa = int(input('Digite o código da reclamação a ser pesquisada : '))
                    sqlPesquisa = "SELECT * FROM reclamação WHERE Código = " + str(codigoPesquisa)
                    codigoPesquisado = listarBancoDados(conexaoComBD,sqlPesquisa)

                    if len(codigoPesquisado) == 0 :
                        print() #Espaço
                        print('Não existem reclamações com esse código')
                    else :
                        print() #Espaço
                        print('A reclamação pesquisada foi :')
                        print() #Espaço
                        for item in codigoPesquisado :
                            print(item[0],')',item[1])


            elif opcaoReclamacoes != 5 :
                print() #Espaço
                print('Opção inválida, por favor tente novamente')


    elif opcao == 2 :

        opcaoElogios = 0

        while opcaoElogios != 5 :

            print() #Espaço

            menuElogio = ('1) Listar elogios','2) Adicionar elogio','3) Remover elogio','4) Pesquisar elogio pelo código','5) Voltar ao menu anterior')
            for item in menuElogio :
                print(item)

            print() #Espaço
            opcaoElogios = int(input('Digite aqui sua opção : '))


            sqlElogios = "SELECT * FROM elogios;"
            listagemDosElogios = listarBancoDados(conexaoComBD,sqlElogios)


            if opcaoElogios == 1 :

                print() #Espaço

                if len(listagemDosElogios) == 0 :
                    print('Nenhum elogio cadastrado no sistema')
                else :
                    print('Os elogios cadastrados no sistema são : ')
                    for item in listagemDosElogios :
                        print(item[0],')',item[1])

            elif opcaoElogios == 2 :

                print() #Espaço

                adicionarElogio = input('Digite aqui seu elogio : ')
                sqlNovoElogio = "INSERT INTO elogios (Elogio) values (%s);"
                dados = (adicionarElogio,)

                codigoNovoElogio = insertNoBancoDados(conexaoComBD,sqlNovoElogio,dados)

                print() #Espaço
                print('Elogio adicionado com suscesso. O código do elogio é ',codigoNovoElogio)


            elif opcaoElogios == 3 :

                print() #Espaço

                if len(listagemDosElogios) == 0:
                    print('Nenhum elogio cadastrado no sistema')
                else:
                    print('Os elogios cadastrados no sistema são : ')
                    for item in listagemDosElogios:
                        print(item[0], ')', item[1])

                    print() #Espaço
                    codigoRemocaoElogio = int(input('Digite o código do elogio ao qual você deseja remover : '))
                    sqlRemocaoElogio = "DELETE FROM elogios WHERE Código = (%s);"
                    dados = (codigoRemocaoElogio,)
                    validarExclusaoElogio = excluirBancoDados(conexaoComBD,sqlRemocaoElogio,dados)

                    print() #Espaço
                    if validarExclusaoElogio == 1 :
                        print('Elogio removido com suscesso.')
                    else :
                        print('Código inválido')


            elif opcaoElogios == 4 :

                print()  # Espaço

                if len(listagemDosElogios) == 0:
                    print('Nenhum elogio cadastrado no sistema')
                else :
                    codigoPesquisaElogio = int(input('Digite o código do elogio ao qual você deseja pesquisar : '))
                    sqlPesquisaSugestao = "SELECT * FROM elogios WHERE Código = " + str(codigoPesquisaElogio)
                    codigoPesquisadoElogio = listarBancoDados(conexaoComBD, sqlPesquisaSugestao)

                    print() #Espaço

                    if len(codigoPesquisadoElogio) == 0 :
                        print('Não existem elogios com esse código')
                    else :
                        print('O elogio pesquisado foi : ')
                        for item in codigoPesquisadoElogio :
                            print(item[0],')',item[1])

            elif opcaoElogios != 5 :

                print() #Espaço
                print('Opção inválida, por favor tente novamente')


    elif opcao == 3 :

        opcaoSugestoes = 0

        while opcaoSugestoes != 5 :

            print() #Espaço

            menuSugestoes = ('1) Listar Sugestões','2) Adicionar sugestão','3) Remover sugestão','4) Pesquisar sugestão por código','5) Voltar ao menu anterior')
            for item in menuSugestoes :
                print(item)

            print() #Espaço

            opcaoSugestoes = int(input('Digite aqui sua opção : '))


            sqlSugestoes = "SELECT * FROM sugestões;"
            listagemDasSugestoes = listarBancoDados(conexaoComBD,sqlSugestoes)


            if opcaoSugestoes == 1 :

                print() #Espaço

                if len(listagemDasSugestoes) == 0 :
                    print('Nenhuma sugestão cadastrada no sistema.')

                else :
                    print('As sugestões cadastradas no sistema são :')
                    for item in listagemDasSugestoes :
                        print(item[0],')',item[1])


            elif opcaoSugestoes == 2 :

                print() #Espaço

                adicionarSugestao = input('Digite aqui sua sugestão : ')

                sqlNovaSugestao = "INSERT INTO sugestões (Sugestão) values (%s);"
                dados = (adicionarSugestao,)
                codigoNovaSugestao = insertNoBancoDados(conexaoComBD,sqlNovaSugestao,dados)

                print() #Espaço
                print('Sugestão cadastrada com suscesso. O código da sugestão é ',codigoNovaSugestao)


            elif opcaoSugestoes == 3 :

                print() #Espaço

                if len(listagemDasSugestoes) == 0:
                    print('Nenhuma sugestão cadastrada no sistema.')

                else:
                    print('As sugestões cadastradas no sistema são :')
                    for item in listagemDasSugestoes:
                        print(item[0], ')', item[1])

                    print() #Espaço
                    codigoRemocaoSugestao = int(input('Digite aqui o código da sugestão ao qual você deseja remover : '))
                    sqlRemocaoSugestao = "DELETE FROM sugestões WHERE Código = (%s)"
                    dados = (codigoRemocaoSugestao,)

                    validarExclusaoReclamacao = excluirBancoDados(conexaoComBD,sqlRemocaoSugestao,dados)

                    print() #Espaço
                    if validarExclusaoReclamacao == 1 :
                        print('Reclamação removida com suscesso.')
                    else :
                        print('Código inválido')


            elif opcaoSugestoes == 4 :

                print() #Espaço

                if len(listagemDasSugestoes) == 0:
                    print('Nenhuma sugestão cadastrada no sistema')

                else:
                    codigoPesquisaSugestao = int(input('Digite o código da sugestão ao qual você deseja pesquisar : '))
                    sqlPesquisaSugestao = "SELECT * FROM sugestões WHERE Código = " + str(codigoPesquisaSugestao)
                    codigoPesquisadoSugestao = listarBancoDados(conexaoComBD, sqlPesquisaSugestao)

                    print()  # Espaço

                    if len(codigoPesquisadoSugestao) == 0:
                        print('Não existem sugestões com esse código')
                    else:
                        print('A sugestão pesquisada foi : ')
                        for item in codigoPesquisadoSugestao:
                            print(item[0], ')', item[1])

    elif opcao != 4 :
        print() #Espaço
        print('Opção inválida, por favor tente novamente')

print() #Espaço
print('Obrigado por usar o Sistema de Ouvidoria.')

encerrarBancoDados(conexaoComBD)