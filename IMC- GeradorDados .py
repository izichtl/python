#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     21/06/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass



from random import uniform
from random import randint

texto = []



def obterTexto():
    for i in range(1, 5000):
        texto.append(str(uniform(1.50, 2.05)) + ';' +
                    str(uniform(50, 110)) + ';' +
                    str(randint(0,10)) + '\n')


def gerarDados():
    arq = 'C:/Users/Formiga/Desktop/@TRABALHOS/meusite/peso.csv'
    entrada = open(arq, "w+", encoding='UTF-8')
    obterTexto()
    entrada.writelines(texto)
    entrada.close()

if __name__ == '__main__':
    gerarDados()


