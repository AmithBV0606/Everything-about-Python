# Lists are one of 4 collection data type in python

users = ['Amith', 'Jhon', 'Sara']

data = ['Amith', 42, False]

emptyList = []

# To check if a specific thing exists in the list :
print('Amith' in users)
print('Amith' in data)
print('Amith' in emptyList)

print('_______________________________________________________')

# Accessing elements of list :
print(users[0])
print(users[-1])
print(users[-2])

print('_______________________________________________________')

# To find a position of specific element :
print(users.index("Sara"))

print('_______________________________________________________')

# Range of values :
print(users[0:3])  # Like slice method in JavaScript
print(users[0:]) # To get all the values
print(users[1:]) # To get all the values after index 1
print(users[-3:-1])

print('_______________________________________________________')

# Length of list :
print(len(users))
print(len(data))

print('_______________________________________________________')

# Lists Data Manipulation Methods :

# To add new elements to the end of the lists :
users.append('Elsa')
print(users)

# users += 'Peter'
users += ['Peter']
print(users)

users.extend(['Robert', 'Jimmy'])
print(users)

# users.extend(data)

print('_______________________________________________________')

# To add new elements whatever the position we want :
users.insert(0, "Bob")
print(users)

users[2:2] = ['Eddie', 'Alex'] # Does not replaces the value at 2nd index
print(users)

# To replace the element :
users[1:3] = ['Robert', 'JPG'] # Does replaces the value at 1st index
print(users)

print('_______________________________________________________')

# Remove elements from the list :
users.remove('Bob')
print(users)

print(users.pop())  # Remove last element
print(users)

del users[0]
print(users)

# del data # It completely deletes the data list
data.clear()
print(data)
