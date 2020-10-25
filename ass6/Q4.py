import lib
from tabulate import tabulate


def func(x):
    f = (4/(1+x**2))
    return f


# append pi vs N in tabular format
data = [(lib.montecarlo(0, 1, N, func)[0],  N)
        for N in range(10, 1001, 10)]
print(tabulate(data, headers=['Pi', 'N']))
