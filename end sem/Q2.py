import libraraay
import math
from tabulate import tabulate

# (4/math.sqrt(9.8))


def func(x):
    f = (1/math.sqrt(1 - (math.sin(math.pi/8))**2*math.sin(x)**2))
    return f


n = 10
T1 = libraraay.simpson(0, math.pi/2, n, func)

# T = (4*math.sqrt(L/g)) * integration solution
T = (4/math.sqrt(9.8))*T1[0]

print("Time period of oscillation : ", T)

'''
Method      N    Results
--------  ---  ---------
Simpson    10    2.0873200174795947


Time period of oscillation (T) :  2.0873200174795947

'''
