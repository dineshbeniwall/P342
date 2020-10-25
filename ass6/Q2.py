import lib
from tabulate import tabulate


def func(x):
    f = (x/(1+x))
    return f


n = 5
Mn1 = lib.midpoint(1, 3, n, func)
Tn1 = lib.trapezoidal(1, 3, n, func)
Sn1 = lib.simpson(1, 3, n, func)

n = 10
Mn2 = lib.midpoint(1, 3, n, func)
Tn2 = lib.trapezoidal(1, 3, n, func)
Sn2 = lib.simpson(1, 3, n, func)

n = 25
Mn3 = lib.midpoint(1, 3, n, func)
Tn3 = lib.trapezoidal(1, 3, n, func)
Sn3 = lib.simpson(1, 3, n, func)

# append result into tabulare form and compareing
a = 1.30685281944  # actual anlaytical result
data = [['N', 'Midpoint', 'Trapezoidal', 'Simpson', 'Analytical result'],
        [5, Mn1[0], Tn1[0], Sn1[0], a], [10, Mn2[0], Tn2[0], Sn2[0], a], [25, Mn3[0], Tn3[0], Sn3[0], a]]

print(tabulate(data, headers='firstrow'))

'''
  N    Midpoint    Trapezoidal    Simpson    Analytical result
---  ----------  -------------  ---------  -------------------
  5     1.30809        1.30437    1.30685              1.30685
 10     1.30716        1.30623    1.30685              1.30685
 25     1.3069         1.30675    1.30685              1.30685
 '''
