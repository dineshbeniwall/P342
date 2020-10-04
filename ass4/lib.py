# LU decomposion function break a given matrix into upper and lower triangle matrix
def ludecom(a):
    # Inisialize upper and lower matrix
    with open('l_and_u.txt') as f:
        u = []
        for i in range(0, 4):
            u.append(list(map(float, f.readline().split())))
    with open('l_and_u.txt') as f:
        l = []
        for i in range(0, 4):
            l.append(list(map(float, f.readline().split())))
    n = len(u)

    # lets start transformation of upper and lower triangle matrix
    for i in range(0, n):
        # upper triangle matrix
        # u[i][j]=a[i][j]-sum(from k=0 to i)(l[i][k]*u[k][j])
        for j in range(0, n):
            # sum(from j=0 to i)(l[i][k]*u[k][j])
            sum = 0
            for k in range(0, i):
                sum += l[i][k]*u[k][j]
            u[i][j] = a[i][j]-sum

        # lower triangle matrix
        # l[i][j] = (1/u[j][j])*(a[i][j]-sum(from k=0 to i)(l[i][k]*u[k][j]))
        # to get the lower triangle matrix just swap row indics to column indics
        # For example l[i][j] to l[j][i] and same for a[i][j]
        # this is because we have to solve column-wise for lower triangle
        for j in range(0, n):
            if i == j:
                l[i][i] = 1
            else:
                sum = 0
                for k in range(0, i):
                    sum += l[j][k]*u[k][i]
                l[j][i] = (a[j][i]-sum)/u[i][i]
    return l, u


def forback(a, b):
    l = ludecom(a)[0]
    u = ludecom(a)[1]
    n = len(u)
    # AX=B
    # A=LU => LUX=B
    # let UX=Z => LZ=B
    # Solve the system LZ=B by forward substitution
    # create zero matrix z
    z = []
    for i in range(0, n):
        z.append(0)
    # z1=b1/l11 and zi=(bi-sum(j=1 to i-1)lij*zj)/lii
    for i in range(0, n):
        if i == 0:
            z[i] = b[i]/l[i][i]
        else:
            sum = 0
            for j in range(0, i):
                sum += l[i][j]*z[j]
            z[i] = (b[i]-sum)/l[i][i]

    # Solve the system UX = Z by backward substitution
    # create zero matrix x
    x = []
    for i in range(0, n):
        x.append(0)
    # xn=zn and xi=(zi-sum(uij*uj))/uii
    i = n-2
    x[n-1] = z[n-1]/u[n-1][n-1]
    while i >= 0:
        sum = 0
        for j in range(i, n):
            sum += u[i][j]*x[j]
        x[i] = (z[i]-sum)/u[i][i]
        i = i-1

    return z, x


# from last assignment
def partialpivot(a):
    r = len(a)
    for k in range(0, r-1):
        if a[k][k] == 0:
            for i in range(k+1, r):
                if abs(a[i][k]) > abs(a[k][k]):
                    store = a[k]
                    a[k] = a[i]
                    a[i] = store
    return a


# check and does partialpivot by itself and return ready to use matrix
def makeready(a):
    # try to run ludecom function and it find ZeroDivisionError then pivoting
    try:
        ludecom(a)
    except ZeroDivisionError:
        a = partialpivot(a)
    return a


# find the determinant
def determinant(a):
    u = ludecom(a)[1]
    det = 1
    for i in range(0, len(u)):
        det = det*u[i][i]
    return det


# Inverse by LU decomposion
# AA^-1=I
# A*(first column)=first column............solve for all columns
def inverse(a, b):
    # here b is identity matrix
    # Inisialize ainverse matrix
    with open('l_and_u.txt') as f:
        ain = []
        for i in range(0, 4):
            ain.append(list(map(float, f.readline().split())))

    for i in range(0, len(ain)):
        c = []
        for j in range(0, len(ain)):
            # send i th column to solve
            c.append(b[j][i])
        x = forback(a, c)[1]
        # put solution of ith column into ainv
        for j in range(0, len(ain)):
            ain[j][i] = x[j]
    return ain
