num = input('Please type the number:')
try:
    n = int(num)
    if n >= 0:
        count = 0
        fac = 1
        while count < n:
            count = count+1
            fac = fac*count
        print(n, "! is:", fac)
    else:
        nn = -1*n
        count = 0
        fac = 1
        while count < nn:
            count = count+1
            fac = fac*count
        facc = -1*fac
        print(n, "! is:", facc)
except ValueError:
    print('Type a valid number!')
