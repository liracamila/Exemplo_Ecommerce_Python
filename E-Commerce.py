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


estoque = {} #Armazenar os dados do meu sistema
estoque = {'Livros':
                [{'codigo': 1, 'produto': 'Verity', 'info': 'Livro de ficção escrito por Colleen Hoover', 'preco': 44.26},
                 {'codigo': 3, 'produto': 'Biblia Sagrada', 'info': 'Livro mais lido do mundo', 'preco': 35.99}],
           'Eletronicos':
                [{'codigo': 2, 'produto': 'Fone de ouvido sem fio', 'info': 'Fone QCY Bluetooth', 'preco': 223.42}]}
# cadastrar_produto (estoque)
mostrar_produto(estoque)
