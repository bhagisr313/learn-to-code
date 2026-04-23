#Problem 66 : Sum between two numbers
start = int(input("Enter first number: "))
end = int(input("Enter second number: "))

# swap if start is greater than end
if start > end:
    start, end = end, start

total = 0

for i in range(start, end + 1):
    total += i

print("Sum =", total)

#Problem 67 : Count primes in range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# swap if needed
if start > end:
    start, end = end, start

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

count = 0

for num in range(start, end + 1):
    if is_prime(num):
        count += 1

print("Prime count =", count)

#Problem 68 : Print palindromes in range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# swap if needed
if start > end:
    start, end = end, start

print("Palindrome numbers are:")

for num in range(start, end + 1):
    if str(num) == str(num)[::-1]:
        print(num)


#Problem 69 : Count even numbers in range
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))

# swap if needed
if start > end:
    start, end = end, start

count = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        count += 1

print("Even numbers count =", count)

#Problem 70 : Find largest number in range divisible by X
start = int(input("Enter start number: "))
end = int(input("Enter end number: "))
x = int(input("Enter X: "))

# swap if needed
if start > end:
    start, end = end, start

# find largest number <= end that is divisible by x
remainder = end % x
largest = end - remainder

# check if it is inside range
if largest < start:
    print("No number divisible by", x, "in range")
else:
    print("Largest divisible number =", largest)