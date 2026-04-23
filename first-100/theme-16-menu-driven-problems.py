#Problem 76 : Menu: sum / product / exit
while True:
    print("""
    1. Sum
    2. Product
    3. Exit""")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        sum_of_numbers = 0 
        numbers = [int(i) for i in input("Enter the numbers: ").split(' ')]
        for i in numbers:
            sum_of_numbers += i
        print(f"Sum = {sum_of_numbers}")
    elif choice == 2:
        product_of_numbers = 1
        numbers = [int(i) for i in input("Enter the numbers: ").split(' ')]
        for i in numbers:
            product_of_numbers *= i
        print(f"Product = {product_of_numbers}")
    elif choice == 3:
        print("Exit Program.")
        break

#Problem 77 : Menu: even/odd check repeatedly
while True:
    print("""
    1. Even/Odd check
    2. Exit""")
    choice = int(input("Enter the choice: "))
    
    if choice == 1:
        number = int(input("Enter the number: "))
        print("Even") if number % 2 == 0 else print("Odd")
    elif choice == 2:
        print("Exit.")
        break
        
#Problem 78 : Calculator using menu
while True:
    print(""" Calculator Menu
    1. Add
    2. Subtract
    3. Multiply
    4. Divide
    5. Exit""")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator.")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", num1 + num2)

    elif choice == 2:
        print("Result:", num1 - num2)

    elif choice == 3:
        print("Result:", num1 * num2)

    elif choice == 4:
        if num2 != 0:
            print("Result:", num1 / num2)
        else:
            print("Cannot divide by zero!")

    else:
        print("Invalid choice! Please try again.")

#Problem 79 : Pattern selector menu
n = int(input("Enter size: "))
print("""
1. Square
2. Right Triangle
3. Inverted Triangle
4. Pyramid""")

choice = int(input("Enter your choice: "))

if choice == 1:
    for i in range(0,n):
        for j in range(0,n):
            print('*', end=' ')
        print()
elif choice == 2:
    for i in range(0,n+1):
        for j in range(i):
            print('*',end=' ')
        print()
elif choice == 3:
    for i in range(n, 0, -1):
        for j in range(i):
            print("*", end=" ")
        print()
elif choice == 4:
    for i in range(n):
        print(" " * (n - i - 1), end="")
        print("* " * (i + 1))
else:
    print("Invalid choice")

#Problem 80 : Number operations menu
print("1. Even or Odd")
print("2. Factorial")
print("3. Prime Check")
print("4. Reverse Number")

choice = int(input("Enter your choice: "))

num = int(input("Enter a number: "))

if choice == 1:
    if num % 2 == 0:
        print("Even Number")
    else:
        print("Odd Number")


elif choice == 2:
    fact = 1
    for i in range(1, num + 1):
        fact *= i
    print("Factorial:", fact)


elif choice == 3:
    if num <= 1:
        print("Not Prime")
    else:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print("Prime Number")
        else:
            print("Not Prime")


elif choice == 4:
    rev = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp //= 10

    print("Reversed Number:", rev)

else:
    print("Invalid Choice")