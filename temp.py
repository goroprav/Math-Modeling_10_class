def mult_func(a):
    
    if (a%4==0 and a%100!=0) or a%400==0:
            print('високосный')
    else:
             print('обыкновенный')
    return a
mult_func(2004)


def prod(A):
    ''' fghg
    '''
    s = 1
    for i in range(0, len(A), 1):
        s = s*A[i]
        print(s)
    
    print('---------')
    return s


N = [2, 4, 6]

print(prod(N))