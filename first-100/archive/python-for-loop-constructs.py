#Problem 1 : Print numbers from 1 to n
num = 8 
for i in range(1,num+1):
  print(i)

#Problem 2 : Print numbers from n to 1
num = 8 
for i in range(num,0,-1):
  print(i)

#Problem 3 : Print even numbers from 2 to n
num = 3 
for i in range(2,num+1,2):
  print(i)

#Problem 4 : Print odd numbers from 1 to n
num = 7 
for i in range(1,num+1,2):
  print(i)

#Problem 5 : Print squares of numbers from 1 to n
import math 
num = 10 
for i in range(1,num+1): 
  print(pow(i,2))

#Problem 6 : Print cubes of numbers from 1 to n
import math
num = 10 
for i in range(1,num+1):
  print(pow(i,3))

#Problem 7 : Find the sum of even numbers from 1 to n
num = 10 
count = 0 
for i in range(1,num+1): 
  if i % 2 == 0: 
    count += i 
print(count)

#Problem 8 : Find the sum of odd numbers from 1 to n
num = 10 
count = 0 
for i in range(1,num+1,2): 
  count += i 
print(count)

#Problem 9 : Find the factorial of a number
num = 6 
count = 1 
for i in range(num,0,-1): 
  count *= i 
print(count)

#Problem 10 : Print the multiplication table of a number
num = 3 
for i in range(1,11): 
  for j in range(1,11): 
    print(str(i) + ' x ' + str(j) + ' = ' + str(i*j))