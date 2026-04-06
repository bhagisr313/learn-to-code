#Problem 1 : Print multiples of 4 from 1 to n
n = 24 
for i in range(1,n+1): 
  if i % 4 == 0: 
    print(i)

#Problem 2 : Print multiples of 3 from n to 1
n = 24 
for i in range(n,0,-1): 
  if i % 3 == 0: 
    print(i)

#Problem 3 : Find the sum of first n natural numbers
n = 6 
sum = 0 
for i in range(1,n+1): 
  sum += i 
print(sum)

#Problem 4 : Find the sum of squares of first n natural numbers
n = 7 
sum = 0 
for i in range(1,n+1): 
  sum += (i * i) 
print(sum)

#Problem 5 : Find the sum of squares of first n natural numbers
n = 7 
sum = 0 
for i in range(1,n+1): 
  sum += (i * i) 
print(sum)

#Problem 6 : Find the factorial of a number
n = 5 
pro = 1 
for i in range(n,0,-1): 
  pro *= i 
print(pro)

#Problem 7 : Print the multiplication table of a number
n = 8 
for i in range(1,11): 
  print(str(n) + ' x ' + str(i) + ' = ' + str(n * i) )

#Problem 8 : Print the multiplication table of a number
n = 8 
for i in range(1,13): 
  print(str(n) + ' x ' + str(i) + ' = ' + str(n * i))

#Problem 9 : Count consonants in a string
string = "Bharghavi" 
count = 0 
for i in string: 
  if i not in 'aeiou': 
    count += 1 
print(count)

#Problem 10 : Count vowels in a string
string = "Bharghavi" 
count = 0 
for i in string: 
  if i not in 'aeiou': 
    count += 1 
print(count)

#Problem 11 : Print numbers from 1 to n which are divisible by 2 or 3
n = 25 
for i in range(1,n+1): 
  if i % 2 == 0 or i % 3 == 0: 
    print(i)

#Problem 12 : Print multiples of 4 from 1 to n
n = 40 
for i in range(1,n+1): 
  if i % 4 == 0: 
    print(i)

#Problem 13 : Print multiples of 5 from 1 to n
n = 40 
for i in range(1,n+1): 
  if i % 5 == 0: 
    print(i)

#Problem 14 : Find the sum of even numbers from 1 to n
n = 40 
result = 0 
for i in range(1,n+1): 
  if i % 2 == 0: 
    result += i 
print(result)

#Problem 15 : Find the product of multiples of 3 from 1 to n
n = 10 
result = 1 
for i in range(1,n+1): 
  if i % 3 == 0: 
    result *= i 
print(result)

#Problem 16 : Print prime numbers from 1 to n
n = 10 
for num in range(2,n+1): 
  for i in range(2,num): 
    if num % i == 0: 
      break 
  else: 
    print(num)

#Problem 17 : Print prime numbers from 1 to n
n = 10 
for num in range(2,n+1): 
  for i in range(2,num): 
    if num % i == 0: 
      break 
  else: 
    print(num)

#Problem 18 : Find the largest digit in a number
num = 700 
temp = num 
lar_num = 0 
while(temp > 0): 
  rem = temp % 10 
  if rem > lar_num: 
    lar_num = rem 
  temp //= 10 
print(lar_num)

#Problem 19 : Find the smallest digit in a number
num = 987 
temp = num 
sma_num = 9 
while(temp > 0): 
  rem = temp % 10 
  if rem < sma_num: 
    sma_num = rem 
  temp //= 10 
print(sma_num)

#Problem 20 : Find the difference between the largest and smallest digits in a number
num = 987 
temp = num 
lar_num = temp % 10 
sma_num = temp % 10 
while(temp > 0): 
  rem = temp % 10 
  if rem < sma_num: 
    sma_num = rem 
  if rem > lar_num: 
    lar_num = rem 
  temp //= 10 
print(lar_num - sma_num)