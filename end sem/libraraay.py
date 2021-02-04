import math
import random

import matplotlib.pyplot as plt

# square fitting


def data(file, char_):
    """
    Open a file that contains
    data to fit | Format (x,y)
    char_ : separator character
           ' '     <== Space delimited
           '\t'    <== Tabs delimited
           ','     <== Comma delimited
    """
    data = open(file, 'r')
    line = [line.rstrip().split(char_)
            for line in data]
    x = column(line, 0)
    y = column(line, 1)
    for i in range(len(x)):
        x[i] = float(x[i])
        y[i] = float(y[i])
    return x, y


def column(a, i):
    """
    Returns a specific column
    of a multidimensional list
    """
    return [row[i] for row in a]


def transpose(a):
    """
    Returns the transpose of a
    mutidimensional list
    """
    trans_a = []
    for i in range(len(a[0])):
        trans_a.append(column(a, i))
    return trans_a


def polynomial(M, i):
    """
    Helps to create the matrix A
    """
    row = [1]
    for exp in range(1, M+1):
        row.append(i ** exp)
    return row


def matrix_A(x, M):
    """
    Create matrix A to fit data
    to a polynomial of order M
    """
    N = len(x)
    matrix_A = []
    for i in x:
        matrix_A.append(polynomial(M, i))
    return matrix_A


def plots(x, y1, y2):
    """
    Function to plot
    """
    fig = plt.figure(figsize=(4, 4))
    a = fig.add_subplot(1, 1, 1)
    a.plot(x, y1, 'k|', marker='o', markersize=4, markeredgewidth=1,
           markeredgecolor='k', markerfacecolor='w', label='Original data')
    a.plot(x, y2, 'r-', linewidth=1, label='Fitted')
    a.set_ylabel('Y')
    a.set_xlabel('X')
    a.spines['right'].set_visible(False)
    a.spines['top'].set_visible(False)
    a.legend(ncol=2, loc='upper left',
             fontsize=9, frameon=False)
    fig.tight_layout()
    return


def function(x, pol_coeff):
    """
    Function to evaluate the polynomial from fitting process
    """
    res = 0
    for exp, coeff in enumerate(pol_coeff):
        res = res + coeff[0] * x ** exp
    return res


def fitting(file, char_, M, plot=True):
    """
    Main function:
    File   : file name containing data
    char_  : character separator
    M      : order of polynomial to fit data
    plot   : If True ==> Plot , if False ==> pass
    """
    points = data(file, char_)
    x, Y = points[0], points[1]
    y = [Y[i: (i+1)] for i in range(len(Y))]
    A_transpose = transpose(matrix_A(x, M))
    Matrix_S = matrix_mult(A_transpose, matrix_A(x, M))
    vector_Z = matrix_mult(A_transpose, y)
    S_inverse = inverse(Matrix_S)
    pol_coeff = matrix_mult(S_inverse, vector_Z)
    y_calc = []
    for value in x:
        y_calc.append(function(value, pol_coeff))
    if plot == True:
        plots(x, Y, y_calc)
        plt.show()
    elif plot == False:
        pass
    y_mean = sum(Y) / len(Y)
    sum_upper = 0
    sum_lower = 0
    for i in range(len(x)):
        sum_upper = sum_upper + (y_calc[i] - y_mean) ** 2
        sum_lower = sum_lower + (Y[i] - y_mean) ** 2
    R_2 = sum_upper / sum_lower
    return {'Coefficients': pol_coeff, "Pearson's r": math.sqrt(R_2)}


