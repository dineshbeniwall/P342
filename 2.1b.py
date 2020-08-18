# 6 by 6 two-dimensional grid (no diagonal connections)
# (0,0,0,0)..(0,0,0,6)
# (0,0,0,1)..(0,0,0,7)
# (0,0,0,6)..(0,0,0,12)
d = 0
i = 0
count = 0
while i != 6:
    j = 0
    while j != 6:
        k = 0
        while k != 6:
            n = 0
            while n != 6:
                d += abs(k-n)+abs(i-j)
                count += 1
                n += 1
            k += 1
        j += 1
    i += 1
print(d, count)
print('Avg.=', d/count)
# 3.888889
