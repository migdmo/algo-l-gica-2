import random

def media(numeros): return sum(numeros)/len(numeros)
def media_ponderada(numeros, pesos):
    soma = 0
    for i in range(len(numeros)):
        soma += numeros[i]*pesos[i]
    return soma/sum(pesos)


def razao_medias(media, media_ponderada):
    return media/media_ponderada

numeros = []
pesos = []
for i in range(10):
    numeros.append(random.randint(1, 10))
    pesos.append(random.randint(1, 5))
m = media(numeros)
mp = media_ponderada(numeros, pesos)
print(numeros)
print(pesos)
print(f'media = {m:.2f}\nmédia ponderada = {mp:.2f}\nrazão = {razao_medias(m, mp):.3f}')