def expofitting(file, char_):

    (x, y) = data(file, char_)
    # q=xy, w=xylny, e=y, r=x2y, t=xy, u=ylny
    q = 0
    w = 0
    e = 0
    r = 0
    t = 0
    u = 0
    p = 0
    for i in range(len(x)):
        q += x[i]*y[i]
        w += x[i]*y[i]*math.log(y[i])
        e += y[i]
        r += x[i]**2*y[i]
        t += x[i]*y[i]
        u += y[i]*math.log(y[i])
        p += x[i]
    a = (r*u-q*w)/(e*r-q**2)
    b = (e*w-q*u)/(e*r-q**2)
    ssx = 0
    ssy = 0
    for i in range(len(x)):
        ssx += (x[i]-p/len(x))**2
        ssy += (y[i]-e/len(x))**2
    sxy = q-len(x)*p/len(x)*e/len(x)
    r = sxy**2/(ssx*ssy)

    return {'Coefficients': [a, b], "Pearson's r": math.sqrt(r)}


'''################################################################################################'''
'''##################################################################################################'''

'''################################################################################################'''
'''##################################################################################################'''

'''################################################################################################'''
'''##################################################################################################'''

'''################################################################################################'''
'''##################################################################################################'''

'''################################################################################################'''
'''##################################################################################################'''


# monte carlo for ellipsoid volume
def ellipsoid(a, b, c, N):
    count = 0
    X = []
    Y = []
    Z = []
    # equation of ellipsoid
    # x2/a2+y2/b2+z2/c2=1
    for i in range(0, N):
        x = -a+(a+a)*random.random()
        y = -b+(b+b)*random.random()
        z = -c+(c+c)*random.random()
        if(x**2/a**2+y**2/b**2+z**2/c**2 <= 1):
            count += 1
            X.append(x)
            Y.append(y)
            Z.append(z)
    # volume of ellipsoid=8abc*p(f)
    v = 8*a*b*c*count/N
    # fractional error
    e = (12.56637-v)/12.56637
    return v, X, Y, Z, e


# random walk analysis(steps, walks, file to store data)
def rnwanalysis(N, M, file):
    # list for store the data
    dx = 0.0
    dy = 0.0
    r2 = 0.0
    r = 0.0
    # M walks of N steps
    for i in range(0, M):
        a = randomwalk(N)
        # append first 5 walks of N steps
        if i < 5:
            file.writelines("[#################################]"), file.writelines(
                "\n""\n"), file.writelines("\n""\n"), file.writelines("\n""\n")
            file.writelines("[")
            file.writelines("%s," % i for i in a[0])
            file.writelines("]"), file.writelines("[#################################]"), file.writelines(
                "\n""\n"), file.writelines("\n""\n")
            file.writelines("[")
            file.writelines("%s," % i for i in a[1])
            file.writelines("]")
            file.writelines("\n""\n"), file.writelines("[#################################]")
        # analysis
        # R**2=x**2+y**2
        r2 += (a[2][-1])**2
        # distance
        r += a[2][-1]
        dx += a[0][-1]
        dy += a[1][-1]
    # average Delta X
    Dx = dx/M
    # average Delta Y
    Dy = dy/M
    # average distance
    avgr = r/M
    # RMS
    rms = math.sqrt(r2/M)
    return Dx, Dy, avgr, rms


# randomwalk
def randomwalk(N):
    dx = 0.0
    dy = 0.0
    x = [0]
    y = [0]
    r = []
    R = 0
    for i in range(0, N):
        th = random.uniform(0, 2*math.pi)
        dx += math.cos(th)
        dy += math.sin(th)
        R = math.sqrt(dx**2+dy**2)
        x.append(dx)
        y.append(dy)
    r.append(R)
    return x, y, r


'''################################################################################################'''
'''##################################################################################################'''

# euler's method
# euler(function,y0,x0,x_last,step)


def euler(f, y0, x0, xl, h):
    xn = x0
    yn = y0
    x = []
    y = []
    while xn < xl:
        yn1 = yn+h*f(yn, xn)
        x.append(xn)
        y.append(yn)
        xn += h
        yn = yn1
    return x, y


