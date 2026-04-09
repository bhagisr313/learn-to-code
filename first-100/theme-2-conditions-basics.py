# Problem 6 : Check if number is positive/negative/zero
num = 5
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# Problem 7 : Check even or odd
num = 4
if num % 2 == 0:
    print("Even")
else:   
    print("Odd")

# Problem 8 : Find greatest of two numbers
num1 = 90
num2 = 90
if num1 > num2:
    print(num1)
elif num1 == num2:
    print("Both are equal")
else:
    print(num2)

# Problem 9 : Find greatest of three numbers
num1 = 105
num2 = 105
num3 = 15
if num1 >= num2 and num1 >= num3:
    print(num1)
elif num2 >= num1 and num2 >= num3:
    print(num2)
else:
    print(num3)

# Problem 10 : Check leap year
year = 1900
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("It's a leap year")
else:
    print("It's not a leap year")