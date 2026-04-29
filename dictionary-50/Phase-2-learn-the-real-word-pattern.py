# Problem 11 : Count frequency of each character in a string
my_dict = {}
my_string = "Banana"
for i in my_string:
    if(i in my_dict):
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)

# Problem 12 : Count frequency of elements in a list
my_list = [1, 2, 2, 2, 3, 3]
my_dict = {}
for i in my_list:
    if(i in my_dict):
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)

# Problem 13 : Find the most frequent character
my_string = "bracadabra"
my_dict = {}
for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
max_value = 0
most_occured_key = ''
for k,v in my_dict.items():
    if v > max_value:
        max_value = v
        most_occured_key = k
print(most_occured_key)

# Problem 14 : Find the least frequent element
my_string = "badabdcabdadbdbaab"
my_dict = {}
for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
min_value = max(my_dict.values())
least_occured_key = ''
for k,v in my_dict.items():
    if v < min_value:
        min_value = v
        least_occured_key = k
print(least_occured_key)

# Problem 15 : Count only vowels in a string
my_string = "the quick brown fox jumped on a lazy dog"
my_dict = {}
for i in my_string:
    if i in 'aeiou':
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
print(my_dict)

# Problem 16 : First non-repeating character
my_string = "aabbcdeff"
my_dict = {}
for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
for j in my_string:
    if my_dict[j] == 1:
        print(j)
        break

# Problem 17 : Find all repeating elements
my_string = "aabbcdeff"
my_dict = {}
for i in my_string:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
for j in my_dict:
    if my_dict[j] > 1:
        print(j)

# Problem 18 : Check if two strings are anagrams (using dict)
my_string1 = "cat"
my_string2 = "car"
my_dict = {}
anagram = True
if len(my_string1) == len(my_string2):
    for i in my_string1:
        if i in my_dict:
            my_dict[i] += 1
        else:
            my_dict[i] = 1
    for j in my_string2:
        if j in my_string2 and j in my_dict:
                my_dict[j] -= 1
        else:
            anagram = False
            break
else:
    anagram = False
print("anagram") if anagram else print("not an anagram")

# Problem 19 : Count words in a sentence
sentence = "a boy and a girl"
my_dict = {}
for i in sentence.split(' '):
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
print(my_dict)

# Problem 20 : Top K frequent elements (start with K=1 or 2)
nums = [2,2,2,3,1,1,4,4,4,4]
k = 2 
my_dict = {}
for i in nums:
    if i in my_dict:
        my_dict[i] += 1
    else:
        my_dict[i] = 1
for key,value in sorted(my_dict.items(), key=lambda x: x[1], reverse=True):
    if k > 0:
        print(key)
    k -= 1 