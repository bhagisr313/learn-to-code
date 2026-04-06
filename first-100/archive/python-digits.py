# Problem 11 : Check if a number is even or odd
num = 8
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

# Problem 12 : Check if a number is positive, negative or zero
num = 0
if num == 0:
    print("Zero")
elif num > 0:
    print("Positive")
else: 
    print("Negative")

# Problem 13 : Find the largest of two numbers
a = 100
b = 100
if a > b:
    print(a)
else: 
    print(b)
  
# Problem 14 : Find the largest of three numbers
a = 10
b = 1
if a > b:
    print(a)
else: 
    print(b)

# Problem 15 : Find the largest of three numbers
a = 10
b = 10
c = 10
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
elif c > a and c > b:
    print(c)
else:
    print("All three values are equal")
  
#Problem 16 : Check if a number is divisible by 5
num = 100
if num % 5 == 0:
    print('Divisible by 5')
else:
    print('Not divisible by 5')

#Problem 17 : Check if a string is empty
text = 'Hi'
if text is '':
    print('String is empty')
else:
    print('String is not empty')

#problem 18 : Check if a character is a digit, letter or special character
ch = 'A'
ascii_value = ord(ch)
if ascii_value >= 48 and ascii_value <= 57:
    print("Digit")
elif (ascii_value >= 65 and ascii_value <= 90) or (ascii_value >= 97 and ascii_value <= 122):
    print("Letter")
else:
    print("Please enter the valid input")

#Problem 19 : Find the sum of first n natural numbers
num = 50
total = 0
for i in range(1,num+1):
    total += i
print(total)

#Problem 20 : Find the factorial of a number
num = 5
total = 1
while (num > 0):
    total *= num
    num-= 1
print(total)