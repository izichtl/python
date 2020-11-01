#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     08/01/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

notas = []
cont = 0
while cont <= 4:
    nt = int(input('Insira a nota: :'))
    notas.append(nt)
    cont = cont + 1

total = sum(notas[0:len(notas)])
media = total / len(notas)

print ('Notas: ',notas[0:len(notas)])
print ('Total: ',total)
print ('Média: ',media)

if media < 50.0:
    print ('!!Você foi reprovado!!')

elif media > 50 and media < 90:
    print ('!!Parabéns - Você foi Aprovado!!')

if media > 90:
    print ('!!Parabéns - Você foi Aprovado com aproveitamento maior do que 90%!!')




