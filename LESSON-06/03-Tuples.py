# Tuples in Python : Tuples are like list except data and order in tuples won't change

Tuple1 = (1, 2, 3, 6, 7, 8, 8, 8)
print(Tuple1)

# With constructor
Tuple2 = tuple(('Amith', 42, True))
print(Tuple2)

# Type of tuple :
print(type(Tuple1))
print(type(Tuple2))

print('______________________________________________________________')

# To work with tuples we need to make a copy of it :
newList = list(Tuple2)
newList.append('Neil')
newTuple = tuple(newList)
print(newTuple)

print('______________________________________________________________')

# Unpacking Tuples :
(one, two, *hey) = Tuple1
print(one)
print(two)
print(hey)

(one, *two, hey) = Tuple1
print(one)
print(two)
print(hey)

print('______________________________________________________________')

# To count the number of duplicates in a Tuple :
print(Tuple1.count(8))
