# Problem 11 : Find max element in list
my_list = [1,2,3,4,5,6,10]
print(max(my_list))

# Problem 12 : Find min element in list
my_list = [1,2,3,4,5,6,10]
print(min(my_list))

# Problem 13 : Find sum of all elements
my_list = [1,2,3,4,5,6,10]
print(sum(my_list))

# Problem 14 : Reverse list using loop
my_list = [1,2,3,4,5,6,10]
new_list = []
for i in range(len(my_list)-1,-1,-1):
    new_list.append(my_list[i])
print(new_list)

# Problem 15 : Reverse list using .reverse()
my_list = [1,2,3,4,5,6,10]
my_list.reverse() # modifies the original list
print(my_list)

# Problem 16 : Sort list ascending
my_list = [1,2,3,4,5,6,10]
my_list.sort()
print(my_list)

# Problem 17 : Sort list descending
my_list = [1,2,3,4,5,6,10]
my_list.sort(reverse = True) # sorts in descending order
print(my_list)

# Problem 18 : Count occurrences of a number
my_list = [1,5,3,4,5,6,5]
target = 5
print(my_list.count(target))

# Problem 19 : Check if element exists in list
my_list = [1,5,3,4,5,6,5]
target = 5
print(target in my_list)

# Problem 20 : Copy list without reference issue
list1 = [1,2,3]
list2 = list1.copy() # copies without reference

list2.append(4)

print(list1, list2)