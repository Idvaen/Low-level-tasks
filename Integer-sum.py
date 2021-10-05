def integer_sum(input):
    n = int(input)
    sum = 0

    if n > 0 and n < 10**4:
        for i in range(n+1):
            sum += i
    elif n < 0 and n > -10**4:
        sum = 1
        for i in range(-n+1):
            sum -= i
    elif n == 0:
        sum = 1
    else:
        print("N less then -10000 or more then 10000")

    return sum
