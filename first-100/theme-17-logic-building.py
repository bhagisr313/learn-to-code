#Problem 81 : Count numbers with digit 5
num = [45, 5, 6, 67, 78, 53]
count = 0

def digit_extractor(n):
    temp = n
    while(temp > 0):
        rem = temp % 10
        temp //= 10
        if rem == 5:
            return True
    return False
    
for i in num:
    if digit_extractor(i):
        count += 1
print(count)

#Problem 82 : Replace 0 with 1 in number
num = 1020304
temp = num
result = 0

multiplier = 1

while(temp > 0):
    rem = temp % 10
    if rem == 0:
        rem = 1
        
    result = rem * multiplier + result
    multiplier *= 10
    temp //= 10
print(result)

#Problem 83 : Remove last digit repeatedly
num = 54321
temp = num

while(temp > 0):
    print(temp)
    temp //= 10

#Problem 84 : Check if all digits are same
num = 3339
temp = num
last_digit = temp % 10
equal_flag = True
while(temp > 0):
    rem = temp % 10
    temp //= 10
    if not (rem == last_digit):
        equal_flag = False
print("All digits are equal") if equal_flag else print("All digits are not equal")
        
#Problem 85 : Find second largest digit
num = 473918652
temp = num
largest_digit = 0
second_largest = 0
while(temp > 0):
    rem = temp % 10
    if rem > largest_digit:
        second_largest = largest_digit
        largest_digit = rem
    elif rem > second_largest:
        second_largest = rem
    temp //= 10
    
print(second_largest)