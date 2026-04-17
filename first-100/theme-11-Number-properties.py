#Problem 51 : Armstrong number check
import math
num = 185
temp = num
result = 0
while(temp > 0):
    rem = temp % 10
    result += math.pow(rem,3)
    temp //= 10
print("It's an armstrong number") if num == result else print("It's not an armstrong number")

#Problem 52 : Print Armstrong numbers till N
import math
n = 500
for i in range(1,n+1):
    temp = i
    result = 0
    while(temp > 0):
        rem = temp % 10
        result += math.pow(rem,3)
        temp //= 10
    if i == result:
        print(f"{i} is an armstrong number") 

#Problem 53 : Perfect number check
num = 28
result = 0
for i in range(1,num):
    if num % i == 0:
        result += i
if num == result:
    print(f"{num} is a perfect square number")
else:
    print(f"{num} is not a perfect square number")

#Problem 54 : Print perfect numbers till N
def perfect_number_check(num):
    result = 0
    for i in range(1,num):
        if num % i == 0:
            result += i
    if num == result:
        return True
    else:
        return False

n = 50
for j in range(1,n):
    if perfect_number_check(j):
        print(f"{j} is a perfect number")

#Problem 55 : Strong number
num = 145
temp = num
result = 0
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
while (temp > 0):
    rem = temp % 10
    temp //= 10
    result += factorial(rem)
print(f"{num} is a strong number")if result == num else print(f"{num} is not a strong number")