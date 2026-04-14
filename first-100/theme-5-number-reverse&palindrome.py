#Problem 21 : Reverse a number
num = 12345
temp = num
reversed_num = 0
while(temp > 0):
    rem = temp % 10 
    reversed_num = reversed_num * 10 + rem
    temp //= 10
print(reversed_num)

#Problem 22 : Check palindrome number
num = 12321
temp = num
rev_num = 0
while(temp > 0):
    rem = temp % 10
    rev_num = rev_num * 10 + rem
    temp //= 10
if rev_num == num:
    print(True)
else:
    print(False)

#Problem 23 : Print all palindromes till N
def is_palindrome(num):
    temp = num
    rev_num = 0
    while(temp > 0):
        rem = temp % 10
        rev_num = rev_num * 10 + rem
        temp //= 10
    if rev_num == num:
        return True
    else:
        return False

n = 100
for i in range(1,n+1):
    if is_palindrome(i):
        print(i)

#Problem 24 : Reverse only even digits
digits = 123456
digits_arr = [int(i) for i in list(str(digits))]

even_digits_arr = []
for i in digits_arr:
    if i % 2 == 0:
        even_digits_arr.append(i)

even_digits_arr.reverse()
j = 0
for i in range(0,len(digits_arr)):
    if digits_arr[i] % 2 == 0:
        digits_arr[i] = even_digits_arr[j]
        j+=1
print(digits_arr)

#Problem 25 : Count palindromes in range
def is_palindrome(num):
    temp = num
    rev_num = 0
    while(temp > 0):
        rem = temp % 10
        rev_num = rev_num * 10 + rem
        temp //= 10
    if rev_num == num:
        return True
    else:
        return False

start = 0
end = 50
count = 0
for i in range(start,end+1):
    if is_palindrome(i):
        count+=1
print(count)
