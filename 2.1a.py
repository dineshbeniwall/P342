# Find the average distance between two points on a --
# straight line made of discrete N (=6) points:	o---o---o---o---o---o
distance = 0
count = 0
n = 0
while n != 6:
    # (0,0)(0,1)..(6,6)
    m = 0
    while m != 6:
        distance += abs(n-m)
        count += 1
        m += 1
    n += 1
print(distance)
avg = distance/count
print('Avg.=', avg)

# 1.944444444444
