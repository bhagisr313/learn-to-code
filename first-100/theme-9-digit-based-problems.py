#Problem 41 : Largest digit in number
num = 876505
temp = num
largest_digit = 0
while(temp > 0):
    rem = temp % 10
    if rem > largest_digit:
        largest_digit = rem
    temp //= 10
print(largest_digit)

#Problem 42 : Smallest digit
num = 865207
temp = num
smallest_digit = 9
while(temp > 0):
    rem = temp % 10
    if rem < smallest_digit:
        smallest_digit = rem
    temp //= 10
print(smallest_digit)

#Problem 43 : Count even digits
num = 53178
temp = num
count = 0
while(temp > 0):
    rem = temp % 10
    if rem % 2 == 0:
        count += 1
    temp //= 10
print(count)

#Problem 44 : Sum of odd digits
num = 53178031
temp = num
result = 0
while(temp > 0):
    rem = temp % 10
    if not (rem % 2 == 0):
        result += rem
    temp //= 10
print(result)

#Problem 45 : Difference between even & odd digit sums
num = 1234560
temp = num
even_sum = 0
odd_sum = 0
while(temp > 0):
    rem = temp % 10
    if rem % 2 == 0:
        even_sum += rem
    else:
        odd_sum += rem
    temp //= 10
print(f"even sum is {even_sum} and odd sum is {odd_sum}.")