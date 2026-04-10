# Problem 11 : Print multiples of 3 up to N
n = 30 
for i in range(3,n+1,3):
    print(i)

# Problem 12 : Skip multiples of 5
n = 50
for i in range(1,n+1):
    if i % 5 != 0:
        print(i)

# Problem 13 : Break when number divisible by 7
n = 60
for i in range(1,n+1):
    if i % 7 == 0:
        break
    print(i)

# Problem 14 : Count numbers divisible by both 3 and 5
n = 32
count = 0
for i in range(1,n+1):
    if i % 3 == 0 and i % 5 == 0:
        count+= 1
print(count)

# Problem 15 : Print first N numbers divisible by 4
n = 5
for i in range(1,n+1):
    print(i*4)