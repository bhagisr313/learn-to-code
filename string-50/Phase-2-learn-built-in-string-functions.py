# Problem 11 : Count occurrences of a character
my_string = "Bharghavi"
ch = "h"
count = my_string.count(ch)
print(count)

# Problem 12 : Check if string starts with a prefix
my_string = "Bharghavi"
prefix = "Bha"
print(my_string.startswith(prefix))

# Problem 13 : Check if string ends with suffix
my_string = "Bharghavi"
suffix = "vi"
print(my_string.endswith(suffix))

# Problem 14 : Find index of a character
my_string = "Bharghavi"
print(my_string.index("i"))

# Problem 15 : Find last index of a character
my_string = "Bharghavi"
ch = "B"
index = my_string.rfind(ch)
print(index)

# Problem 16 : Split a sentence into words
my_string = "My name is Bharghavi"
words = my_string.split( )
print(words)

# Problem 17 : Join list of words into string
words = ['My', 'name', 'is', 'Bharghavi']
sentence = "-".join(words) # provide what do you need in between sentence to join
print(sentence)

# Problem 18 : Check if string contains only alphabets
my_string = "Python0"
print(my_string.isalpha()) # check if the sentence or words has alphabets and numbers

# Problem 19 : Check if string contains only digits
my_string = "986756" # Should be a string of numbers
print(my_string.isdigit()) 

# Problem 20 : Check if string is alphanumeric
my_string = "986756hgh"
print(my_string.isalnum())