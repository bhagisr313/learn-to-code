# Problem 16 : Sum of even numbers till N
n = 10
total = 0
for i in range(2, n+1, 2):
    total += i
print(total)

# Problem 17 : Count odd numbers till N
n = 25
count = 0
for i in range(1, n+1, 2):
    count += 1
print(count)

# Problem 18 : Sum of digits of a number
n = 259
temp = n
res = 0
while temp > 0:
    rem = temp % 10
    temp //= 10
    res += rem
print(res)

# Problem 19 : Count digits in number
n = 25900
if n == 0:
    count = 1
else:
    count = 0
    temp = n
    while temp > 0:
        temp //= 10
        count += 1
print(count)

# Problem 20 : Product of digits
n = 2589
temp = n
res = 1
while temp > 0:
    rem = temp % 10
    temp //= 10
    res *= rem
print(res)