# runge_kutta_4
# rk4(function1,function2,firstdiff_y0,y0,x0,last X, step)
def rk4(f1, f2, yi0, y0, x0, xl, h):
    z0 = yi0
    x = []
    y = []
    g = []
    while x0 < xl:
        k1y = h*f1(z0, x0)
        k1z = h*f2(z0, x0)

        k2y = h*f1(z0+k1z/2, x0+h/2)
        k2z = h*f2(z0+k1z/2, x0+h/2)

        k3y = h*f1(z0+k2z/2, x0+h/2)
        k3z = h*f2(z0+k2z/2, x0+h/2)

        k4y = h*f1(z0+k3z, x0+h)
        k4z = h*f2(z0+k3z, x0+h)

        yn = y0+(k1y+2*k2y+2*k3y+k4y)/6
        zn = z0+(k1z+2*k2z+2*k3z+k4z)/6
        # store values
        x.append(x0)
        y.append(yn)
        g.append(zn)
        x0 += h
        y0 = yn
        z0 = zn
    return x, y, g


# shooting method using runge_kutta_4
# rk4shooting(function1,function2,firstdiff_yi,xi,y0,x0,last X, step,high guess,low guess)
def rk4shooting(f1, f2, yi, xi, y0, x0, xl, h, gh, gl):

    # last element of Y form sloutions of diff eqn(using rk4)
    (x1, y1, z1) = rk4(f1, f2, gh, y0, x0, xl, h)
    yh = y1[-1]
    (x2, y2, z2) = rk4(f1, f2, gl, y0, x0, xl, h)
    yl = y2[-1]

    # checking guesses and guide in right direction
    if (yh > yi and yl > yi) or (yh < yi and yl < yi):
        return print("Change guesses")
    elif yh < yi and yl < yi:
        return print("Take another high guess ")
    elif yh > yi and yl > yi:
        return print("Take another low guess ")

    # finding solution
    while abs(yh - yi) > 0.001 or abs(yl - yi) > 0.001:
        if abs(yh-yi) < 0.001:
            return x1, y1, z1
        if abs(yl-yi) < 0.001:
            return x2, y2, z2
        if yh > yi and yl < yi:
            g = gl + (((gh - gl)/(yh - yl)) * (yi - yl))
            (x3, y3, z3) = rk4(f1, f2, g, y0, x0, xl, h)
            if abs(y3[-1]-yi) < 0.001:
                return x3, y3, z3
            elif g < yi:
                gl = g
            else:
                gh = g
        if yl > yi and yh < yi:
            g = gh+(((gl-gh)/(yl-yh))*(yi-yh))
            (x3, y3, z3) = rk4(f1, f2, g, y0, x0, xl, h)
            if abs(y3[-1]-yi) < 0.001:
                return x3, y3, z3
            elif g < yi:
                gh = g
            else:
                gl = g


'''#########################################################################################################'''
'''#########################################################################################################'''


# double differentiation
def ddx(f, x):
    h = 0.00001
    fddx = (f(x+h)+f(x-h)-2*f(x))/(h**2)
    return fddx


# fourth order differentiation
def ddddx(f, x):
    h = 0.00001
    fddddx = (ddx(f, x+h)+ddx(f, x-h)-2*ddx(f, x))/(h**2)
    return fddddx

# Midpoint / Rectangle method


def midpoint(a, b, n, f):
    # divide integration range in N equal parts
    h = (b-a)/n
    Mn = 0
    dxmax = 0
    for i in range(0, n):
        # midpoint of each intervals
        x = ((a+i*h)+(a+(i+1)*h))/2
        Mn += h*f(x)
        # double differentiation for error
        fddx = ddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # max error
    er = (((b-a)**3)/(24*(n**2)))*dxmax
    return Mn, er


# Trapezoidal rule
def trapezoidal(a, b, n, f):
    # divide integration range in N equal parts
    h = (b-a)/n
    Tn = 0
    x0 = a
    xpre = x0
    dxmax = 0
    for i in range(1, n+1):
        # endpoint of each intervals
        xi = x0+i*h
        Tn += (h/2)*(f(xpre)+f(xi))
        xpre = xi
        # double differentiation for error
        fddx = ddx(f, xi)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # max error
    er = (((b-a)**3)/(12*(n**2)))*dxmax
    return Tn, er


