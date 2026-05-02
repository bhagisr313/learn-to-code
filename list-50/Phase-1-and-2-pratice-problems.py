#Problem 1 : Remove duplicates from list (keep order)
my_list = [1,2,3,4,3]
my_list2 = []
my_set = set()
for i in my_list:
    if i not in my_set:
        my_set.add(i)
        my_list2.append(i)
print(my_list2)

#Problem 2 : Find second largest number
my_list = [0,4,1,3,2]
max_value = float('-inf')
sec_max = float('-inf')
for i in my_list:
    if i > max_value:
        sec_max = max_value
        max_value = i
    elif i > sec_max and i != max_value:
        sec_max = i
print(sec_max)

#Problem 3 : Find all pairs with given sum
arr = [2, 4, 3, 5, 7, 8, 9]
target = 7
for i in range(0,len(arr)-1):
    for j in range(i+1,len(arr)):
        if arr[i] + arr[j] == target:
            print(arr[i],arr[j])

#Problem 4 : Move all zeros to end (maintain order of others)

#Problem 5 : Rotate list by K steps (right rotation)
arr = [2, 4, 3, 5, 7, 8, 9]
k = 5
while k > 0:
    arr = [arr[len(arr)-1], *arr[0:len(arr)-1]]
    k-=1
print(arr)

#Problem 6 : Find intersection of two lists
arr1 = [2, 4, 3, 5, 7, 9]
arr2 = [1, 8, 4]
intersect_arr = []
for i in arr1:
    if i in arr2:
        intersect_arr.append(i)
print(intersect_arr)

#Problem 7 : Find union of two lists (no duplicates)
arr1 = [2, 4, 3, 5, 7, 9]
arr2 = [1, 8, 4]
my_set = set()
for i in arr1:
    my_set.add(i)
for i in arr2:
    my_set.add(i)
print(list(my_set))

#Problem 8 : Find missing number from 1 to N
arr = [4, 2, 1, 3, 6]
N = 6
sum_of_n = (N*(N+1))//2
sum_of_arr = sum(arr)
print(sum_of_n - sum_of_arr)

#Problem 9 : Find all duplicates in list
arr = [1,2,2,3,3,3,4]
result_arr = []
my_set = set()
for i in arr:
    if i not in my_set:
        my_set.add(i)
    else:
        if i not in result_arr:
            result_arr.append(i)
print(result_arr)

#Problem 10 : Merge two sorted lists into one sorted list

#Problem 11 : Find subarray with given sum

#Problem 12 : Kadane’s Algorithm (maximum subarray sum)

#Problem 13 : Check if list is palindrome
arr = [1, 2, 3, 4, 5, 6, 6, 5, 4, 3, 2, 1]
palindrome_flag = True
for i in range(0,len(arr)//2):
    if arr[i] != arr[-(i+1)]:
        palindrome_flag = False
        break
print("It's Palindrome") if palindrome_flag else print("It's not Palindrome")

#Problem 14 : Flatten a nested list (1 level first, then recursive if you can)
#Problem 15 : Find majority element (> n/2 times)
#Problem 16 : Split list into chunks of size K
#Problem 17 : Rearrange positives and negatives alternatively
#Problem 18 : Find longest consecutive sequence
#Problem 19 : Product of array except self
#Problem 20 : Sort list based on frequency of elements