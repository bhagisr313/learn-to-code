#Problem 56 : Print 1, 4, 7, 10…
n = 10
temp = n
result = 1
d = 3
while(temp > 0):
    print(result)
    result += d
    temp -= 1

#Problem 57 : Print 2, 6, 18…
n = 20
temp = n
result = 2
m = 3
while(temp > 0):
    print(result)
    result *= m
    temp -= 1

#Problem 58 : Fibonacci series till N
n = 10
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for i in range(0,n+1):
    print(fibonacci(i))

#Problem 59 : Sum of Fibonacci till N
n = 5
result = 0
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1) + fibonacci(num-2)
for i in range(0,n+1):
    result += fibonacci(i)
print(result)

#Problem 60 : Nth Fibonacci number
n = 10
def fibonacci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1 
    else:
        return fibonacci(num-1) + fibonacci(num-2)
print(fibonacci(n))