import lib

a = 1
b = 1.5
c = 2
N = 100
for i in [100, 500, 1000, 2000, 5000, 7000, 10000, 15000, 20000, 50000]:
    v = lib.ellipsoid(a, b, c, i)
    print(f"For N={i} volume of ellipsoid : {v[0]}")
'''
For N=100 volume of ellipsoid : 12.0
For N=500 volume of ellipsoid : 11.904
For N=1000 volume of ellipsoid : 12.888
For N=2000 volume of ellipsoid : 12.492
For N=5000 volume of ellipsoid : 12.384
For N=7000 volume of ellipsoid : 12.713142857142858
For N=10000 volume of ellipsoid : 12.3912
For N=15000 volume of ellipsoid : 12.5712
For N=20000 volume of ellipsoid : 12.4488
For N=50000 volume of ellipsoid : 12.67824
[Finished in 0.47s]
'''
