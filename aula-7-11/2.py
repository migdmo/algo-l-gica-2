def conta_vogais(texto):
    vogais = ['a', 'e', 'i', 'o', 'u']
    _vogais = 0
    for letra in texto:
        if letra in vogais:
            _vogais+=1

    return _vogais
print(conta_vogais('Glauber e isadora'))