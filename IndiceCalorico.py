#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     02/01/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------


gra_p = float (input('Gramas da porção: '))
cal_p = float (input('Calorias da porção: '))

g100 = 100*cal_p/gra_p
id_cal = 100*cal_p/gra_p/100

print ('Gramas da Porção:', int(gra_p),'g')
print ('Calorias da Porção:', int(cal_p), 'Kcals')
print ('100g: ', int(g100),'Kcal')
print ('Indice Calórico: %.1f '%id_cal)


def IndiceCalorico(gra_p, cal_p):
    g100 = 100*cal_p/gra_p
    id_cal = 100*cal_p/gra_p/100

    #print ('Gramas da Porção:', int(gra_p),'g')
    #print ('Calorias da Porção:', int(cal_p), 'Kcals')
    print ('100g: ', int(g100),'Kcal')
    print ('Indice Calórico: %.1f '%id_cal)

calculo = (lambda gra_p, cal_p: 100*cal_p/gra_p/100 )

print('Indice Calórico: %.2f' %(calculo(210, 212)))


"""
IndiceCalorico(210, 728)"""