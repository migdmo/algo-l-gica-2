produtos = []
qtds = []
valores = []
totalGeral = 0
for i in range(2):
    qtd = int(input("Digite a quantidade do produto: "))
    qtds.append(qtd)
    valor = float(input("Digite o valor do produto: "))
    valores.append(valor)
    produtos.append((qtd*valor))
    totalGeral += (qtd*valor)

maior = produtos[0]
iMaior = 0
for i in range(len(qtds)):
    if valores[i] >maior:
        maior = valores[i]
        iMaior = i
print(f"quantidade do produto com maior valor {qtds[iMaior]}")