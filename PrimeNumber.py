#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     05/07/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import math




def calcVol(radius):
    volume  = (4/3*math.pi)*(radius**3)
    return volume



print(calcVol(10))

def calFrete(produtos):
    x = 0
    custoFrete = 0
    for i in range(produtos):
        x += 1
        if x == 1:
          custoFrete += 3
        elif x != 1:
           custoFrete += 0.75
    return print(custoFrete)

calFrete(1212)


def primeNumb(numero):
    if numero == 3 or numero == 5 or numero == 7 or numero == 11:
        return print(numero, 'é um numero primo')
    elif numero % 3 != 0 and numero % 5 != 0 and numero % 7 != 0 and numero % 11 != 0:
        return print(numero, 'é um numero primo')
    else:
        return print(numero, 'não é um numero primo')

































