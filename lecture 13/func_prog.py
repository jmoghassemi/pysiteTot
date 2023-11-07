x = [y * 2 for y in range(10)]
print(x)

keys = ["a", "b", "c"]
values = [1, 2, 3]

dict_compre = {key: value for key, value in zip(keys, values)}

# End of list comprehension --------------

mult2 = lambda x: x * 2

print(mult2(2))

chars = ["a", "b", "c", "d", "e", "f", "g"]
stoi = {ch: i for i, ch in enumerate(chars)}

encode = lambda s: [stoi[c] for c in s]
print(encode("aed"))

# End of Lambda ---------------
# First class functions:


def apply(func, value):
    return func(value)


def square(x):
    return x**2


result = apply(square, 5)
print(result)