# Simpson's rule
def simpson(a, b, n, f):
    h = (b-a)/(2*n)
    S = 0
    dxmax = 0
    # odd terms
    for i in range(1, n+1):
        x = h*(-1+2*i)+a
        S += 4*f(x)
        # fourth order differentiation for error
        fddx = ddddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # even terms
    for i in range(1, n):
        x = 2*h*i+a
        S += 2*f(x)
        fddx = ddddx(f, x)
        if abs(fddx) > dxmax:
            dxmax = abs(fddx)
    # integral
    Sn = (h/3)*(f(a)+f(b)+S)
    # max error
    er = (((b-a)**5)/(180*(n**4)))*dxmax
    return Sn, er


# Montecarlo integration
def montecarlo(a, b, n, f):
    Fn = 0
    sigmaf = 0
    for i in range(1, n+1):
        # random number
        x = a+(b-a)*random.random()
        # intergral
        Fn += ((b-a)/n)*f(x)
        # error
        sigmaf += math.sqrt(((1/n)*(f(x)**2))-(((1/n)*f(x))**2))
    return Fn, sigmaf


'''#############################################################################'''
'''#############################################################################'''


# Polynomial function. Input coff and value of x


def polynomiale(coff, x):
    # order of polynomial
    n = len(coff)-1
    p = 0
    for i in range(0, len(coff)):
        p = coff[i]*x**(n-i)+p
    return p


# polynomial synthetic division
def polydivide(coff, d):
    ncoff = []
    ncoff.append(coff[0])
    i = 0
    for i in range(0, len(coff)-2):
        ncoff.append(ncoff[i]*d+coff[i+1])
    return ncoff


# differentiation of polynomial
def differentiation(coff, x):
    h = 0.0001
    fd = (polynomial(coff, x+h)-polynomial(coff, x-h))/(2*h)
    return fd


# double differentiation of polynomial
def doublediff(coff, x):
    h = 0.0001
    fdd = (differentiation(coff, x+h)-differentiation(coff, x-h))/(2*h)
    return fdd


# Roots of polynomial
# input coff. of polynomial, alpha0=initial guess, epsilon, n=order of polynomial
def roots(coff, alpha0, epsilon, n):
    root = []
    alphai = alpha0
    for i in range(0, n):
        alphaii = 0
        if polynomial(coff, alpha0) < epsilon:
            root.append(alphai)
            coff = polydivide(coff, alphai)
        else:
            while abs(alphaii-alphai) > epsilon:
                p = polynomial(coff, alphai)
                pi = differentiation(coff, alphai)
                pii = doublediff(coff, alphai)
                g = pi/p
                h = g**2-pii/p
                d1 = g+((n-1)*(n*h-g**2))**(1/2)
                d2 = g-((n-1)*(n*h-g**2))**(1/2)
                if abs(d1) > abs(d2):
                    a = n/d1
                else:
                    a = n/d2
                alphaii = alphai-a
                alphai = alphaii
            root.append(alphai)
            coff = polydivide(coff, alphai)
        # print(coff, alphai)
    return root


class color:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# bracketing of roots :
def bracketing(a, b, func):
    i = 0
    while i < 12:  # Limiting no.of iterations to 12
        if func(a) * func(b) < 0:
            return a, b
        elif func(a) * func(b) == 0:
            if func(a) == 0:
                print("root of the equation:", a)
            if func(b) == 0:
                print("root of the equation:", b)
        elif func(a) * func(b) > 0:
            if abs(func(a)) < abs(func(b)):
                a = a - 1.5 * (b - a)
            else:
                b = b + 1.5 * (b - a)
        i += 1
    if i > 12:
        print("Iterations are more than 12, try another guess")
    else:
        return a, b


