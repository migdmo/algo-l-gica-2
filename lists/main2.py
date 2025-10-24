lista = []

for i in range(5):
    lista.append(int(input(f"Digite a nota para o aluno {i+1}: ")))

soma = 0
for nota in lista:
    soma += nota


print(lista)
print(soma)
print(f"a média das notas é: {soma/len(lista)}")


letras = ["a","c","b"]
letras.sort()
print(letras)