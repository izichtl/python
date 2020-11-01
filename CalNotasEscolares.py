

n = int(input('Digite a quantidade de notas:  '))
lista = []
aux = []

for i in range(n):
    cont = i
    nota = float(input('Nota %i: ' %(cont+1)))
    lista.append(nota)
    aux.append(nota)

soma = sum(aux)
media = soma / len(aux)
acima_a = 0
acima_b = 0
abaixo = 0

for ii in range(len(aux)):
    if lista[ii] >= media:
        acima_a+=1
for ii in range(len(aux)):
    if lista[ii] >= 7:
        acima_b+=1
    else:
        abaixo+=1


print('-'*100)
print('Foram informadas %i notas.' % n)
print('As notas informadas foram:')
print(lista)

print('As notas informadas na ordem reversa foram:')
print(lista[::-1])

print('-'*100)
print('A soma das notas é %i:' %soma)
print('A média das notas é %.2f:' %media)
print('O numero de notas acima da média é %i:' %acima_a)
print('O numero de notas acima de 7 é %i:' %acima_b)
print('O numero de notas abixo de 7 é %i:' %abaixo)
print('-'*100)
print('Obrigado por usar o sistema de notas! by Ivan Zichtl')










