# Bisection method for roots
def bisection(a, b, func):
    file = open('Q1_bisection.txt', 'w')
    a, b = bracketing(a, b, func)  # Recalling the function
    i = 1
    file.write(color.BOLD + "Bisection method" + color.END + "\n{:>3}       {:>10} ".format("Iterations",
                                                                                            "Absolute error") + "\n")
    while abs(a - b) > 0.000001 and i < 200:
        c = (a + b) / 2
        if func(a) * func(c) < 0:
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - b)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            file.write("{:>3}         {:>10.20f} ".format(i, abs(c - a)) + "\n")
            a = c
        else:
            print("While iterating through the points one of the point has landed on the root of the equation.")
            print(a, b)
            break
        i += 1
    file.close()
    return b


# regular falsi method for roots
def regularfalsi(a, b, func):
    # file = open('Q1_regular_falsi.txt', 'w')
    bracketing(a, b, func)
    i = 1
    # file.write(color.BOLD + "False Position method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
    #                                                                                              "Absolute error") + "\n")
    c = 1
    c_n1 = a
    while abs(c - c_n1) > 0.000001 and i < 200:
        c = b - ((b - a) * func(b)) / (func(b) - func(a))
        if func(a) * func(c) < 0:
            c_n1 = b
            #file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            b = c
        elif func(a) * func(c) > 0:
            c_n1 = a
            #file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
            a = c
        else:
            if func(a) == 0:
                print(a, " is the root.")
            elif func(b) == 0:
                print(b, " is the root.")
        i += 1
    #file.write("{:>3}         {:>10.20f} ".format(i, abs(c - c_n1)) + "\n")
    # file.close()
    return c


# Newton raphson method
def newtonraphson(x_o, func):
    # file = open('Q1_Newton_Raphson.txt', 'w')
    h = 0.0001
    der = (func(x_o+h) - func(x_o-h))/(2*h)  # Derivative of the function
    x = x_o - (func(x_o) / der)
    copy = 1
    i = 1
    # file.write(color.BOLD + "Newton-Raphson method." + color.END + "\n{:>3}       {:>10} ".format("Iterations",
    #                                                                                              "Absolute error") + "\n")
    while abs(x - copy) > 0.000001 and i < 200:
        copy = x
        x_o = x
        der = (func(x_o + h) - func(x_o - h)) / (2 * h)
        x = x_o - (func(x_o) / der)
        '''
        file.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
        i += 1
    file.write("{:>3}         {:>10.20f} ".format(i, abs(x - copy)) + "\n")
    file.close()
    '''
    return x


'''######################################################################################################################################'''
'''#######################################################################################################################################'''
# sum and dot of two vecotrs


def sumdotvector(A, B):
    sum = []
    dot = 0
    for i, j in zip(A, B):
        sum.append(i+j)
        dot += i*j
    return sum, dot


# general matrix multipalication

def matrixmuliply(M, y):
    # general matrix multipalication
    a = []
    b = []
    c = []
    product = [a, b, c]
    try:
        for rowx, r in zip(M, product):
            j = 0  # columns
            while j != len(y[0]):
                k = 0
                sum = 0
                for rowy in y:
                    sum += rowx[k]*rowy[j]
                    k += 1
                r.append(sum)
                j += 1
        return product
    except TypeError:
        for rowx, r in zip(M, product):
            k = 0
            sum = 0
            for rowy in y:
                sum += rowx[k]*rowy
                k += 1
            a.append(sum)
        return a


'''######################################################################################################################################'''
'''#######################################################################################################################################'''
# solutions of matrix without augmentation


def partialpivot(a, b):
    r = len(b)
    for k in range(0, r-1):
        if a[k][k] == 0:
            for i in range(k+1, r):
                if abs(a[i][k]) > abs(a[k][k]):
                    store = a[k]
                    a[k] = a[i]
                    a[i] = store
                    store = b[k]
                    b[k] = b[i]
                    b[i] = store
    return a, b


def gaussjordan(a, b):
    partialpivot(a, b)
    r = len(b)
    for k in range(0, r):
        pivot = a[k][k]
        # for the pivot row divide by akk
        for j in range(k, r):
            a[k][j] = a[k][j]/pivot
        b[k] = b[k]/pivot
        # for the non pivot row
        for i in range(0, r):
            if i == k or a[i][k] == 0:
                continue
            factor = a[i][k]
            # substraction
            for d in range(k, r):
                a[i][d] = a[i][d]-factor * a[k][d]
            b[i] = b[i]-factor * b[k]
    return a, b

