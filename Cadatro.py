
def cadastrar_produto(produtos):
    nome = input("Digite o nome do produto: ")
    descricao = input("Digite a descrição do produto: ")
    valor = float(input("Digite o valor do produto: "))
    disponivel = input("Disponível para venda? (sim/não): ").strip().lower() == 'sim'

    produto = {
        'nome': nome,
        'descricao': descricao,
        'valor': valor,
        'disponivel': disponivel
    }
    produtos.append(produto)
    print(f"O produto {nome} foi cadastrado com sucesso!")
    listar_produtos(produtos)  


def listar_produtos(produtos):
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    print("\nLista de Produtos:")
    print("Nome do Produto | Valor")
    print("----------------|------")
    for produto in produtos_ordenados:
        print(f"{produto['nome']} | R$ {produto['valor']:.2f}")
    print("\nDigite '1' para cadastrar um novo produto ou '0' para voltar ao menu.")
    escolha = input("Escolha uma opção: ")
    if escolha == '1':
        cadastrar_produto(produtos)


produtos = []

while True:
    print("\n--Cadastro de Produtos--")
    print("")
    print("1 - Cadastrar novo produto")
    print("2 - Listar produtos")
    print("3 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == '1':
        cadastrar_produto(produtos)
    elif escolha == '2':
        listar_produtos(produtos)
    elif escolha == '3':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida, tente novamente.")