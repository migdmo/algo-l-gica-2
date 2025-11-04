def mean(lista):
    soma = 0
    for item in lista:
        soma += item
    return soma/len(lista)
def retorna_maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] > maior:
            maior = lista[i]
    return maior
def retorna_menor(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] < menor:
            menor = lista[i]
    return menor
def perc_aprovados(lista):
    aprovados = 0
    for nota in lista:
        if nota >= 7.0:
            aprovados += 1
    return (aprovados/(len(lista))*100)


nomes = []
notas = []
while True:
    nome = input("Digite o nome: ")
    nomes.append(nome)
    nota = float(input("Digite a nota: "))
    notas.append(nota)
    op = int(input("Deseja continuar a cadastrar? [0 - Não; 1 - Sim]: "))
    if op == 0:
        break
print(f'{len(nomes)} alunos foram cadastrados')

print(f'média das notas: {mean(notas):.2f}\nmaior nota: {retorna_maior(notas)}\nmenor nota: {retorna_menor(notas)}')
print(f'% de aprovados: {perc_aprovados(notas):.2f}%')
for i in range(len(notas)):
    if notas[i] >= 7.0:
        print(f'{nomes[i]}: aprovado(a)')
    else:
        print(f'{nomes[i]}: reprovado(a)')