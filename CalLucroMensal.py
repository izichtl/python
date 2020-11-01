#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     23/09/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>





n = int(input('Empresas:'))
m = int(input('Meses:'))

empresa = 1
print('_'*20)

while empresa <= n:
    mes = 1
    balanca = 0
    print('Empresa:{}:'.format(empresa))
    while mes <=m:
        print('Mês:{}:'.format(mes))

        ganho = int(input('Ganho da Empresa {} no mês {}:  R$'.format(empresa, mes)))
        gasto = int(input('Gasto da Empresa {} no mês {}:  R$'.format(empresa, mes)))
        balanca = balanca + (ganho - gasto)
        print('_'*20)
        mes = mes + 1


    if balanca == 0:
        print('A empresa {} não alteração de saldo!'.format(empresa))
    elif balanca > 0:
        print('A empresa {} teve lucro de:{}:'.format(empresa, balanca))
    else:
        print('A empresa {} teve prejuizo de:{}:'.format(empresa, balanca))

    empresa = empresa + 1
    print('__'*20)