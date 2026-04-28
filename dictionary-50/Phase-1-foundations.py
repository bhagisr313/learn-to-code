# Problem 1 : Create a dictionary with 5 key-value pairs and print all keys
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
print(my_dict)

# Problem 2 : Print all values in a dictionary
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
for key in my_dict:
    print(my_dict[key])

# Problem 3 : Access a value using key (handle missing key safely using .get())
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
print(my_dict.get("Shambhavi"))

# Problem 4 : Add a new key-value pair
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
# Adding new key value
my_dict["Khushi"] = 21

# Problem 5 : Update value of an existing key
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
# Updating new key value
my_dict["Bharghavi"] = 21
print(my_dict)

# Problem 6 : Delete a key using del
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
del my_dict["Chinmay"] # Deleting using key
print(my_dict)

# Problem 7 : Delete a key using .pop()
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
# Deleting using key
my_dict.pop("Shambhavi")
print(my_dict)

# Problem 8 : Check if a key exists in dictionary
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
print("Chinmay" in my_dict) # using in keyword

# Problem 9 : Count total number of keys
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
print(len(my_dict.keys()))

# Problem 10 : Iterate using .items() and print key-value pairs
my_dict = dict()
my_dict["Bharghavi"] = 26
my_dict["Avinash"] =  31
my_dict["Shambhavi"] = 28
my_dict["Chinmay"] = 30
for k,v in my_dict.items():
    print(k,v)