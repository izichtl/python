#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import random
import time
import getpass
import sys

y = random.randint(1,2)
x = random.randint(1,2)
#x = 1
#b = int(input('Usuário, insira um número: :'))
count = 0

while x != y:
    count = count + 1
#    print (x)
#    x = x + 1    count = count + 1
#   print (len(str(x)))

#while  x == y:
#   print ('Contagem finalizada:', count,'Loop')


if y == x:
    print (count)

print (y, x)