#11 passos O(n)
def soma1(n):
    soma = 0
    for i in range(n + 1):
        soma += i

    return soma


print(soma1(10))


# print(%timeit soma1(10))

#3 passos - O(1)
def soma2(n):
    return (n * (n + 1)) / 2

print(soma2(10))

def lista1():
    lista = []
    for i in range(1000):
        lista += 1
    return lista

print(lista1())

def lista2():
  return range(1000)

l = lista2()

for i in l:
  print(i)
