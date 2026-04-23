#Problem 71 : Star pattern with odd rows
num = 5
for i in range(0,num):
    for j in range(0,i+1):
        if i % 2 != 0:
            break
        else:
            print('*',end=' ')
    print()

#Problem 72 : Print numbers only on edges of square
n = 5
counter = 0
for i in range(0,n):
    for j in range(0,n):
        counter += 1
        if j > 0 and j < n-1 and i != 0 and i != n-1:
            print('  ', end=' ')
        else:
            if counter < 10:
                print(f" {counter}",end=' ')
            else:
                print(counter ,end=' ')
    print()

#Problem 73 : Hollow square pattern
n = 6
for i in range(0,n):
    for j in range(0,n):
        if j > 0 and j < n-1 and i != 0 and i != n-1:
            print(' ', end=' ')
        else:
            print('*',end=' ')
    print()

#Problem 74 : Triangle with alternating rows
n = 5
for i in range(0,n):
    for j in range(0,i+1):
        if i % 2 == 0:
            print('1',end=' ')
        else:
            print('0',end=' ')
    print()

#Problem 75 : Pattern with increasing gaps
n = 5
for i in range(0,n):
    for j in range(0,i+1):
        if j > 0 and j < i:
            print(' ',end=' ')
        else:
            print('*',end=' ')
    print()