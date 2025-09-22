numbers = [1, 2, 3, 4, 5]

# Use map() with a lambda to square each item
squared_numbers = list(map(lambda x: x**2, numbers))
print(squared_numbers)

squared_numbers_ = map(lambda x: x**2, numbers)
print(squared_numbers_) # It gives an iterator object like generator
print(type(squared_numbers_))

for n in squared_numbers_:
    print(n)
    print(type(n))
