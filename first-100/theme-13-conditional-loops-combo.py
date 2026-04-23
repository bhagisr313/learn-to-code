#Problem 61 : Print numbers divisible by 3 but not 5
limit = 100
for i in range(3,limit+1,3):
    if i % 5 != 0:
        print(i)

#Problem 62 : Count numbers divisible by 2 or 7
limit = 100
count = 0
for i in range(1,limit+1):
    if i % 2 == 0 or i % 7 == 0:
        count += 1
print(count)

#Problem 63 : Print numbers between A and B divisible by both

#Problem 64 : Sum numbers not divisible by 3
limit = 10
sum_result = 0
for i in range(1,limit+1):
    if i % 3 != 0:
        sum_result += i
print(sum_result)

#Problem 65 : Print alternate even numbers
limit = 200
for i in range(2,limit+1,4):
    print(i)