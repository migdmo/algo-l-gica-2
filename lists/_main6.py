a = [1, 3, 5]

# b aponta para a mesma referência de a
#b = a

# b é uma cópia de a
b = a[:]
print(b)

a.append(-5)
print(a)
