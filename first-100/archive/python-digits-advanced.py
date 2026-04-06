#Problem 1 : Check if a number is divisible by 3 and 5
num = 15 
if num % 3 == 0 and num % 5 == 0: 
  print('Number is divisible by 3 & 5') 
  else: 
    print('Number is not divisible by 3 & 5')

#Problem 2 : Check if a character is uppercase or lowercase
ch = 'h' 
ascii_value = ord(ch) 
if ascii_value >= 65 and ascii_value <= 90: 
  print('Uppercase') 
elif ascii_value >= 97 and ascii_value <= 122: 
  print('Lowercase') 
else: 
  print('Enter the valid character')

#Problem 3 : Check if a number is greater than 100
num = 200 
if num > 100: 
  print('Yes') 
else: 
  print('No')

#Problem 4 : Find the absolute value of a number
num = 200 
if num < 0: 
  num = -num
print(num)

#Problem 5 : Check if a number is even or odd
value = 8 
if value % 2 == 0: 
  print('Even') 
else: 
  print("Odd")

#Problem 6 : Sum of digits of a number
num = 800 
num_str = str(num) 
result = 0 
for i in num_str: 
  result += int(i) 
  print(result)

#Problem 7 : Find the largest digit in a number
num = 88888 
num_str = str(num) 
largest_num = num_str[0] 
for i in num_str: 
  if int(largest_num) < int(i): 
    largest_num = i 
print(largest_num)

#Problem 8 : Find the number of digits in a number
num = 986765 
count = 0 
num_str = str(num) 
for i in num_str: 
  count += 1 
print(count)

#Problem 9 : Reverse a number
num = 9876543210 
num_str = str(num) 
rev_num = '' 
for i in range(len(num_str)-1,-1,-1): 
  rev_num += num_str[i] 
print(rev_num)

#Problem 10 : Check if a number is a palindrome
num = 131 
num_str = str(num) 
rev_num = '' 
for i in range(len(num_str)-1,-1,-1): 
  rev_num += num_str[i]

#Problem 11 : Check if a number is a palindrome
if num_str == rev_num: 
  print("True") else: print("False")

#Problem 12 : Check if a number is a palindrome
if num_str == rev_num: 
  print("True") 
  else: 
    print("False")

#Problem 13 : Print the multiplication table of a number
num = 3 
value = 1 
for i in range(1,11): 
  value = num * i print(str(num) + ' x ' + str(i) + ' = ' + str(value))

#Problem 14 : Find the sum of first n natural numbers
num = 5 
num_str = str(num) 
result = 0 
for i in range(num,0,-1): 
  result += int(i) 
print(result)

#Problem 15 : Count the number of even digits in a number
num = 86420 
count = 0 
num_str = str(num) 
for i in num_str: 
  if int(i) % 2 == 0: 
    count += 1 
print(count)