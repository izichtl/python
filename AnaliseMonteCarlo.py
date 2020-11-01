



"""
import random

def rolarDado():
    rolar = random.randint(1,100)
    return rolar

x = 0

while x < 100:
        result = rolarDado()
        print (result)
        x+=1

"""

import random

def rolarDado():
    perdeu = 0
    ganhou = 0
    rolar = random.randint(1,100)
    if rolar == 100:
        print (rolar,'Perdeu')
        perdeu += 1
        return False
    elif rolar <= 50:
        print(rolar, "Perdeu2")
        perdeu += 1
        return False
    elif 100 > rolar >= 50:
        print (rolar,'Ganhou')
        ganhou += 1
        return True, perdeu, ganhou

x = 0

while x < 100:
        result = rolarDado()
        #print (result)
        x+=1

print(rolarDado(perdeu))