num = input('Please type the number:')
try:
    n = int(num)
    condition = True
    count = 1
    sum = 1
    cs = 0
    if n > 0:
        while sum-cs > 0.001 and condition:
            if count == n:
                condition = False
            else:
                count = count+1
                cs = sum
                sum = sum+1/count
        print("Sum:", sum, "Number of terms:", count)
    elif n == 0:
        print("Sum is 1 or not defined as per the # QUESTION")
    else:
        nn = -1*n
        while sum-cs > 0.001 and condition:
            if count == nn:
                condition = False
            else:
                count = count+1
                cs = sum
                sum = sum+1/count
        summ = -1*sum
        print("Sum:", summ, "Number of terms:", count)
except ValueError:
    print('Type an integer!')
