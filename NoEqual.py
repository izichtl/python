#
#
#
#SERIE DE NUMEROS SEM REPETIÇÕES
#
#
#

n = int(input('Digite o numero de elementos: '))
lista = []
aux = []

for i in range(n):
    elemento = int(input('O elemento: %i de %i é: ' %(i+1, n)))
    lista.append(elemento)
    aux.append(elemento)

for ele in aux:
    aparições = lista.count(ele)
    for i in range(aparições-1):
        lista.remove(ele)
print(aux)
print(lista)

