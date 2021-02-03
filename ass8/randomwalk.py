import lib
import math
# Random walk
# lib.rnwanalysis(steps, No. of walks, file to store data)
with open('rw1.txt', 'w') as file:
    r1 = lib.rnwanalysis(250, 200, file)
with open('rw2.txt', 'w') as file:
    r2 = lib.rnwanalysis(500, 500, file)
with open('rw3.txt', 'w') as file:
    r3 = lib.rnwanalysis(1000, 1000, file)
with open('rw4.txt', 'w') as file:
    r4 = lib.rnwanalysis(5000, 1000, file)
with open('rw5.txt', 'w') as file:
    r5 = lib.rnwanalysis(10000, 5000, file)

# printing and appending the answer
print("Average Delta X : ", r1[0])
print("Average Delta Y : ", r1[1])
print("Average Displacement : ", r1[2])
print("RMS : ", r1[3])
print("root N : ", math.sqrt(200))

print("Average Delta X : ", r2[0])
print("Average Delta Y : ", r2[1])
print("Average Displacement : ", r2[2])
print("RMS : ", r2[3])
print("root N : ", math.sqrt(500))

print("Average Delta X : ", r3[0])
print("Average Delta Y : ", r3[1])
print("Average Displacement : ", r3[2])
print("RMS : ", r3[3])
print("root N : ", math.sqrt(1000))

print("Average Delta X : ", r4[0])
print("Average Delta Y : ", r4[1])
print("Average Displacement : ", r4[2])
print("RMS : ", r4[3])
print("root N : ", math.sqrt(5000))

print("Average Delta X : ", r5[0])
print("Average Delta Y : ", r5[1])
print("Average Displacement : ", r5[2])
print("RMS : ", r5[3])
print("root N : ", math.sqrt(10000))


'''
For 250 steps and 200 walks:
Average Delta X :  -0.8266661000501686
Average Delta Y :  -1.5040960429282342
Average Displacement :  14.101703102547392
RMS :  15.993984023905949
root N :  14.142135623730951

For 500 steps and 500 walks:
Average Delta X :  0.4099829649860854
Average Delta Y :  -0.06637635889390484
Average Displacement :  19.3292694315621
RMS :  21.812057166498224
root N :  22.360679774997898

For 1000 steps and 1000 walks:
Average Delta X :  0.6925368086439121
Average Delta Y :  -0.12786108481780661
Average Displacement :  27.643509374698056
RMS :  31.368713226644314
root N :  31.622776601683793

For 5000 steps and 1000 walks:
Average Delta X :  2.27258630476794
Average Delta Y :  0.3003250364469931
Average Displacement :  61.36573705014846
RMS :  69.46538633863027
root N :  70.71067811865476

For 10000 steps and 5000 walks:
Average Delta X :  -0.7788739170042102
Average Delta Y :  -0.16111118803700916
Average Displacement :  86.88112367507458
RMS :  98.05587900420413
root N :  100.0
[Finished in 99.362s]
'''
