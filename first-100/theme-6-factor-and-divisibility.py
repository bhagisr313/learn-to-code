#Problem 26 : Find factors of a number
num = 840
for i in range(1,int(num/2)+1):
    if num % i == 0:
        print(i)
print(num)

#Problem 27 : Count factors
num = 971
count = 1
for i in range(1,int(num/2)+1):
    if num % i == 0:
        count+=1
print(count)

#Problem 28 : Check prime number
num = 27
count = 1
for i in range(1,int(num/2)+1):
    if num % i == 0:
        count+=1
print("Prime") if count == 2 else print("Not prime")

#Problem 29 : Print primes till N
n = 10
def is_prime(num):
    count = 1
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            count+=1
    return count == 2
    
for i in range(1,n+1):
    if is_prime(i):
        print(i)

#Problem 30 : Sum of prime numbers till N
n = 10
result = 0
def is_prime(num):
    count = 1
    for i in range(1,int(num/2)+1):
        if num % i == 0:
            count+=1
    return count == 2
    
for i in range(1,n+1):
    if is_prime(i):
        result += i
print(result)