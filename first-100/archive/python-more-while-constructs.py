#Problem 1 : Find the largest digit in a number
num = 700 
temp = num 
lar_num = 0 
while(temp > 0): 
  rem = temp % 10 
  if rem > lar_num: 
    lar_num = rem 
    temp //= 10 
  print(lar_num)

#Problem 2 : Find the smallest digit in a number
num = 987 
temp = num 
sma_num = 9 
while(temp > 0): 
  rem = temp % 10 
  if rem < sma_num: 
    sma_num = rem 
  temp //= 10 
print(sma_num)

#Problem 3 : Find the difference between the largest and smallest digits in a number
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

#Problem 4 : Check if all digits in a number are the same
num = 888 
temp = num 
res_digit = temp % 10 
is_same = True 
while(temp > 0): 
  rem = temp % 10 
  if res_digit != rem: 
    print(False) 
    is_same = False 
  temp //= 10 
if (is_same): 
  print(True)

#Problem 5 : Count even digits in a number
num = 123456 
temp = num 
count = 0 
while(temp > 0): 
  rem = temp % 10 
  temp //= 10 
  if rem % 2 == 0: 
    count += 1 
print(count)

#Problem 6 : Count odd digits in a number
num = 1234567 
temp = num 
count = 0 
while(temp > 0): 
  rem = temp % 10 
  temp //= 10 
  if rem % 2 != 0: 
    count += 1 
print(count)

#Problem 7 : Print even digits in a number
digit = 24378 
result = [] 
temp = digit 
while(temp > 0): 
  rem = temp % 10 
  if rem % 2 == 0: 
    result.append(rem) 
  temp //= 10 
for i in result[::-1]: 
  print(i, end=" ")

#Problem 8 : Print odd digits in a number
digit = 24378 
result = [] 
temp = digit 
while(temp > 0): 
  rem = temp % 10 
  if rem % 2 != 0: 
    result.insert(0,rem) 
  temp //= 10 
for i in result: 
  print(i, end=" ")

#Problem 9 : Check if a digit is present in a number
digit = 24378 
result = [] 
temp = digit 
while(temp > 0): 
  rem = temp % 10 
  if rem % 2 != 0: 
    result.insert(0,rem) 
  temp //= 10 
for i in result: 
  print(i, end=" ")

#Problem 9 : Check if a digit is present in a number
digit = 24378 
temp = digit 
is_present = False 
while(temp > 0): 
  rem = temp % 10 
  if rem == digit: 
    is_present = True 
  temp //= 10 
print(is_present)

#Problem 11 : Count even and odd digits in a number
num = 234567 
temp = num 
even_count = 0 
odd_count = 0 
while(temp > 0): 
  rem = temp % 10 
  if rem % 2 == 0: 
    even_count += 1 
  else: 
    odd_count += 1 
  temp //= 10 
print("Even: " + str(even_count)) 
print("Odd: " + str(odd_count))

#Problem 12 : Check if a digit is present in a number
num = 1234556 
digit = 8 
temp = num 
is_present = False 
while(temp > 0): 
  rem = temp % 10 
  if rem == digit: 
    is_present = True 
  break 
  temp //= 10 
print(is_present)