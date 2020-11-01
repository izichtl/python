#-------------------------------------------------------------------------------
# Name:        Indice Calórico - Lambda
# Purpose:     Calcular a relação massa calorida dos alimentos.
#
# Author:      Formiga -  IZ
#
# Created:     02/10/2019
# Copyright:   (c) Formiga 2019
# Licence:     <Comercial Free>
#-------------------------------------------------------------------------------

#input dos valores
gra_p = float (input('Gramas da porção: '))
cal_p = float (input('Calorias da porção: '))

#Calculo da relação da porção com a quantidade de calorias.
calculo = (lambda gra_p, cal_p: 100*cal_p/gra_p/100 )
print('Indice Calórico: %.2f' %(calculo(gra_p, cal_p)))
