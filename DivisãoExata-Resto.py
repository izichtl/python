#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     23/09/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()





num = int(input('Insira um numero:'))
z, y, w = 1, 2, 3
while z * y * w <= num:
    ln = z * y * w
    print('{} X {} X {} == {}'.format(z, y, w, ln))
    z += 1
    y += 1
    w += 1

    if z * y * w > num:
        print('_'*50)
        print('Resposta: {} X {} X {} == {} :'.format(z, y, w, ln))
        resto = num - ln
        if resto == 0:
            print('Cálculo Exato')
        else:
            print("Resta: {}".format(resto))
'''
    else:


'''
