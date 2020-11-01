#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Formiga
#
# Created:     19/06/2019
# Copyright:   (c) Formiga 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import numpy as np
from numpy import array


altura = [1.70, 1.85, 1.66, 1.54, 1.81, 1.90]
peso = [85.7, 45.6, 55.3, 85.6, 74.2, 77.7]

nAltura = np.array(altura)
nPeso = np.array(peso)

imc = nPeso / nAltura ** 2


print(imc)