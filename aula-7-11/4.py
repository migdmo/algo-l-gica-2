def cadastro(codigo,descricao,valor, lista_produtos):
    lista_produtos.append({ 'código': codigo,
                'descrição': descricao,
                'valor': valor
            })

def altera_produto(codigo, lista_produtos, novo_valor):
    for produto in lista_produtos:
        if(produto['código'] == codigo):
            produto['valor'] = novo_valor

produtos = []
for i in range(2):
    codigo = int(input("digite o código: "))
    descricao = input("digite a descrição: ")
    valor = float(input("digite o valor: "))
    
    cadastro(codigo,descricao,valor, produtos)  

print(produtos)
altera_produto(1234, produtos, 20)

print(produtos)