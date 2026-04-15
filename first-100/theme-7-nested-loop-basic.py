#Problem 31 : Print square pattern
num = 5
for i in range(0,num):
    for j in range(0,num):
        print('*', end=' ')
    print()

#Problem 32 : Print right triangle pattern
num = 10
for i in range(0,num):
    for j in range(0,num):
        if i + j >= num - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Problem 33 : Print inverted triangle
num = 11
for i in range(0,num):
    for j in range(0,num):
        if i <= j and i + j <= num - 1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()

#Problem 34 : Print number triangle
num = 8
count = 1
for i in range(0,num):
    for j in range(0,num):
        if i >= j:
            print(count, end=' ')
            count+=1
        else:
            print(' ', end=' ')
    print()

#Problem 35 : Print multiplication table
num = 5
for i in range(1,num+1):
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()