# inverse with augmentation


def augment(a, b):
    for i in range(0, len(a)):
        try:
            for j in range(0, len(b[0])):
                a[i].append(b[i][j])
        except TypeError:
            a[i].append(b[i])
    return a


def partialpivot2(a):
    r = len(a)
    for k in range(0, r-1):
        if a[k][k] == 0:
            for i in range(k+1, r):
                if abs(a[i][k]) > abs(a[k][k]):
                    store = a[k]
                    a[k] = a[i]
                    a[i] = store
    return a


def gaussjordan2(a, b):
    augment(a, b)
    partialpivot2(a)
    row = len(a)
    col = len(a[0])
    for k in range(0, row):
        pivot = a[k][k]
        # for the pivot row divide by akk
        for j in range(k, col):
            a[k][j] = a[k][j]/pivot
        # for the non pivot row
        for i in range(0, row):
            if i == k or a[i][k] == 0:
                continue
            factor = a[i][k]
            # substraction
            for d in range(k, col):
                a[i][d] = a[i][d]-factor * a[k][d]
    return a


# b is identity matrix
def inversee(a, b):
    gaussjordan2(a, b)
    sol = [[], [], []]
    for i in range(0, len(a)):
        for j in range(len(a), len(a[1])):
            sol[i].append(a[i][j])
    return sol


'''######################################################################################################################################'''
'''#######################################################################################################################################'''

'''######################################################################################################################################'''
'''#######################################################################################################################################'''


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


# check and does partialpivot by itself and return ready to use matrix
def makeready(a):
    # try to run ludecom function and it find ZeroDivisionError then pivoting
    try:
        ludecom(a)
    except ZeroDivisionError:
        a = partialpivot2(a)
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
def inverselu(a, b):
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


'''######################################################################################################################################'''
'''#######################################################################################################################################'''

'''######################################################################################################################################'''
'''#######################################################################################################################################'''


def matrix_mult(a, b):
    """
    Matrix multiplication
    """
    zip_b = zip(*b)
    zip_b = list(zip_b)
    matrix = [[sum(a_i * b_i for a_i,
                   b_i in zip(row_a, col_b))
               for col_b in zip_b] for row_a in a]
    return matrix


def Identity(n):
    """
    Create a identity matrix
    """
    result = d_2_List(n, n)
    for i in range(n):
        result[i][i] = 1
    return result


def d_2_List(rows, cols):
    """
    Auxiliar function
    to calculate inverse
    """
    a = []
    for row in range(rows):
        a += [[0]*cols]
    return a


def S_Matrix(m, row, k):
    """
    Square matrix
    """
    n = len(m)
    r_Oper = Identity(n)
    r_Oper[row][row] = k
    return matrix_mult(r_Oper, m)


def add_S_Matrix(m, s_row, k, t_row):
    """
    Add rows of
    square matrix
    """
    n = len(m)
    r_oper = Identity(n)
    r_oper[t_row][s_row] = k
    return matrix_mult(r_oper, m)


def inverse(m):
    """
    Inverse of matrix m
    """
    n = len(m)
    assert(len(m) == len(m[0]))
    inverse = Identity(n)
    for col in range(n):
        d_row = col
        assert(m[d_row][col] != 0)
        k = 1 / m[d_row][col]
        m = S_Matrix(m, d_row, k)
        inverse = S_Matrix(inverse, d_row, k)
        s_row = d_row
        """
        Gauss Jordan Elimination
        """
        for t_row in range(n):
            if (s_row != t_row):
                k = -m[t_row][col]
                m = add_S_Matrix(m, s_row,
                                 k, t_row)
                inverse = add_S_Matrix(inverse,
                                       s_row, k,
                                       t_row)
    return inverse
