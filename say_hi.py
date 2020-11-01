#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     02/07/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def  say_hi(name, age):

  #return ('Olá {0} é nome / {1} é age'.format(name, age))

  return f'Olá {name} é nome / {age} é age'


print(say_hi('Ivan', 32))


def easy_unpack(elementes: tuple):
    el = elementes
    el1 = tuple(el)
    return (el1)

print(easy_unpack(5875474581))