#Problem 46 Print numbers till input is negative
while True:
    num = int(input("Enter a number: "))
    
    if num < 0:
        break
    print(num)

#Problem 47 Keep taking input until 0
while True:
    num = int(input("Enter a number: "))
    
    if num <= 0:
        break

#Problem 48 Count inputs greater than 10
count = 0
while True:
    num = int(input())
    if num < 0:
        break
    if num >= 10:
        count += 1
print(count)

#Problem 49 Sum inputs until limit reached
result = 0
limit = int(input("Enter the limit: "))
while True:
    num = int(input("Enter the numbers: "))
    result += num
    if result >= limit:
        break
print(result)

#Problem 50 Find max from user inputs
max_value = 0
max_input = int(input("Enter the value of n: "))

while max_input > 0:
    num = int(input(f"Enter the {max_input} numbers: "))
    
    if max_value < num:
        max_value = num
    max_input -=1
print(max_value)
