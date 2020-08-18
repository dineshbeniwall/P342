num = 3
try:
    n = int(num)
    if n >= 0:
        count = 0
        sum = 0
        while count < n:
            count = count+1
            sum = sum+count
        print("Sum of integers till the input:", sum)
    else:
        nn = -1*n
        count = 0
        sum = 0
        while count < nn:
            count = count+1
            sum = sum+count
        summ = -1*sum
        print("Sum of integers till the input:", summ)
except ValueError:
    print('Type a valid number!')
