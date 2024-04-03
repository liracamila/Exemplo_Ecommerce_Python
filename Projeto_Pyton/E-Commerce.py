def cadastrar_produto(estoque):
    codigo = int(input("Digite o código do produto: "))
    categoria = input("Digite a categoria do produto: ")
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    preco = float(input("Digite o preço do produto: "))
    produto = {"codigo": codigo, "produto": nome, "info": descricao, "preco": preco}
    if categoria not in estoque:
        estoque[categoria] = []
        estoque[categoria].append(produto)
    else:
        estoque[categoria].append(produto)
    return estoque

def mostrar_produto(estoque):
    print ("--------------------------------------------")
    print ("---------- Informações do Produto ----------")
    print ("--------------------------------------------")
    for categoria in estoque:
        for produto in estoque[categoria]:
            print (f"Código: {produto['codigo']}")
            print (f"Categoria: {categoria}")
            print (f"Nome: {produto['produto']}")
            print (f"Descrição: {produto['info']}")
            print (f"Preço: R$ {produto['preco']}\n")

def mostra_produto_preco(estoque, preco_max):
    print ("--------------------------------------------")
    print ("---------- Informações do Produto ----------")
    print ("--------------------------------------------")
    for categoria in estoque:
        for produto in estoque[categoria]:
            if produto['preco'] <= preco_max:
                print (f"Código: {produto['codigo']}")
                print (f"Categoria: {categoria}")
                print (f"Nome: {produto['produto']}")
                print (f"Descrição: {produto['info']}")
                print (f"Preço: R$ {produto['preco']}\n")

estoque = {} #Armazenar os dados do meu sistema
estoque = {'Livros': [
                {
                    'codigo': 1,
                    'produto': 'Verity',
                    'info': 'Livro de ficção escrito por Colleen Hoover',
                    'preco': 44.26},
                 {
                    'codigo': 3,
                    'produto': 'Melhor do que nos filmes',
                    'info': 'Livro de romance',
                    'preco': 32.49},
                 {
                    'codigo': 5,
                    'produto': 'Biblia Sagrada',
                    'info': 'Livro mais lido do mundo',
                    'preco': 35.99}
              ],
           'Eletronicos': [
                {
                    'codigo': 2,
                    'produto': 'Fone de ouvido sem fio',
                    'info': 'Fone QCY Bluetooth',
                    'preco': 223.42},
                 {
                    'codigo': 4,
                    'produto': 'Smartfone Samsung Galaxy A54',
                    'info': 'Fone QCY Bluetooth',
                    'preco': 1649.00},
                 {
                    'codigo': 6,
                    'produto': 'Smart TV 70"',
                    'info': 'Televisão Smart Samsung de 70 polegadas',
                    'preco': 3799.89}
            ]}

#Menu interativo
while True:
    print("Seja bem-vindo a nossa loja virtual!")
    print("O que você deseja fazer? \n 1) Cadastro de produto \n 2) Mostrar produtos \n 3) Filtrar produto por preço \n 0) Sair do Sistema")
    opcao = int(input("Digite a opção desejada: "))

    #Cadastrar produtos
    if opcao == 1:
        cadastrar_produto (estoque)

    #Mostrar produtos
    elif opcao == 2:
        mostrar_produto(estoque)

    #Mostrar produtos dado um limite de preço
    elif opcao == 3:
        preco_max = float(input("Digite o limite máximo de preço a ser buscado: "))
        mostra_produto_preco(estoque, preco_max)

    #Sair do sistema
    elif opcao == 0:
        print("-------------------------------")
        print("----- Programa encerrado! -----")
        print("-------------------------------")
        break

    #Opção inválida
    else:
        print("Opção Inválida.")
