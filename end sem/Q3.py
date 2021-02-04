import libraraay

# for first parts
# w(t)=wo+wc*t
print("part one", libraraay.fitting('esem_table.txt', '\t', 1, plot=False))
'''
{'Coefficients': [[1.9576363636363632], [-0.44363636363636405]], "Pearson's r": 0.9882421864887738}
w(t) = wo + wc*t
w(t) = 1.9576363636363632 -0.44363636363636405*t
Pearson's r =  0.9882421864887738
'''
# for second parts
# w(t)=wo*exp(-wc*t)
# y=Aexp(-bx)
# lny = lnA - Blnx
print("part two", libraraay.expofitting('esem_table.txt', '\t'))
'''
{'Coefficients': [[0.7871196117658699], [-0.39334527099852357]], "Pearson's r": 0.9882421864887736}
w(t) = w(t)=wo*exp(-wc*t)
w(t) = 0.7871196117658699 -0.39334527099852357*ln(t)
or
w(t) = log(exp(0.7871196117658699)) - 0.39334527099852357*log(t)
Pearson's r = 0.9882421864887736
'''
