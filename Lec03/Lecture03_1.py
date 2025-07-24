new_a = 10
b = 30

import math

math.sqrt(new_a + b)

print(new_a)
print(new_a)
print(new_a)
print(new_a)
print(new_a)
print(new_a)


for elem in range(3):
    AddedStr += str(elem)
print(AddedStr)


# See Range
s = range (10, 21)
sum = 0
for a in s:
    sum = sum + a   # sum += a
print (sum)


# Define list
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
type(prime_numbers)

prime_numbers[-2]

# Define a list with strings
data = ['alpha', 'beta', 'gamma', 'delta']
data[2]
data[2] = 'G'

# Delete sequence in a list

del data[1:3]

# Overwrite value in a list

prime_numbers[3] = prime_numbers[6]

# Append list
prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19]
prime_numbers.append(23)

appd_list = [1, 2, 3]
prime_numbers.append(appd_list)

# Reverse

appd_list.reverse()

# Sort

mix_list = [1,5,2,7,4]
mix_list.sort()

# Insert
mix_list.insert(2, 10)
mix_list.sort()

# Remove

mix_list.remove(5)

# Dupliated Nubmers
mix_list = [1, 5, 2, 7, 4, 5]
mix_list.remove(5)

# Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2

# Search in a list

4 in list3
7 in list3
4 not in list3


numbers = list3
for number in numbers:
    if number in numbers:
        numbers.remove(number)


# Cumulative Sum

numbers = [0, 1, 2, 3, 4, 5]
sum = 0
sum_so_far = []

for number in numbers:
    sum += number
    sum_so_far.append(sum)
print(sum_so_far)

# List Operations : *

zeroes = ["A"] * 50

# Usage List : Data Accumulator

nums = []
x = eval (input ("Enter a number: "))
while x >= 0:
    nums.append(x)
    x= eval(input("Enter a number: "))


# Count values in a list
count_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1]
count_list.count(1)

# Pop function

count_list.pop(3)  # Removes the element at index 3 and returns it
#del count_list[3]

# Remove all specified values
while count_list.count(1)>0:
    count_list.remove(1)


# Multi-dimensional Lists

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix[1][1]  # Accessing element at row 1, column 2



######### Dictionaries #########

# Define a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}

print (thisdict)
print (thisdict["brand"])
print(len(thisdict))

# Define a dictionary using dict
thisdict2 = dict(name = "John", age = 36, country = "Norway")

thisdict.get("model")

# Get Keys, Values, and items
thisdict.keys()
thisdict.values()
thisdict.items()

# Update values

thisdict["brand"] = "Toyota"

if "brand" in thisdict:
    print("Brand exists in the dictionary.")

# update item:
thisdict.update({"year": 2020})
thisdict.update({"color": "red"})
thisdict.pop("model")

# Implement For-loop to iterate through keys
for key_elem in thisdict.keys():
    print(key_elem)

for key_elem, value_elem in thisdict.items():
    print("This is key: ", key_elem)
    print("This is value: ", value_elem)
