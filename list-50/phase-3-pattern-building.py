# Problem 21 : Find second largest element
my_list = [1,4,3,5,6]
max_value = float('-inf')
sec_max = float('-inf')
for i in my_list:
    if i > max_value:
        sec_max = max_value
        max_value = i
    elif i > sec_max and i != max_value:
        sec_max = i
print(sec_max)

# Problem 22 : Find second smallest element
my_list = [1,4,3,5,6]
min_value = float('inf')
sec_min = float('inf')
for i in my_list:
    if i < min_value:
        sec_min = min_value
        min_value = i
    elif i < sec_min and i != min_value:
        sec_min = i
print(sec_min)

# Problem 23 : Remove duplicates from list
my_list = [3,2,4,12,4,2,32,3,24]
my_set = set()
for i in my_list:
    if i not in my_set:
        my_set.add(i)
print(list(my_set))

# Problem 24 : Find duplicate elements
my_list = [3,2,4,12,4,2,32,3,24,2]
my_set = set()
result_list = [ ]
for i in my_list:
    if i not in my_set:
        my_set.add(i)
    elif i not in result_list:
        result_list.append(i)
print(result_list)

# Problem 25 : Find missing number in range 1–N
my_list = [1,2,3,5]
n = 5
sum_of_list = sum(my_list)
sum_of_first_n = n * (n+1)//2
print(sum_of_first_n - sum_of_list)

# Problem 26 : Move all zeros to end

# Problem 27 : Move all negatives to one side
# Problem 28 : Rotate list by 1 position
# Problem 29 : Rotate list by K positions
# Problem 30 : Find intersection of two lists