matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]
print(matriz)

print(matriz[0][1])

matriz[0][1] = "oi" # type: ignore


print(matriz[0][1])
print(matriz)


matriz.append([10,11,12])
print(matriz)