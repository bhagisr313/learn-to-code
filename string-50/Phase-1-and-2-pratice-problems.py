#Problem 1 : Check if a string is a palindrome (ignore spaces & case)
my_string1 = "A man a plan a canal Panama"
my_string2 = (my_string1.replace(" ", "")).lower()
result_str = ""
for i in my_string2[::-1]:
    result_str += i
print("It is Palindrome") if result_str == my_string2 else print("It's not a pallindrome")

#Problem 2 : Find the longest word in a sentence
my_string =  "I love solving challenging problems in Python"
my_string2 = my_string.split(" ")
max_value = len(my_string2[0])
for i in my_string2:
    if len(i) > max_value:
        max_value = len(i)
print(max_value)

#Problem 3 : Reverse words in a sentence (not characters)
my_string1 = "I love Python"
reversed_str = my_string1.split(" ")[::-1]
result_str = " ".join(reversed_str)
print(result_str)

#Problem 4 : Remove all duplicate characters from a string
my_str = "programming"
result_str = ""
my_set = set()
for i in my_str:
    if i not in my_set:
        my_set.add(i)
        result_str += i
print(result_str)

#Problem 5 : Find the first repeated character
my_str = "programming"
my_set = set()
for i in my_str:
    if i not in my_set:
        my_set.add(i)
    else:
        print(i)
        break

#Problem 6 : Count number of words in a sentence (handle multiple spaces)
my_str =  "   Hello   world   from   AI   "
count = 1 if my_str[0] != " " else 0
for i in range(0,len(my_str)-1):
    if my_str[i] == " " and my_str[i+1] != " ":
        count += 1
print(count)

#Problem 7 : Capitalize first letter of each word (like title case manually)
my_str = "i love python programming"
my_str2 = " "
if my_str[0] != " ":
    my_str2 += my_str[0].upper()
for i in range(1,len(my_str)):
    if my_str[i-1] == " " and my_str[i] != " ":
        my_str2 += my_str[i].upper()
    else:
        my_str2 += my_str[i]
print(my_str2)

#Problem 8 : Check if two strings are rotations of each other
s1 = "waterbottle"
s2 = "erbottlewat"
length_s1 = len(s1)
rotation_flag = False
def right_rotation(s1):
    return s1[1::] + s1[0]
while  s1 != s2 and length_s1 > 0:
    s1 = right_rotation(s1)
    if s1 == s2:
        rotation_flag = True
        print("s1 and s2 are rotations") 
    length_s1 -= 1

if rotation_flag == False:
    print("s1 and s2 are not rotations")

#Problem 9 : Compress string (e.g., "aaabbc" → "a3b2c1")
my_str = "aaabbccaaa"
result_str = ""
count = 1
for i in range(1,len(my_str)):
    if my_str[i]  == my_str[i-1]:
        count += 1
    else:
        result_str += my_str[i-1] + str(count)
        count = 1
    if i == len(my_str)-1:
        result_str += my_str[i] + str(count)
print(result_str)

#Problem 10 : Find longest substring without repeating characters

#Problem 11 : Check if a string contains all unique characters
my_str = "abcdefghtay"
my_set = set()
for i in my_str:
    my_set.add(i)
print("Unique") if len(my_str) == len(my_set) else print("Not unique")

#Problem 12 : Find the most frequent word in a paragraph
my_str = "a boy and a girl"
my_list = my_str.split(" ")
my_dict = {}
for i in my_list:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
max_value = 0
key = ""
for k,v in my_dict.items():
    if v > max_value:
        max_value = v
        key = k
print(key)

#Problem 13 : Replace multiple spaces with a single space
my_str = "    I   love    Python   programming    "
result_str = my_str[0]
for i in range(1,len(my_str)):
    if my_str[i-1] != " " or my_str[i] != " ":
        result_str += my_str[i]
print(result_str)

#Problem 14 : Check if string is a valid palindrome after removing one char
#Problem 15 : Find all substrings of a string
#Problem 16 : Count occurrences of each word (not char)
#Problem 17 : Find the second most frequent character
my_str = "aabbbbccde"
my_dict = {}
for i in my_str:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
max_value = 0
sec_max = 0
key = " "
for k,v in my_dict.items():
    if v > max_value:
        max_value = v
for k1,v1 in my_dict.items():
    if v1 > sec_max and v1 != max_value:
        sec_max = v1
        key = k1
print(key)

#Problem 18 : Check if one string is a subsequence of another
#Problem 19 : Group anagrams from a list of strings
#Problem 20: Find the longest common prefix among list of strings