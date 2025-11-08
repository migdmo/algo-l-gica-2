def calcular(a, b, operacao):
    if operacao  == '+':
        return a+b
    if operacao == '-':
        return a-b
    if operacao == '*':
        return a*b
    if operacao == '/':
        return a/b

a = int(input())
b = int(input())
operacao = input()

print(calcular(a, b, operacao))