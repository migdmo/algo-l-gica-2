# nome = input("Digite seu nome: ")
# valor = float(input("Digite um valor: "))
# quantidade = int(input("Digite a quantidade: "))
# metodo = int(input("Digite o método de pagamento [1 - à vista; 2 - à prazo]: "))
# total = 0 

# if metodo == 2:
#     n_parcelas = int(input("Digite o número de parcelas: "))
#     if n_parcelas <= 5:
#         total = (quantidade*valor) + (quantidade*valor)*(15/100)
#     else:
#         total = (quantidade*valor) + (quantidade*valor)*(20/100)
# else:
#     if metodo == 1:
#         total = (quantidade*valor) + (quantidade*valor)*(10/100)

# print(f"o total é {total:.2f}")

valores = [1, 2, 3, 4, 5]
for x in valores:
    print(x)


for x in range(3, 10, 2):
    print(f"o valor é {x}")