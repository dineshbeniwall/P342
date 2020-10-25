import lib
import math
from tabulate import tabulate


def func(x):
    f = math.exp(-x**2)
    return f


n = 10
Mn = lib.midpoint(0, 1, n, func)
n = 15
Tn = lib.trapezoidal(0, 1, n, func)
n = 25
Sn = lib.simpson(0, 1, n, func)

# apppend the results in tabulare formate
data = [['Method', 'N', 'Results', 'Max Error'], ["Midpoint", 10, Mn[0], Mn[1]],
        ["Trapezoidal", 15, Tn[0], Tn[1]], ["Simpson", 25, Sn[0], Sn[1]]]
print(tabulate(data, headers='firstrow'))

'''
Method         N    Results    Max Error
-----------  ---  ---------  -----------
Midpoint      10   0.747131  0.000827096
Trapezoidal   15   0.746552  0.0007309
Simpson       25   0.746824  0.00094739
'''
