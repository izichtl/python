#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Formiga
#
# Created:     21/06/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
import matplotlib as plt

def tabela(valIMC):
    if valIMC   < 16:
        return str(valIMC) + ':          Magreza grave'
    elif valIMC < 17:
        return str(valIMC) + ':          Magreza moderada'
    elif valIMC < 18.5:
        return str(valIMC) + ':          Magreza leve'
    elif valIMC < 25:
        return str(valIMC) + ':          Saudável'
    elif valIMC < 30:
        return str(valIMC) + ':          Obesidade 1'
    elif valIMC < 40:
        return str(valIMC) + '           Obesidade 2'
    else:
        return str(valIMC) + ':          Obesidade 3'




altura, peso, força = np.loadtxt('C:/Users/Formiga/Desktop/@TRABALHOS/meusite/peso.csv',
                                    delimiter=';',
                                    unpack=True,
                                    dtype='float')
imc = peso / altura **2





#print('-'*50)
#print('-'*50)
print('.'*50)

print('Mín:                     ', tabela(np.amin(imc)))
print('Máx:                     ', tabela(np.amax(imc)))
print('Máx - Mín:               ', tabela(np.ptp(imc)))

print('Média Tradicional:       ', tabela(np.median(imc)))

print('Média por Força:         ', tabela(np.average(imc)))

print('Média Aritimética:       ', tabela(np.mean(imc)))

print('Desvio Padrão:           ', tabela(np.std(imc)))

print('Variância:               ', tabela(np.var(imc)))
print('.'*50)



print('Percentil')
print('1º Percentíl:            ', tabela(np.median(np.percentile(imc, q=range(0,25)))))
print('2º Percentíl:            ', tabela(np.median(np.percentile(imc, q=range(26,50)))))
print('3º Percentíl:            ', tabela(np.median(np.percentile(imc, q=range(51,75)))))
print('4º Percentíl:            ', tabela(np.median(np.percentile(imc, q=range(76,100)))))
print('.'*50)





