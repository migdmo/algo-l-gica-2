idade = int(input("Digite sua idade: "))
valor = float(input("Digite o valor total da compra: "))


if idade < 25 or idade >= 60:
    if idade < 25:
        print('desconto base: 10%')
        if valor > 200.00:
            valor -= valor*0.1
        else:
            if valor > 500.00:
                valor -= valor*0.1
    else:
        if idade >= 60:
            print('desconto base: 15%')

            if valor > 200.00:
                print('desconto adicional de 5%')
                valor -= valor*0.22
            else:
                if valor > 500.00:
                    print('desconto adicional de 7%')
                    valor -= valor*0.22
print(f'valor final: {valor}')