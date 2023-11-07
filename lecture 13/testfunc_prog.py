# List Comprehension

list1 = [1, 2, 3, 4, 5]
# print(list1)

list2 = []

for i in range(1, 1000):
    list2.append(i)

list3 = [i**2 for i in range(1, 1000)]

dict1 = {"a": 1, "b": 2, "c": {"cd": 1, "ce": 2}}

dict2 = {}
my_chars = ["a", "b", "c"]

"""
for element in enumerate(my_chars):
    print(element)
"""
for i, char in enumerate(my_chars):
    # print(f"index: {i}, character: {char}")
    dict2[char] = i + 1

# print(dict2)

# dict1 = {"a": 1, "b": 2, "c": {"cd": 1, "ce": 2}}
dict3 = {char: i for i, char in enumerate(my_chars)}


# SLUT PÅ LIST COMPREHENSION ------------------------------------------
# NU: Lambda Functions!
def main():
    pass


def mult3(x):
    """This function multiplies by three"""
    return x * 3


mult2 = lambda x: x * 2

my_chars = ["a", "b", "c", "d", "e", "f"]
my_string_input = "fbde"

stoi = {ch: i for i, ch in enumerate(my_chars)}

"""
print(f"The character a has the index: {stoi['a']}")

for c in my_string_input:
    print("My current character in the string is: ", c)
    print("My current encoded index for the char is: ", stoi[c])
"""

encode = lambda my_string: [stoi[c] for c in my_string]

# print(encode(my_string_input))

# when done with assignment you should be able to:
# Run print(decode(encode(my_string_input))) and get back exactly my_string_input


# END OF LAMBDA FUNCTIONS ----------------
# Start of First Class Functions


def apply(func, value):
    return func(value)


def square(value):
    return value**2


def powerofthree(value):
    return value**3


result = apply(square, 5)
result2 = apply(powerofthree, 5)
copy_of_square = square

print(copy_of_square(4))

# print(result)
# print(result2)
