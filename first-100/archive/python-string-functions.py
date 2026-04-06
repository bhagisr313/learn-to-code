#Problem 1 : Print first character of a string
str = "python" 
print(str[0])

#Problem 2 : Print last character of a string
str = "python" 
length = len(str) 
print(str[length - 1])

#Problem 3 : Convert lowercase to uppercase
str = 'Hii' 
result_str = '' 
for i in str: ascii_value = ord(i) 
if ascii_value >= 97 and ascii_value <= 122: 
  ascii_value -= 32 elif ascii_value >= 65 and ascii_value <= 90: 
  ascii_value = ascii_value 
  else:
    print("Enter characters in valid range") 
    result_str += chr(ascii_value) print(result_str)

#Problem 4 : Convert uppercase to lowercase
str = 'Hii' 
result_str = '' 
for i in str: ascii_value = ord(i) if ascii_value >= 65 and ascii_value <= 90: ascii_value += 32 elif ascii_value >= 97 and ascii_value <= 122: ascii_value = ascii_value else: print("Enter characters in valid range") result_str += chr(ascii_value) print(result_str)

#Problem 5 : Concatenate two strings
str1 = 'My name is' 
str2 = 'Bharghavi' 
print(str1 +' ' + str2)

#Problem 6 : Find the length of a string
str = 'Bharghavi' 
count = 0 
for i in str: 
  count += 1 print(count)

#Problem 7 : Count the number of vowels in a string
str = 'Bharghavi' 
count = 0 
for i in str: 
  if i in 'aeiou': 
    count += 1 
print(count)

#Problem 8 : Reverse a string
str = 'Bharghavi' 
reversed_str = '' 
for i in range(len(str)-1,-1,-1): 
  reversed_str += str[i] 
  print(reversed_str)

#Problem 9 : Reverse a string
str = 'Bharghavi' 
reversed_str = '' for i in range(len(str)-1,-1,-1): 
reversed_str += str[i] 
print(reversed_str)

#Problem 10 : Count the number of uppercase characters in a string
str = "BharGhaVi" 
count = 0 
for i in str: 
  ascii_value = ord(i) 
  if ascii_value >= 65 and ascii_value <= 90: 
    count += 1 
print(count)