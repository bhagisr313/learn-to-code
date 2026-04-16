#Problem 36 : Pyramid pattern
num = 5
for i in range(0,num):
    for j in range(0,2*num):
        if i+j >= num and j-i <= num:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#Problem 37 : Reverse pyramid
num = 5
for i in range(num-1,-1,-1):
    for j in range(2*num,0,-1):
        if i+j >= num and j-i <= num:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#Problem 38 : Diamond pattern (simple)
num = 4
for i in range(0,2*num):
    for j in range(0,2*num):
        if i+j >= num-1 and j-i <= num-1 and i-j <= num-1 and i+j <= 2*(num-1 + (num-1)/2):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

#Problem 39 : Alternating 1-0 pattern
num = 5
counter = 1
for i in range(0,num):
    for j in range(0,i+1):
        print(counter%2, end=' ')
        counter+=1
    print()

#Problem 40 : Floyd’s triangle
num = 5
counter = 1
for i in range(0,num):
    for j in range(0,i+1):
        print(counter, end=' ')
        counter+=1
    print()