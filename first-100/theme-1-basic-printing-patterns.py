# Problem 1 : Print numbers from 1 to N
if n <= 0:
    print("Invalid input")
else:
    for i in range(1, n + 1):
        print(i)
# Problem 2 : Print even numbers up to N
if n <= 0:
    print("Invalid input")
else:
    for i in range(2, n + 1, 2):
            print(i)
# Problem 3 : Print numbers in reverse
if n <= 0:
    print("Invalid input") 
else:
    for i in range(n,0,-1):
        print(i)  
# Problem 4 : Print sum of first N numbers
if n <= 0:
    print("Invalid input")
else:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
# Problem 5 : Print factorial of N
if n < 0:
    print("Invalid input")
else:
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    print(factorial)