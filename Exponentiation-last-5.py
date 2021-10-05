def pow_end_5(n):

    n = str(n)
    limit = 4*10**5
    last_n = int(n[len(n)-1])

    if last_n == 5 and int(n) <= limit and int(n) >= -limit:
        res = int(n)**2
    else:
        print('5 is not the last character')
        exit()

    return res
