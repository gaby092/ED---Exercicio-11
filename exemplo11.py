opcao = 1
bd_estoque = [] #bd = banco de dados
while opcao != 4:
    print('='*30)
    print("1 - adicionar")
    print("2- consultar estoque")
    print("3- consultar valor total do estoque")
    print("4- sair")
    opcao = int(input('opcao >>>> '))
    if opcao == 1:
        print('-----adicionar')
        codigo = int(input('codigo: '))
        nome = input('nome: ')
        descricao = input('descricao: ')
        preco = float(input('preco: '))
        # adicionar a quantidade do produto no estoque
        produto = [codigo, nome, descricao, preco]
        bd_estoque.append (produto) # adicionar produto na lista estoque
        print('----------adicionado com sucesso--------')
    elif opcao == 2:
        print('-----estoque-----')
        # percorrer o bd
        print('codigo\tnome\tdescricao\tpreco')
        for prod in bd_estoque:
           print(prod[0],end='\t')
           print(prod[1],end='\t')
           print(prod[2],end='\t')
           print(prod[3])
        #  print(f'codigo: {prod[0]}')
        #  print(f'nome: {prod[1]}')
        #  print(f'descricao: {prod[2]}')
        #  print(f'preco: {prod[3]:.2f}')
        print('-----fim do estoque-----')
    elif opcao == 3:
        pass    # implementar aqui
    elif opcao == 4:
        print('-----saindo')
    else:
        print('opcao incorreta')