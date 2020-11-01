#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      Formiga
#
# Created:     02/07/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def easy_unpack(elementes: tuple) -> tuple:
    """impor
        returns a tuple with 3 elements - first, third and second to the last
    """


    return (elementes[0], elementes[2], elementes[-2])



def easy_unpack1(aa):
    """
        returns a tuple with 3 elements - first, third and second to the last
    """
    return tuple(aa[i] for i in [0,2,-2])




print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))