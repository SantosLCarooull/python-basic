""""
Objetivo do desafio:Desenvolver um aplicativo que gerencie uma lista de compras que permita adicionar, 
remover e listar os produtos adicionados nela. 

Para isso, o seu aplicativo precisa ter as seguintes funcionalidades: 

Menu de Opções: 
O sistema deve fornecer um menu de opções para o usuário interagir. As opções devem ser as seguintes: 
 
Adicionar produto
Remover produto
Pesquisar produtos
Sair do programa  

Adicionar Produto: O usuário deve poder adicionar um novo produto à lista de compras. O sistema deve solicitar 
informações sobre o nome, unidade de medida, quantidade e descrição do produto. As opções de unidade devem ser:

Quilograma
Grama
Litro
Mililitro
Unidade
Metro
Centímetro 
Essas opções devem aparecer quando o sistema perguntar a unidade de medida.  

Controle de ID Automático: O sistema deve atribuir automaticamente um ID único para cada produto adicionado à lista.

Remover Produto: O usuário deve poder remover um produto da lista com base ID do produto. O sistema deve solicitar o 
ID do produto que o usuário deseja remover.

Pesquisar Produtos por Nome: O usuário deve poder pesquisar produtos na lista com base no nome ou parte do nome. 
O sistema deve exibir os resultados correspondentes e fornecer a contagem total de produtos encontrados.

Listar Todos os Produtos: O sistema deve ser capaz de exibir todos os produtos presentes na lista de compras, se houver.
Contudo, o menu não deve mostrar uma opção de “Listar produtos”. A exibição deverá ocorrer toda vez que o menu principal
for executado, acima dele.

Cabeçalho do Aplicativo: Deve ser exibido um cabeçalho ao iniciar o aplicativo para fornecer uma saudação e indicar que
é uma Lista de Compras Simples.

Feedback de Ação: Após a execução de uma ação (como adicionar ou remover um produto), o sistema deve fornecer feedback
indicando o resultado da ação.

Tratamento de Entradas Inválidas: O sistema deve ser capaz de lidar com entradas inválidas do usuário e fornecer 
mensagens de erro apropriadas para orientar o usuário.

Encerramento do Programa: O usuário deve poder encerrar o programa de forma adequada, escolhendo a opção de saída no 
menu.
"""""

def lista_compras():
    from rapidfuzz import process, fuzz

    lista_usuario = []
    id_produto = 1
    while True:
        print('Menu inicial: crie e edite uma lista de compras simples com o menu abaixo:    ')
        print('1. Adicionar produto:    ')
        print('2. Remover produto:    ')
        print('3. Pesquisar produtos:    ')
        print('4. Sair do programa:    ')
        print("\nSua lista atual:    ")
        for item in lista_usuario:
            print(item)
        menu = input('Digite a seguir a opção desejada:  ')

        if menu == '4':
            print("Obrigado por utilizar a Lista de Compras Simples!  ")
            break

        if menu not in ['1', '2', '3', '4']:
            print('Opção iválida! Por favor tente novamente.  ')
            continue

        lista_final = False

        if menu == '1':
            while not lista_final:
                nome_produto= input('Insira o nome do produto:  ')
                quantidade_produto = input('Forneça a quantidade deste produto:  ')

                print('kg. Quilograma  ')
                print('g. Grama  ')
                print('l. Litro  ')
                print('ml. Mililitro  ')
                print('uni. Unidade  ')
                print('m. Metro  ')
                print('cm. Centímetro   ')
                unidade_produto = input('Escolha a unidade de medida do produto:  ')

                # if unidade_produto.lower() == ['kg','g','l','ml','uni','m','cm']:
                #     continue
                #
                if unidade_produto not in ['kg','g','l','ml','uni','m','cm']:
                    print('Opção iválida! Por favor tente novamente.  ')
                    continue

                descricao_produto = input('Forneça uma breve descrição ao produto:  ')

                produtos = {
                    'id': id_produto,
                    'produto': nome_produto,
                    'quantidade': quantidade_produto,
                    'medida': unidade_produto,
                    'descricao': descricao_produto
                }
                lista_usuario.append(produtos)

                id_produto += 1

                print("\nSua lista de compras:  ")   # Exibe a lista
                for item in lista_usuario:
                    print(f"ID: {item['id']} - {item['produto']}: {item['quantidade']}: {item['medida']}: {item['descricao']}")

                add_mais = input("Deseja continuar adionando itens? (s / n): ")

                if add_mais == "n" or add_mais == 'N':
                    lista_final = True
                else:
                    lista_final = False

        if menu == '2' :
            print("\nSua lista de compras:  ")
            for item in lista_usuario:
                print(f"ID: {item['id']} - {item['produto']}: {item['quantidade']}{item['medida']}: {item['descricao']}")

            id_remover = int(input('Digite o ID do item que deseja remover da lista de compras:    '))
            remover = next((item for item in lista_usuario if item['id'] == id_remover), None)

            if remover:
                lista_usuario.remove(remover)
                print(f"Item com ID {id_remover} removido.")
            else:
                print(f"Item com ID {id_remover} não encontrado.")


        if menu == '3':

            busca = input('Digite o nome ou parte do nome para buscar item em sua Lista de Compras: ')
            lista_usuario_str = [str(item['produto']) for item in lista_usuario]
            limite_similaridade = 50


            resultado = process.extract(busca, lista_usuario_str, scorer=fuzz.ratio, limit=3)
            print(f"{len(resultado)} Produto(s) encontrado(s): ")
            for nome_produto, similaridade, _ in resultado:
                if similaridade >= limite_similaridade:
                    print(f"Produto: {nome_produto} - Similaridade encontrada de: {similaridade:.2f}%")

                else:
                    print(f"Produto '{nome_produto}' tem uma similaridade de {similaridade:.2f}% e não atende ao limite de {limite_similaridade}%")


lista_compras()